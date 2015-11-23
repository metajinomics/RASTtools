# RASTtools
RASTtools

## make upload command from genbank file
```
python GenbankToUploadCommand.py CP001220.gbk yourID Password
```
### for massive upload:
```
for x in *.gbk;do python GenbankToUploadCommand.py $x yourID Password;done
cat *.out > RASTupload.sh
cat RASTupload.sh | parallel
```

## Download
input file: job ID
```
python RASTdownloadCommad.py inpufile ID password
```

## Fix
```
python Fix.py RASTcommand.sh OldList.txt ID password
```

## subsystem counter
```
javac SubSystemCounter.java
java SubSystemCounter bindingfile
```