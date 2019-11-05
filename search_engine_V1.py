import json

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("document/dict_id2txt_troken_sun.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
count = 1
max_len = 0

for i in json_obj.keys():
    doc = {
        'art_id': i,
        'text': json_obj[i]
        }
    max_len = max(max_len,len(json_obj[i]))
    res = es.index(index="test_search_engine_v1",id=i,doc_type='tweet',body=doc)
    print(count,">",i,":",res['result']," MAX: ",max_len)
    count = count + 1

