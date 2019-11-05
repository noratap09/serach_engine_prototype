import json
import deepcut

from elasticsearch import Elasticsearch
es = Elasticsearch()

def check(s,e,art,s_a,e_a,art_a):
    answer = set(range(s_a,e_a+1))

    for i in range(0,len(art)):
        l = range(s[i],e[i]+1)
        #print(art[i],s[i],e[i])
        if(str(art_a) == art[i]):
            answer = answer-set(l)

    #print(answer,s_a,e_a,art_a)
    if answer:
        return False

    return True

my_file = open("data_set_fix.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0
count = 1
error=0
error_list = list()
false_list = list()
rank=2

for data in json_obj['data']:
    question = deepcut.tokenize(data['question'])
    question = " ".join(question)
    question = question.replace("/","")
    print(count,">",data['article_id'],":",question)

    query = {
            "query": {
                    "query_string": {
                                    "query": question
                                    }
                      }
            }
    try:
        res2 = es.search(index="test_search_engine_v2",body=query)

        art_id1 = list()
        paragraph1 = list()
        start_pos1 = list()
        end_pos1 = list()

        for i in range(0,rank):
            art_id1.append(res2['hits']['hits'][i]['_source']['art_id'])
            paragraph1.append(res2['hits']['hits'][i]['_source']['paragraph'])
            start_pos1.append(res2['hits']['hits'][i]['_source']['start_pos'])
            end_pos1.append(res2['hits']['hits'][i]['_source']['end_pos'])


        question_type = data['question_type']
        answer_s = data['answer_begin_position']
        answer_e = data['answer_end_position']

        if(question_type==1):
            if(check(start_pos1,end_pos1,art_id1,answer_s,answer_e,data['article_id'])):
                print("T")
                score = score+1
            else:
                print("F")
                false_list.append(data['question_id'])
        elif(question_type==2):
            res2 = es.search(index="test_search_engine_v2",body=query)
            resposn = list()
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
    count=count+1

print("SCORE:",score,"/",len(json_obj['data']))
print("ERROR:",error)
print("--------------Error LIST-------------------")
print(error_list)
print("--------------False LIST-------------------")
print(false_list)

