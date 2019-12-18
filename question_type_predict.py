import json
keywords = ["ใช่หรือไม่","ไม่หรือใช่","จริงหรือไม่","ใช่หรือไม","ใช่ไหม","ใช่มั้ย","ใช่เปล่า","ใช่หรือเปล่า"]
my_file = open("ThaiQACorpus2019-DevelopmentDataset.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
score = 0
count = 1
false_list = list()

def question_type_predict(question_input):
    #เขียนfucntion แยกประเถทคำถาม
    
    if any(keyword in question_input.lower() for keyword in keywords):
            #print(y["question_id"] , " is in yes or no question type")
        return 2 
    else:
            #print(y["question_id"] ,"this question is full answer question")
        return 1
    #return 1 #return ได้แค่ 1,2

for data in json_obj['data']:
    question_type = question_type_predict(data['question'])
    if(question_type == data['question_type']):
        print("T")
        score = score+1
    else:
        print("F")
        false_list.append(data['question_id'])
    count = count+1

print("SCORE:",score,"/",count)
print("--------------False LIST-------------------")
print(false_list)