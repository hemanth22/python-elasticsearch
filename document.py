from datetime import datetime
from elasticsearch import Elasticsearch
import json
import requests
es = Elasticsearch('http://localhost:9200',verify_certs=False)
resp = es.search(index="financial", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print(hit["_source"])