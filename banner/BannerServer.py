#!/usr/bin/python3
# Obtain server banner

import socket
import re
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Obtain server banner')
    
    # Main arguments
    parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
    parser.add_argument("-proxy", dest="proxy", help="Proxy[IP:PORT]", required=None)

    parsed_args = parser.parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((parsed_args.target, 80))	
	

    http_get = b"GET / HTTP/1.1\nHost: "+parsed_args.target+"\n\n"
    data = ''
    try:
	sock.sendall(http_get)
	data = sock.recvfrom(1024)
	print data
    except socket.error:
	print ("Socket error", socket.errno)
    finally:
	print("closing connection")
	sock.close()

    strdata = data[0]
    #  looks like one long line so split it at newline into multiple strings
    headers = strdata.splitlines()
    #  use regular expression library to look for the one line we like
    for s in headers:
	if re.search('Server:', s):
	    print(s)
		
