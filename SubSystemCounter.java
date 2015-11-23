import java.io.*;
import java.util.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

class SubSystemCounter {
    public static void main(String[] args) {
        
        
        //read file
        String fileName1 = args[0];
        
        Scanner fileScanner = null;
		try {
			fileScanner = new Scanner(new File(fileName1));
		} catch(FileNotFoundException e) {
			System.err.println("Could not find file '" + fileName1 + "'.");
			System.exit(1);
		}//try
		String line = null;
		HashMap <String,Integer> subMap = new HashMap <String,Integer> ();
		int num = 1;
		while(fileScanner.hasNext()) {
			line = fileScanner.nextLine();
			String[] entry = line.split("\t");
			//System.out.println(entry.length);
			if(entry.length<4){continue;}
			if (subMap.containsKey(entry[3])){
				int tempnum = subMap.get(entry[3]);
				tempnum ++;
				subMap.put(entry[3],tempnum);
			}else{
				subMap.put(entry[3],num);
			}
		}
		fileScanner.close();
		/*
		//System.out.println(datacogTable[3136]);
		
		//read info
		String cogTable [] = ReadCog();
		//System.out.println(cogTable[2272]);
		
		//read function map
		HashMap <String,Integer> FunMap = new HashMap <String,Integer> ();
		ReadFun(FunMap);
		
		HashMap <String,String> FunMapName = new HashMap <String,String> ();
		ReadFunName(FunMapName);
		//System.out.println(FunMap.get("H"));
		//int temp = FunMap.get("H");
		//temp ++;
		//FunMap.put("H",temp);
		//System.out.println(FunMap.get("H"));
		*/
		/*
		Set set = FunMap.entrySet();
      	Iterator iterator = set.iterator();
      	while(iterator.hasNext()) {
        	Map.Entry mentry = (Map.Entry)iterator.next();
        	System.out.print("key is: "+ mentry.getKey() + " & Value is: ");
        	System.out.println(mentry.getValue());
      	}
      	*/
      	/*
      	//count function
		int tempCog = 0;
		for (int i=0;i<5666;i++){
			if(cogTable[i] == ""){continue;}
			for (int j=0;j< cogTable[i].length();j++){
				tempCog = FunMap.get(cogTable[i].substring(j,j+1));
				tempCog += datacogTable[i];
				FunMap.put(cogTable[i].substring(j,j+1),tempCog);
			}
			
		}
		*/
		// print result
		Set set = subMap.entrySet();
      	Iterator iterator = set.iterator();
      	while(iterator.hasNext()) {
        	Map.Entry mentry = (Map.Entry)iterator.next();
        	System.out.print(mentry.getKey() + "\t");
        	System.out.println(mentry.getValue());
      	}
      	
		//count
		
        
    }
    

	
	
}
