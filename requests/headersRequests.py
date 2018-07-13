import requests

if __name__ == "__main__":
    response = requests.get("http://www.google.com")
    for header in response.headers.keys():
        print (header  + ":" + response.headers[header])
