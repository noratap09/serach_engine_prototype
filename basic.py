from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'XXXX',
    'text': ['The', 'bird','red'],
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=4, body=doc)
print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

query = {
  "query": {
    "query_string": {
      "query": " fox red"
    }
  }
}

res2 = es.search(index="test-index",body=query)
print(res2)

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])