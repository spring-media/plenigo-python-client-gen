#!/bin/python3

import os
import json
import argparse
from copy import deepcopy

# Operations that we want to remove from paths
METHODS_TO_REMOVE = {"put", "post", "delete", "options", "head", "patch", "trace"}

# Function to find $ref values and gather them into a set
def find_ref_values(data, ref_set=None):
    if ref_set is None:
        ref_set = set()

    if isinstance(data, dict):
        for key, value in data.items():
            if key == "$ref":
                ref_set.add(value.split('/')[-1])
            else:
                find_ref_values(value, ref_set)
    elif isinstance(data, list):
        for item in data:
            find_ref_values(item, ref_set)

    return ref_set

# Function to load the OpenAPI specification JSON file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Gather references based on the given endpoints
def gather_references(openapi_spec, endpoints):
    all_references = set()
    for endpoint in endpoints:
        path_item = openapi_spec.get('paths', {}).get(endpoint, {})
        new_schema_references = find_ref_values(path_item)
        all_references.update(new_schema_references)
    return all_references

# Search schemas for additional references recursively
def search_schemas(openapi_spec, all_references):
    schemas_seen_so_far = all_references.copy()
    already_searched = set()
    while schemas_seen_so_far:
        schema_to_search = schemas_seen_so_far.pop()
        already_searched.add(schema_to_search)
        try:
            schema_to_search_obj = openapi_spec["components"]["schemas"][schema_to_search]
        except KeyError:
            print(f"Schema {schema_to_search} not found. This is probably an Example or Parameter, so we can skip.")
            continue

        new_sub_schemas = find_ref_values(schema_to_search_obj)
        all_references.update(new_sub_schemas)
        for sub_schema in new_sub_schemas:
            if sub_schema not in already_searched:
                schemas_seen_so_far.add(sub_schema)
    return all_references

def remove_http_methods_we_dont_care(openapi_spec):
    new_openapi = deepcopy(openapi_spec)
    if "paths" not in new_openapi:
        return new_openapi
    
    for path, path_item in new_openapi["paths"].items():
        # path_item is a dictionary of methods => operationObject
        methods_to_delete = []
        for method in path_item.keys():
            if method.lower() in METHODS_TO_REMOVE:
                methods_to_delete.append(method)
        # Actually remove them
        for m in methods_to_delete:
            del path_item[m]
    return new_openapi


# Filter the OpenAPI specification based on the endpoints and references
def filter_openapi_spec(openapi_spec, endpoints, all_references):
    new_open_api = deepcopy(openapi_spec)
    new_open_api['paths'] = {path: item for path, item in openapi_spec['paths'].items() if path in endpoints}
    new_open_api["components"]["parameters"] = {param: item for param, item in openapi_spec["components"]["parameters"].items() if param in all_references}
    new_open_api["components"]["schemas"] = {schema: item for schema, item in openapi_spec["components"]["schemas"].items() if schema in all_references}
    new_open_api["components"]["examples"] = {example: item for example, item in openapi_spec["components"]["examples"].items() if example in all_references}
    return new_open_api

# Save the filtered OpenAPI specification to a JSON file
def save_openapi_spec(file_path, openapi_spec):
    abs_path = os.path.abspath(file_path.strip())
    with open(abs_path, 'w') as file:
        json.dump(openapi_spec, file, indent=2)

def allOf_fixer(openapi_spec):
    # fix the openapi spec because it might contain allOf entries that were not "correctly" created
    # the correct way is to get all the keys inside the schemas dictionary beside the allOf key and create a new dictionary with those keys
    # and append this new dictionary to the allOf list and also erase the original keys, keeping only the allOf key
    openapi_spec = deepcopy(openapi_spec)
    for schema in openapi_spec["components"]["schemas"]:
        schema_obj = openapi_spec["components"]["schemas"][schema]
        if "allOf" in schema_obj:
            all_of_obj = schema_obj["allOf"]
            new_schema_obj = {}
            for key in schema_obj:
                if key != "allOf":
                    new_schema_obj[key] = schema_obj[key]
            if new_schema_obj:
                all_of_obj.append(new_schema_obj)
            openapi_spec["components"]["schemas"][schema] = {"allOf": all_of_obj}
    return openapi_spec

def enum_deduplicator(openapi_spec):
    # look for "enum" keys in the dictionary recursively
    # because the dictionary might contain other dicts or arrays
    # if the key is found, make sure that the contents of the enums list are unique
    openapi_spec = deepcopy(openapi_spec)
    def enum_deduplicator_helper(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "enum":
                    seen = set()
                    deduplicated_list = []
                    for item in value:
                        if item not in seen:
                            deduplicated_list.append(item)
                            seen.add(item)
                    data[key] = deduplicated_list
                else:
                    enum_deduplicator_helper(value)
        elif isinstance(data, list):
            for item in data:
                enum_deduplicator_helper(item)
    enum_deduplicator_helper(openapi_spec)
    return openapi_spec

def delete_key_from_dict(data, key):
    # because the dictionary might contain other dicts or arrays
    # if the key is found, delete it
    if isinstance(data, dict):
        for k, v in list(data.items()):
            if k == key:
                del data[k]
            else:
                delete_key_from_dict(v, key)
    elif isinstance(data, list):
        for item in data:
            delete_key_from_dict(item, key)



# Main function to set up the CLI
def main():
    parser = argparse.ArgumentParser(description="Filter an OpenAPI specification based on specific endpoints.")
    parser.add_argument("input_file", help="Path to the OpenAPI specification JSON file")
    parser.add_argument("output_file", help="Path to save the filtered OpenAPI specification")
    parser.add_argument("endpoints_file", help="Path to the YAML file containing the list of endpoints")

    args = parser.parse_args()

    # Load the OpenAPI specification and endpoints
    openapi_spec = load_json_file(args.input_file)
    endpoints = load_json_file(args.endpoints_file)
    
    openapi_spec = remove_http_methods_we_dont_care(openapi_spec)

    # Gather and search references
    all_references = gather_references(openapi_spec, endpoints)
    all_references = search_schemas(openapi_spec, all_references)

    # Filter the OpenAPI spec
    new_open_api = filter_openapi_spec(openapi_spec, endpoints, all_references)

    new_open_api = allOf_fixer(new_open_api)
    new_open_api = enum_deduplicator(new_open_api)

    schema_obj = new_open_api["components"]["schemas"]
    #delete_key_from_dict(schema_obj, "required")
    #delete_key_from_dict(new_open_api, "enum")


    # Deletes examples because we don't need them and they are usually wrong anyways
    del new_open_api["components"]["examples"]

    # Save the filtered spec
    save_openapi_spec(args.output_file, new_open_api)

if __name__ == "__main__":
    main()
