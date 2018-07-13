import ftplib

def ftpListDirectory(ftp):
    try:
        dirList = ftp.nlst()
        print (dirList)
    except:
        dirList = []
        print ('[-] Could not list directory contents.')
        print ('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print ('[+] Found default page: ' + fileName)
            retList.append(fileName)
            
    return retList

def anonymousLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', '')
        print(ftp.getwelcome())
        ftp.set_pasv(1)
        #ftp.storbinary('STOR myfile.txt', open('file.txt', 'rb'))
        print(ftp.dir())        
        print ('\n[*] ' + str(hostname) +' FTP Anonymous Logon Succeeded.')
        return ftp
    except Exception as e:
        print (str(e))
        print ('\n[-] ' + str(hostname) +' FTP Anonymous Logon Failed.')
        return False

host = '192.168.1.233'
ftp = anonymousLogin(host)
ftpListDirectory(ftp)
