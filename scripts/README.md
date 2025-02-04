## trim_down_openapi_spec

The trim_down_openapi_spec.py takes an OpenAPI specification file (in JSON format) and a list of specific endpoints that you want to keep. It then filters out everything in the spec that isn't relevant to those endpoints, cleaning up the resulting file by:

1. Removing operations you don't care about (e.g., PUT, POST, DELETE, etc.).
2. Keeping only the paths you specify (the ones in the endpoints list).
3. Gathering and retaining the associated schema references for those paths (so that only relevant schemas remain).
4. Handling allOf definitions in a “corrected” way.
5. Ensuring enums don’t have duplicated values.
6. Deleting the examples section from components (since examples can be large and/or out of date).

#### Usage
The script takes three positional arguments:

1. input_file — Path to the original OpenAPI JSON file
2. output_file — Path to where you want the filtered spec to be saved
3. endpoints_file — Path to the JSON file containing your endpoints

For example:

```bash
python3 filter_openapi.py openapi.json filtered_openapi.json endpoints.json
```

If you are in the project root directory and in a linux machine, you can run the code like this:

```bash
./scripts/trim_down_openapi_spec.py ./openapi_specs/latest/openapi-v241218-MINOR.json ./openapi_specs/latest/openapi-v241218-MINOR-trimmed-down.json ./scripts/endpoints.json
```

This will trim down the openapi-v241218-MINOR.json openapi spec, creating the openapi-v241218-MINOR-trimmed-down.json 
