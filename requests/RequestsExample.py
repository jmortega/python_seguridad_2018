# -*- encoding: utf-8 -*-

import requests, json

print ("Requests Library tests.")
responseGet = requests.get("http://www.google.es")

print (responseGet.text.encode('utf-8'))

print (responseGet.json)

print (responseGet.encoding)

print (responseGet.content)

print ("Status code: "+str(responseGet.status_code))

print ("Headers response: ")
for header, value in responseGet.headers.items():
  print(header, '-->', value)
  
print ("Headers request : ")
for header, value in responseGet.request.headers.items():
  print(header, '-->', value)
