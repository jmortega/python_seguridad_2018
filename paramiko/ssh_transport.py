import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    transport = paramiko.Transport(ip)
    try:
        transport.start_client()
    except Exception as e:
        print(e)
    
    try:
        transport.auth_password(username=user,password=passwd)
    except Exception as e:
        print(e)
        
    if transport.is_authenticated():
        print (transport.getpeername())
        channel = transport.open_session()
        channel.exec_command(command)
        response = channel.recv(1024)
        print ('Command %r(%r)-->%s' % (command,user,response))

ssh_command('192.168.1.233', 'msfadmin', 'msfadmin','ls -la')
