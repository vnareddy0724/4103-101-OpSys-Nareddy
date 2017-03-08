"""
    Name: cat
    Description:
        Dumps a file
    Params: 
        file (string) - The file to be dumped
		inputfile : redirects output to inputfile if > exists
		count : append output to inputfile if >> exists
		pipe:checks whether piping exists
    Returns: None
""" 
import shutil

def cat(file,inputfile,count,pipe):
	try:
		f=open(file,'r')
		
		if pipe == 1:
			f2=open("pipe.txt",'w')
			for lines in f:
				f2.write(lines+"\n")	
		
		elif inputfile == None:
			
			print(f.read())
			f.close()
		
			
			
		else:
			if count == 0:
				shutil.copy(file,inputfile)
			else:
				f1=open(inputfile,'a')
				for lines in f:
					f1.write(lines+"\n")
					
	except Exception as e:
		print("\n"+str(e))					
