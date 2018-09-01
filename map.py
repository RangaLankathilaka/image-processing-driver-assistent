import urllib3.request
import json
endpoint='https://maps.googleapis.com/maps/api/directions/json?'
api_key=' AIzaSyDXNqIb3EV7jCgsuRkdpn67YGgI1FHvN44 '
origin=input('where are you: ').replace(' ','+')
destination=input('where do you want to go?: ').replace('','+')
nav_request='origin=()&destination=() &key=()'.format(origin,destination,api_key)
request=endpoint+nav_request
response=urllib3.request.urlopen(request).read()
directions=json.load(response)
print (directions)