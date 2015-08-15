#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'

#Print table
resource = client.getResourceNetworking(id=resourceId, show='table')

#Get JSON Object
resource = client.getResourceNetworking(id=resourceId)

#Print networking values
for i in resource:
    print([i['key'], i['value']['value']])

#Use json.dumps() to get raw json
resourceRaw = json.dumps(resource)
print resourceRaw
