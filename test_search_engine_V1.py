import json
import deepcut

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("qa-output100-2019.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0

for data in json_obj['data']:
    question = deepcut.tokenize(data['question'])
    question = " ".join(question)
    print(data['article_id'],":",question)

    query = {
            "query": {
                    "query_string": {
                                    "query": question
                                    }
                      }
            }

    res2 = es.search(index="test_search_engine_v1",body=query)
    art_id =  res2['hits']['hits'][0]['_source']['art_id']
    if(int(art_id) == data['article_id']):
        print("T")
        score = score+1
    else:
        print("F")

print("SCORE:",score,"/",len(json_obj['data']))