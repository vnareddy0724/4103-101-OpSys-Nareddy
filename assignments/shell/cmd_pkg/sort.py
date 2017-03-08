
"""
    Name: sort
    Description:
        sorts a file
    Params: 
        file (string) - The file to be sorted
		inputfile : redirects output to inputfile if > exists
		count : append output to inputfile if >> exists
		pipe:checks whether piping exists
    Returns: None
""" 


def sort(file,inputfile,count,pipe):
	try:	
		f=open(file,'r')
		listOfLines=[]
		for lines in f:
			listOfLines.append(lines)
		listOfLines.sort()
		
		if pipe == 1:
			f2=open("pipe.txt",'w')
			for i in listOfLines:
				f2.write(i+"\n")
				
			f2.close()	
		
		elif inputfile == None:
			for i in listOfLines:
				print(i)
				
				
				
		else:
			if count == 0:
				f1=open(inputfile,'w')
			else:
				f1=open(inputfile,'a')
			for i in listOfLines:
				f1.write(i+"\n")
				
			f1.close()
	except FileNotFoundError as e:
		print("\n"+str(e))		
