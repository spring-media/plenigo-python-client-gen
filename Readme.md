# Plenigo API client 

This is an unofficial client for [Plenigo API](https://api.plenigo.com/) and is generated with the help of [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). 

Keep in mind that not all the endpoints have been tested, make sure that you check the client code and try it out on staging envirionment before using it in production.

> openapi.json is available in the repo and went thru some manual changes so that the client can be properly generated.

## :dart: Usage

```python
from plenigo import AuthenticatedClient, PlenigoApi
from plenigo.api.transactions.search_transactions import sync_all

client = AuthenticatedClient(api=PlenigoApi.STAGE, token="YourAPIkey")

all_transactions = sync_all(client=client, size=30)
```

## :gear: Install

As the client is available in one of the subdirectories we need to install it with:

```
pip install -e "git+ssh://git@github.com/spring-media/plenigo-python-client-gen.git@main#egg=plenigo-client&subdirectory=plenigo-client"
```

## Development

Install the generator itself
```sh
pip install openapi-python-client
```

Generate the client
```sh
openapi-python-client generate --path openapi.json --custom-template-path templates --config config.yml
```

If you need to make any changes then update only the templates in the `templates` folder and the config.yaml file.
```sh
openapi-python-client update --path openapi.json --custom-template-path templates --config config.yml
```

Additional logic was added to the client via the templates and config file:

* sync_all, asyncio_all - pull all the data from a given endpoint (going thru pagination)
* retry logic for all endpoints with exponential backoff
* debug logging 

