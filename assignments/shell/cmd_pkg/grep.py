
"""
    Name: grep
    Description:
        It displays file having keyword.
    Params: 
        keyword: searching for keyword
		file : searching keyword in file
		inputfile: redirects to inputfile if > exists
		count : if >> exists then it appends to inputfile
		pipe : checking whether commands contains piping
    Returns: None
""" 


import re

def grep(keyword,file,inputfile,count,pipe):

	try:
		if pipe == 1:
			f=open(file,'r')
			key=keyword[1:-1]
			list=[]
			for lines in f:
				if re.search(key, lines):
					list.append(lines)
			f.close()		
			f2=open("pipe.txt",'w')
			for lines in list:
				f2.write(lines)
					
			f2.close()		
					
		
		elif inputfile == None:
			f=open(file,'r')
			key=keyword[1:-1]
			print(key)
			for lines in f:
				if re.search(key, lines):
					print(lines)
			f.close()		
					
					
					
		else:
			f=open(file,'r')
			key=keyword[1:-1]
			if count == 0:
				f1=open(inputfile,'w')
			else:
				f1=open(inputfile,'a')
			for lines in f:
				if re.search(key, lines):
					f1.write(lines)
					
			f1.close()		
	except Exception as e:
		print("\n"+str(e))				
