# -*- coding: UTF-8 -*-
 
import pygeoip
 
def main():
    geoip_country() 
    geoip_city()
    print ('done')
 
def geoip_city():
    path = 'GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    print (gic)
    print (gic.record_by_addr('64.233.161.99'))
    #{'city': 'Mountain View', 'region_name': 'CA', 'area_code': 650, 'longitude': -122.0574, 'country_code3': 'USA', 'latitude': 37.419199999999989, 'postal_code': '94043', 'dma_code': 807, 'country_code': 'US', 'country_name': 'United States'}
    print (gic.record_by_name('google.com'))
    #{'city': 'Mountain View', 'region_name': 'CA', 'area_code': 650, 'longitude': -122.0574, 'country_code3': 'USA', 'latitude': 37.419199999999989, 'postal_code': '94043', 'dma_code': 807, 'country_code': 'US', 'country_name': 'United States'}
    print (gic.region_by_name('google.com'))
    #{'region_name': 'CA', 'country_code': 'US'}
    print (gic.region_by_addr('64.233.161.99'))
    #{'region_name': 'CA', 'country_code': 'US'}
 
def geoip_country(): 
    path = 'GeoIP.dat'
    gi = pygeoip.GeoIP(path)
    #print gi.country_code_by_name('google.com')
    #'US'
    print (gi.country_code_by_addr('64.233.161.99'))
    #'US'
    #print gi.country_name_by_name('google.com')
    #'United States'
    print (gi.country_name_by_addr('64.233.161.99'))
    #'United States'
 
if __name__ == '__main__':
    main()
