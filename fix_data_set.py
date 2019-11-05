import json

my_file = open("ThaiQACorpus2019-DevelopmentDataset.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)

for data in json_obj['data']:
    if(data['question_type']==1 and data['answer_begin_position'] == None):
        data['answer_begin_position'] = data['answer_end_position'] - len(data['answer'])
        print(data['answer_begin_position'])
        print(data['question_id'])

json_obj = json.dumps(json_obj,ensure_ascii=False)
target_file = open("data_set_fix.json","w",encoding = 'utf-8')
target_file.write(json_obj)
target_file.close()