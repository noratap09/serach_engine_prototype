import json

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("dict_id2txt_troken.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)

for i in json_obj.keys():
    doc = {
        'art_id': i,
        'text': json_obj[i]
        }

    res = es.index(index="test_search_engine_v1", doc_type='tweet',body=doc)
    #print(res['result'])

