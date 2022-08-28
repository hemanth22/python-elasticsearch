from datetime import datetime
from elasticsearch import Elasticsearch
import json
import requests
es = Elasticsearch('http://localhost:9200',verify_certs=False)
resp = es.search(index="financial", query={ "match": { "address": "mill" } })
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    datainmp = hit["_source"]
    print("account number: " + str(datainmp['account_number']))
