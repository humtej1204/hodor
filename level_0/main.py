#!/usr/bin/python3
import requests

datos = {'id':'3670','holdthedoor':'\n'}

for i in range(1024):
    r = requests.post('http://158.69.76.135/level0.php', data = datos)
    print("Vamos {} veces...".format(i))

