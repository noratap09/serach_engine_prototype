import glob
from shutil import copyfile

path = glob.glob("../ex_data/documents-nsc/documents-nsc/*.txt")
count = 0
for myfile in path:
    print(count,":",myfile)
    if(count%3==0):
        copyfile(myfile,"document/up/"+myfile.split("\\")[1])
    elif(count%3==1):
        copyfile(myfile,"document/sun/"+myfile.split("\\")[1])
    elif(count%3==2):
        copyfile(myfile,"document/pp/"+myfile.split("\\")[1])

    count = count+1