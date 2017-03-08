

"""
    Name: tail
    Description:
        Displays last few lines of file
    Params: 
        file (string) - The file to be displayed
		inputfile : redirects output to inputfile if > exists
		count : append output to inputfile if >> exists
		pipe:checks whether piping exists
    Returns: None
""" 

def tail(file,inputfile,count1,pipe):

	try:
		f=open(file,'r')
		count=len(f.readlines())
		count=count-10
		f=open(file,'r')
		listOfLines=[]
		for lines in f:
			listOfLines.append(lines)
		del listOfLines[0:count]
		
		if pipe == 1:
			f2=open("pipe.txt",'w')
			for i in listOfLines:
				f2.write(i)
				
			f2.close()	
		
		elif inputfile == None:
			for i in listOfLines:
				print(i)
				
			
				
		else:
			
			if count1 == 0:
				f1=open(inputfile,'w')
			else:
				f1=open(inputfile,'a')
				
			for i in listOfLines:
				f1.write(i+"\n")
				
			f1.close()	
		f.close()		
	except FileNotFoundError as e:
		print("\n"+str(e))	
