#!/usr/bin/env python
# --*-- coding: UTF-8 --*--
from ftplib import FTP
import sys
f=FTP('ftp.funet.fi')
f.login()
f.cwd('/pub/linux/kernel/v1.0')
f.voidcmd("TYPE I")
datasock,estsize=f.ntransfercmd("RETR linux-1.0.tar.gz")
transbytes=0
fd=open('linux-1.0.tar.gz','wb')
while 1:
	buf=datasock.recv(2048)
	if not len(buf):
		break
	fd.write(buf)
	transbytes +=len(buf)
	print ("Recepción de %d" %transbytes)
	if estsize:
		print (" en %d bites (%.1f%%)\r"%(estsize,100.0*float(transbytes)/float(estsize)))
	else:
		print ("bytes\r")
	print ("\n")
fd.close()
datasock.close()
f.voidresp()
f.quit()
