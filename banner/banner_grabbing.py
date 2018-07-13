import socket
import sys

import argparse

parser = argparse.ArgumentParser(description='Banner grabbing')
    
# Main arguments
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.1]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number",type=int, required=True)

parsed_args = parser.parse_args() 

portList ="21,22"

for ip in range(1,parsed_args.machines):
	#vulnbanners = open('vulnbanners.txt', 'r')
	for port in (21,22):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(( str(parsed_args.network +'.' + str(ip)), int(port) ))
			print 'Connecting to '+str(parsed_args.network +'.' + str(ip) )+' in the port: '+str(port)
			sock.settimeout(1)
			banner = sock.recv(1024)
			print banner
			sock.close()
			'''for vulnbanner in vulnbanners:
				if banner.strip() in vulnbanner.strip():
					print 'We have found a banner! '+banner
					print 'Host: '+str(parsed_args.network + '.' + str(ip))
					print 'Port: '+str(port)'''
		except Exception,e:
			print str(e)
			print 'Error connecting to: '+str(parsed_args.network + '.'+ str(ip)) +':'+ str(port) 
			pass