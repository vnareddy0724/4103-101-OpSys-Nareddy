
"""
    Name: wc
    Description:
        Gives the total number of words in a file that is given as input.
    Params: 
        file(string) - Path of file for which number of words to be counted.
		inputfile : redirects output to inputfile if > exists
		count : append output to inputfile if >> exists
		pipe:checks whether piping exists
    Returns: None
"""
	
def wc(file,inputfile,count,pipe):
	try:
		f=open(file,'r')
		wordcount=0
		for lines in f:
			f1=lines.split()
			wordcount=wordcount+len(f1)
		f.close()

		if pipe == 1:
			f2=open("pipe.txt",'w')
			f2.write(str(wordcount))
				
		elif count == 0 and inputfile != None:
			f3=open(inputfile,'w')
			f3.write("Num of words "+str(wordcount))
		elif count == 1:
			f3=open(inputfile,'w')
			f3.write("Num of words "+str(wordcount))
				
		else:			
			
			print (str(wordcount))
			f=open(file,'r')
			count=len(f.readlines())
			print (str(count))
			print(file)
			
	except Exception as e:
		print("\n"+str(e))		
