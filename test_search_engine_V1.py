import json
import deepcut

from elasticsearch import Elasticsearch
es = Elasticsearch()

my_file = open("ThaiQACorpus2019-DevelopmentDataset.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0
count = 1
error=0
error_list = list()
false_list = list()
rank=1
resposn = list()

for data in json_obj['data']:
    question = deepcut.tokenize(data['question'])
    question = " ".join(question)
    question = question.replace("/","")
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
        for i in range(0,rank):
            resposn.append(res2['hits']['hits'][i]['_source']['art_id'])
        if(str(data['article_id']) in resposn):
            print("T")
            score = score+1
        else:
            print("F")
            false_list.append(data['question_id'])
    except:
        error_list.append(data['question_id'])
        print("Error : ",data['question_id'],">",question)
        error=error+1
    count = count+1

print("SCORE:",score,"/",len(json_obj['data']))
print("ERROR:",error)
print("--------------Error LIST-------------------")
print(error_list)
print("--------------False LIST-------------------")
print(false_list)