import deepcut
import json

my_file = open("dict_id2txt.json",'r',encoding = 'utf-8-sig')
txt = my_file.read()

json_obj = json.loads(txt)
list_keys = list(json_obj.keys())

for i in list_keys:
    print("TROKEN :",i)
    json_obj[i] = deepcut.tokenize(json_obj[i])

json_obj = json.dumps(json_obj,ensure_ascii=False)
target_file = open("dict_id2txt_troken.json","w",encoding = 'utf-8')
target_file.write(json_obj)
target_file.close()




