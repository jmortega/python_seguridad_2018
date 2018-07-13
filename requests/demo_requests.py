#!/bin/python
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r = requests.get("http://" +url)
print (r.status_code)
print (r.url)
data = r.text
print (data)
