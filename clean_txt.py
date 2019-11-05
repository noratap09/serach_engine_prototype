import glob
import re
import json

path = glob.glob("raw_data/*.txt")
list_txt = list()
list_art_id = list()
for myfile in path:
    data = open(myfile,'r',encoding = 'utf-8-sig')
    txt = data.read()
    _ , art_id = myfile.split("\\")
    art_id = art_id[:-4]
    list_txt.append(txt)
    list_art_id.append(art_id)
    print("LOAD FILE:",myfile)

"""
    for i in range(0,len(list_txt)):
    pat_header = r'<doc id=".*" url=".*" title=".*">'
    pat_end = r"</doc>\n"
    list_txt[i] = re.sub(pat_header,"",list_txt[i])
    list_txt[i] = re.sub(pat_end,"",list_txt[i])
"""

dic_txt = dict(zip(list_art_id, list_txt))
json_obj = json.dumps(dic_txt,ensure_ascii=False)
target_file = open("dict_id2txt.json","w",encoding = 'utf-8')
target_file.write(json_obj)
target_file.close()