# python Fix.py RASTcommand.sh OldList.txt ID password
import sys 

command = open(sys.argv[1])
old = open(sys.argv[2])
ID = sys.argv[3]
passWD = sys.argv[4]
listC=[]
flag=0
for line in command:
    tempcol = line.strip().split(" ")
    tempTax = tempcol[4].split("=")
    listC.append(tempTax[1])
#print listC
for line in old:
    flag =0
    tempCol = line.strip().split("\t")
    if (len(tempCol)<3):
        continue
    tempID = tempCol[2].split(".")
    for i in range(len(listC)):
        if (tempID[0] == listC[i]):
            flag=1
    if(flag==0):
        #print "~/sas/bin/svr_delete_RAST_job "+ID+" "+passWD+" "+tempCol[0]
        #print tempCol[2]
        print tempCol[0]
