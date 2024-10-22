# check https://api.plenigo.com/ website, parse the html and check the version of the openapi spec
# the version looks something like this as text: plenigo API v3 (API.241015-MAJOR)
# and this as html:<h1 class="sc-fujyAs sc-dFRpbK bpZWeL fdKBSs">plenigo API v3<!-- --> <span>(<!-- -->API.241015-MAJOR<!-- -->)</span></h1>
# the file containing the openapi spec can be found in the html: <p>Download OpenAPI specification<!-- -->:<a download="openapi.json" target="_blank" class="sc-bsatvv gidAUi" href="blob:https://api.plenigo.com/34a50f04-3802-4d2d-8bb9-7b1e12f1246e">Download</a></p>

import requests
from bs4 import BeautifulSoup
import json
import os
import sys

url = 'https://api.plenigo.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
version = soup.find('h1').text
# get words inside the parenthesis
version = version.split('(')[1].split(')')[0]

# list the files in the openapi_specs folder
# open the fist folder and check the version
# if the version is different, print a message
latest_folder_path = "./openapi_specs/latest"
files = os.listdir(latest_folder_path)
file_path = os.path.join(latest_folder_path, files[0])
with open(file_path, 'r') as file:
    openapi_spec = json.load(file)
current_prod_version = openapi_spec['info']['version']
if version != current_prod_version:
    print(f"Version mismatch: Current version is {current_prod_version} while the website version is {version}")
    sys.exit(1)
else:
    print("We are currently using the latest version")
    sys.exit(0)



