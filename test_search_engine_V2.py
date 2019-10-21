import json
import deepcut

from elasticsearch import Elasticsearch
es = Elasticsearch()

def check(s_1,e_1,s_2,e_2,s_a,e_a,art1,art2,art_a):
    l1 = range(s_1,e_1+1)
    l2 = range(s_2,e_2+1)
    answer = range(s_a,e_a+1)

    print(art_a,":(",art1,"),(",art2,")")
    print(answer,":(",l1,"),(",l2,")")

    ck = set(answer)
    if(art_a ==  int(art1)):
        ck = ck-set(l1)
    if(art_a ==  int(art2)):
        ck = ck-set(l2)

    if ck:
        return False

    return True

my_file = open("qa-output100-2019.json",'r',encoding = 'utf-8-sig')
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
    print(data['article_id'],":",question)

    query = {
            "query": {
                    "query_string": {
                                    "query": question
                                    }
                      }
            }
    try:
        res2 = es.search(index="test_search_engine_v2",body=query)

        art_id1 =  res2['hits']['hits'][0]['_source']['art_id']
        paragraph1 =  res2['hits']['hits'][0]['_source']['paragraph']
        start_pos1 = res2['hits']['hits'][0]['_source']['start_pos']
        end_pos1 =  res2['hits']['hits'][0]['_source']['end_pos']

        art_id2 =  res2['hits']['hits'][1]['_source']['art_id']
        paragraph2 =  res2['hits']['hits'][1]['_source']['paragraph']
        start_pos2 = res2['hits']['hits'][1]['_source']['start_pos']
        end_pos2 =  res2['hits']['hits'][1]['_source']['end_pos']

        answer_s = data['answer_begin_position ']
        answer_e = data['answer_end_position']


        if(check(start_pos1,end_pos1,start_pos2,end_pos2,answer_s,answer_e,art_id1,art_id2,data['article_id'])):
            print("T")
            score = score+1
        else:
            print("F")
            false_list.append(data['article_id'])
    except:
        error_list.append(data['article_id'])
        print("Error : ",data['article_id'],">",question)
        error=error+1

print("SCORE:",score,"/",len(json_obj['data']))
print("ERROR:",error)
print("--------------Error LIST-------------------")
print(error_list)
print("--------------False LIST-------------------")
print(false_list)

