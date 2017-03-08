
"""
    Name: head
    Description:
        displays first few lines of a file
    Params: 
        file (string) - The file to be displayed
		inputfile : redirects output to inputfile if > exists
		count : append output to inputfile if >> exists
		pipe:checks whether piping exists
    Returns: None
""" 



def head(file,inputfile,count,pipe):
	try:
		f=open(file,'r')
		linescount=0
		list=[]
		for lines in f:
				list.append(lines)
				linescount=linescount+1
				if linescount == 20:
					break
		
		if pipe == 1:
			f2=open("pipe.txt",'w')
			for i in list:
				f2.write(i)
			f2.close()		
					
					
		elif inputfile == None:
			for i in list:
				print(i)
				
					
		
					
		else:
			if count == 0:
				f1=open(inputfile,'w')
			else:
				f1=open(inputfile,'a')
			for i in list:
				f1.write(i)
				
					
			f1.close()		
					
		f.close()	
	except FileNotFoundError as e:
		print("\n"+str(e))	
