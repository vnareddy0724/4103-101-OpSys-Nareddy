
"""
    Name: lsa
    Description:
        lists hidden files and directories
    Params: 
        file:if there is standard redirect output to file then filename is passed else None.
		count : checks whether output should append to file exists (>>)
		pipe : checking whether commands contains piping
    Returns: None
""" 


import os

def lsa(file,count,pipe):
	path=os.getcwd()
	result=[os.curdir, os.pardir]+os.listdir(path)
	
	if pipe == 1:
		f=open("pipe.txt",'w')
		for i in result:
			f.write(i+"\n")	
			
		f.close()	
	
	else:
		if count == 0 and file != None:
			f=open(file,'w')
		elif count == 1:
			f=open(file,'a')
		for i in result:
			if file == None:
				print(i)
			else:
				f.write(i+"\n")
		f.close()
