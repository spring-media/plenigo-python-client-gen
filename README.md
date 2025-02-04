# Plenigo API client 

This is an unofficial client for the [Plenigo API](https://api.plenigo.com/) and is generated with the help of [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) based on the OpenAPI specs provided by Plenigo.

This sdk is tailored to the specific needs of Axel Springer and likely won't work for your needs out of the box. For ex we remove unwanted paths, schemas out of the openapi spec because there were a lot of bugs and errors inside the spec given by plenigo that prevented us from compiling a working version for our needs. By reducing the openapi spec to only the paths we needed, we were able to reduce the blast radius of bugs.

If you need a new path that is not specified in the ./scripts/endpoints.json file, just update the file with the new path like this:
```json
[
  "/customers",
  ...
]
```

You can download the most recent OpenAPI specs from the [Plenigo API documentation](https://api.plenigo.com). The `openapi.json` file in this repo is a copy of the revision used when the client was last generated.

## :dart: Usage

```python
from plenigo import AuthenticatedClient, Environment
from plenigo.api.transactions.search_transactions import sync_all

# Create a client for the staging environment; use Environment.PRODUCTION for the live API
client = AuthenticatedClient(base_url=str(Environment.STAGING), token="YourAPIkey")

all_transactions = sync_all(client=client, size=30)
```

## :gear: Install

As the client is available in one of the subdirectories we need to install it with:

```
pip install -e "git+ssh://git@github.com/spring-media/plenigo-python-client-gen.git@main#egg=plenigo-client&subdirectory=plenigo-client"
```

## Development

Install the generator itself:

```sh
pip install openapi-python-client
```

The OpenAPI Python client version is pinned to a version compatible with the OpenAPI specs published by Plenigo. At the time of writing, the OpenAPI specs are version 3.1.0 and the generator version is 0.17.3. See the comments in `requirements.txt` for more information.

Generate the client:

```sh
openapi-python-client generate \
  --path openapi.json \
  --config config.yml
  --custom-template-path templates
```

If you need to make any changes, then update only the templates in the `templates` folder and the `config.yml` file and re-run the `generate` command with the `--overwrite` option:

```sh
openapi-python-client generate \
  --overwrite \
  --path openapi-<version>.json \
  --config config.yml \
  --custom-template-path templates \
  --output-path=plenigo-client
```

### Generating the client from the specs

When updating the OpenAPI specs and/or the generator client, pay attention to version compatibility and template code (when using the `--custom-template-path` option).

Additional logic was added to the client via the templates and config file:

* `sync_all`, `asyncio_all` - pull all the data from a given endpoint, using pagination
* retry logic for all endpoints with exponential backoff
* debug logging 

It helps to compare the Jinja templates that come with the generator package with those in this repo and adjust accordingly. 
