#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import re


class Shodan:
    """ Clase para buscar en Shodan """
    def __init__(self,API_KEY):
        self.api =  shodan.Shodan(API_KEY)    

    def buscar(self,cadena):
        """ Busca segun la cadena dada """
        try:
        # Buscamos lo de la cadena pasada como parametro
            resultado = self.api.search(str(cadena))
            return resultado
        except Exception as e:
            print ('Ups! Ha ocurrido un error: %s' % e)
            resultado = []
            return resultado

        
    def obtener_info_host(self,IP):
        """ Obtiene la info que pueda tener shodan sobre una IP """
        try:
                host = self.api.host(IP)
                return host
        except Exception as e:
                print ('Ups! Ha ocurrido un error: %s' % e)
                host = []
                return host     


def usage():
    print ("""Uso: ShodanSearch.py {OPTION} {CADENA | HOST}
     OPCIONES:
      -s, --search: Para buscar segun una determinada cadena
      -h, --host: Para obtener la informacion de un host segun su IP
     EJEMPLOS
      ShodanSearch.py -s apache
      ShodanSearch.py -h 8.8.8.8""")

def banner():
        print ("""
         ____  _               _             _____      
                / ___|| |__   ___   __| | __ _ _ __
                \___ \| '_ \ / _ \ / _` |/ _` | '_ \  
                 ___) | | | | (_) | (_| | (_| | | | |  
                |____/|_| |_|\___/ \__,_|\__,_|_| |_|
                                               Search
    """ )

def main():
    import sys
    import time

    API_KEY = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
    shodan = Shodan(API_KEY)
    if len(sys.argv) < 3:
        usage()
        sys.exit(2)
    else:
        if sys.argv[1] == '-s' or sys.argv[1] == '--search':
            banner()
            time.sleep(3)
            resultado = shodan.buscar(sys.argv[2])
            if len(resultado) != 0:
                    print ('Cantidad de resultados encontrados: %s' % resultado['total'])
                    for i in resultado['matches']:
                        print ('Ciudad: %s' % i.get('city','Unknown'))
                        print ('Pais: %s' % i.get('country_name','Unknown'))
                        print ('IP: %s' % i.get('ip_str'))
                        print ('O.S: %s' % i.get('os','Unknown'))
                        print ('Puerto: %s' % i.get('port'))
                        print ('Hostnames: %s' % i.get('hostnames'))
                        print ('Latitude: %s' % i.get('latitude','Unknown'))
                        print ('Longitude: %s' % i.get('longitude','Unknown'))
                        print ('Actualizado en: %s' % i.get('updated'))
                        print (i['data'])
                        print ('')
                    print (resultado.keys())
                    if 'organizations' in resultado.keys():
                        for key,value in resultado['organizations'].items():
                            print (key + ":" + value)
                    if 'countries' in resultado.keys():
                        for key,value in resultado['countries'].items():
                            print (key + ":" + value)
                    if 'cities' in resultado.keys():
                        for key,value in resultado['cities'].items():
                            print (key + ":" + value )                       
                        
        elif sys.argv[1] == '-h' or sys.argv[1] == '--host':
            banner()
            time.sleep(3)
            host = shodan.obtener_info_host(sys.argv[2])
            if len(host) != 0:
                print (host)
            # Imprimiendo la informacion obtenida
                if 'ip' in host.keys():
                        print ('IP: %s' % host.get('ip_str'))
                if 'country_name' in host.keys():
                        print ('Pais: %s' % host.get('country_name','Unknown'))
                if 'country_code' in host.keys():
                        print ('Codigo pais: %s' % host.get('country_code','Unknown'))
                if 'city' in host.keys():
                        print ('City: %s' % host.get('city','Unknown'))
                if 'latitude' in host.keys():
                        print ('Latitude: %s' % host.get('latitude'))
                if 'longitude' in host.keys():
                        print ('Longitude: %s' % host.get('longitude'))
                if 'hostnames' in host.keys():
                        print ('Hostnames: %s' % host.get('hostnames'))
                # Imprimimos los banners
                try:
                        for i in host['data']:
                            print ('Puerto: %s' % i['port'])
                            print ('Banner: %s' % i['banner'])
                            print ('')
                except Exception as e:
                    pass
        else:
                    usage()
                    sys.exit(2)

if __name__ == '__main__':
    main()
