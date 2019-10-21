import json
import deepcut

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("ThaiQACorpus-DevelopmentDataset.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0
count = 1
error=0
error_list = list()
false_list = list()

for data in json_obj['data']:
    question = deepcut.tokenize(data['question'])
    question = " ".join(question)
    print(count,")",data['article_id'],":",question)

    query = {
            "query": {
                    "query_string": {
                                    "query": question
                                    }
                      }
            }

    try:
        res2 = es.search(index="test_search_engine_v1",body=query)
        art_id =  res2['hits']['hits'][0]['_source']['art_id']
        if(int(art_id) == data['article_id']):
            print("T")
            score = score+1
        else:
            print("F")
            false_list.append(data['article_id'])
    except:
        error_list.append(data['article_id'])
        print("Error : ",data['article_id'],">",question)
        error=error+1
    count = count+1

print("SCORE:",score,"/",len(json_obj['data']))
print("ERROR:",error)
print("--------------Error LIST-------------------")
print(error_list)
print("--------------False LIST-------------------")
print(false_list)