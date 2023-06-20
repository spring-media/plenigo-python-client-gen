# Plenigo API client 

This is an unofficial client for [Plenigo API](https://api.plenigo.com/) and is generated with the help of [openapi-python-client](https://github.com). 

Keep in mind that not all the endpoints have been tested, make sure that you check the client code and try it out on staging envirionment before using it in production.

> openapi.json is available in the repo and went thru some manual changes so that the client can be properly generated.

## Usage

```python
from plenigo import AuthenticatedClient, PlenigoApi
from plenigo.api.transactions.search_transactions import sync_all
from plenigo.api import jsonable_encoder

client = AuthenticatedClient(api=PlenigoApi.STAGE, token="YourAPIkey")

all_transactions = sync_all(client=client, size=30)

# if needed you can encode the data to json
jsonable_encoder(all_transactions)
```

Additional logic was added to the client via the templates and config file:

* pagination support (sync_all, asyncio_all)
* retry logic for all endpoints with exponential backoff
* debug logging 

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

