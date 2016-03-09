#!/usr/bin/python
# usage: python upload_from_list list path id pass
import sys
import genbank_get
path = sys.argv[2]
uid = sys.argv[3]
upass = sys.argv[4]
for x in open(sys.argv[1],'r'):    
    filename = path+'/'+x.strip()+'.gbk'
    taxid = genbank_get.taxon(filename)
    orga = genbank_get.organism(filename)
    final = "svr_submit_RAST_job --user='"+uid+"' --passwd="+upass+" --genbank="+filename+" --taxon_id="+taxid+" --bioname='"+orga+"'"
    print final
