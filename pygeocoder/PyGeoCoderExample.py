# -*- encoding: utf-8 -*-
'''
Notas:
Google Maps API V3 tiene una serie de limitaciones sobre su uso gratuito que pueden verse en detalle en el siguiente enlace: https://developers.google.com/maps/documentation/business/faq#usage_limits
'''
import pprint
from pygeocoder import Geocoder


results = Geocoder.geocode("Mountain View")
pprint.pprint(results.coordinates)
pprint.pprint(results.country)
pprint.pprint(results.postal_code)
print(results.latitude)
print(results.longitude)

results = Geocoder.reverse_geocode(results.latitude, results.longitude)
pprint.pprint(results.formatted_address)
