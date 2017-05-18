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

## separate genbank file
RefSeq provide its genbank file as a big merged file. To upload genbank file into RAST, this big file need to be separated.
```
python separate_genbank_file.py input
```


## Download RefSoil RAST
in Excel, save as refsoil file into refsoil.txt (choose tab deliminated). then change return carrage
```
tr '\15' '\n' < refsoil.txt > refsoil.unix.txt
```
get rast id
```
python refsoil_to_rastid.py refsoil.unix.txt > refsoil.rast.id
```
then make list
```
python RASTdownloadCommad.py refsoil.rast.id ID password
```