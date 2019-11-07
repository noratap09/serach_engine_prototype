import json

my_file = open("ThaiQACorpus2019-DevelopmentDataset.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0
count = 1
false_list = list()

def question_type_predict(question_input):
    #เขียนfucntion แยกประเถทคำถาม
    return 1 #return ได้แค่ 1,2

for data in json_obj['data']:
    question_type = question_type_predict(data['question'])

    if(question_type == data['question_type']):
        print("T")
        score = score+1
    else:
        print("F")
        false_list.append(data['question_id'])
    count = count+1

print("SCORE:",score,"/",len(json_obj['data']))
#print("--------------False LIST-------------------")
#print(false_list)