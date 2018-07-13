# Port Scanner
from socket import *                          # Importamos modulo socket
ip=raw_input("Introduce IP : ")               # Preguntamos por la IP
start=input("Introduce puerto de inicio : ")  # Preguntamos por el puertos
end=input("Introduce puerto de fin : ")      
print ("Escaneando IP {} : ".format(ip))
for port in range(start,end):                 # Bucle
    print ("Probando puerto {} ...".format(port))
    s=socket(AF_INET, SOCK_STREAM)            # Crea el objeto socket
    s.settimeout(5)                           # set timeout  
    if(s.connect_ex((ip,port))==0):           # Comprobar conexion
        print ("Port " , port, "is open")       # Prints open port
    s.close()                                 # Cierra el socket
print ("Escaneo finalizado! ")
