#coding: utf-8
#!/usr/local/bin/python

import sys
import pygeoip

gi4 = pygeoip.GeoIP('GeoIP.dat', pygeoip.MEMORY_CACHE)
ip = "5.135.4.5"
code = gi4.country_code_by_addr(ip)
name = gi4.country_name_by_addr(ip)

print (code + ' -- ' + name)

