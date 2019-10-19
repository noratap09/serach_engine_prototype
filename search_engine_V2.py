import json
import math

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("document/dict_id2txt_troken_up.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)

vocab_per_paragraph = 3700

for i in json_obj.keys():
    num = math.ceil(len(json_obj[i])/vocab_per_paragraph)
    pos_s = 0
    for j in range(0,num):
        print(i,":",j,"/",num)
        data = json_obj[i][j*vocab_per_paragraph:(j+1)*vocab_per_paragraph]
        pos_e = pos_s+len(''.join(data))
        #print(pos_s,":",pos_e)
        doc = {
            'art_id': i,
            'paragraph' : j,
            'text': data,
            'start_pos': pos_s,
            'end_pos': pos_e
            }

        res = es.index(index="test_search_engine_v2",id=str(i)+"_"+str(j), doc_type='tweet',body=doc)

        pos_s = pos_e+1
