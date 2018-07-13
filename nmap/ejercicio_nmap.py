#!/usr/bin/python

#importar nmap e inicializar portScanner
import nmap                       
nm = nmap.PortScanner()

#pedimos al usuario el host que vamos a escanear
host_scan = raw_input('Host scan: ')
while host_scan == "":
    host_scan = raw_input('Host scan: ')

#ejecutar nmap
portlist="21,22,23,25,80,8080"	
nm.scan(hosts=host_scan, arguments='-n -p'+portlist)

#mostrar comando nmap a ejecutar
print (nm.command_line())
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

#tratamiento fichero
archivo = open('scan.txt', 'w')
for host, status in hosts_list:
    print (host, status)
    archivo.write(host+'\n')

#mostrar estado de cada puerto
array_portlist=portlist.split(',')
for port in array_portlist:
	state= nm[host_scan]['tcp'][int(port)]['state']
	print ("Port:"+str(port)+" "+"State:"+state)
	archivo.write("Port:"+str(port)+" "+"State:"+state+'\n')

#cierre fichero
archivo.close()
