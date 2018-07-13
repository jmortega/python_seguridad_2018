import shodan
import argparse
import socket

SHODAN_API_KEY = "v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik"

api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Shodan search')
    
# Main arguments
parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
parser.add_argument("-search", dest="search", help="search", required=None)

parsed_args = parser.parse_args()

hostname = socket.gethostbyname(parsed_args.target)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search(parsed_args.search)

        # Show the results
        print ('Results sodan search: %s' % results['total'])
        for result in results['matches']:
                print ('IP: %s' % result['ip_str'])
                print (result['data'])
                print ('')
except shodan.APIError as e:
        print ('Error: %s' % e)
        
# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.count(parsed_args.search)
        
        # Show the results
        print ('Results sodan search: %s' % results['total'])
        for result in results['matches']:
                print ('IP: %s' % result['ip_str'])
                print (result['data'])
                print ('')
except shodan.APIError as e:
        print ('Error: %s' % e)       

# Lookup the host
host = api.host(hostname)
        
# Print general info
print ("""
                IP: %s
                Organization: %s
                Operating System: %s
        """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        
# Print all banners
for item in host['data']:
        print ("""Port: %s
        Banner: %s""" % (item['port'], item['data']))
