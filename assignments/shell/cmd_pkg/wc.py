

"""
    Name: wc
    Description:
        Gives the total number of words in a file that is given as input.
    Params: 
        file(string) - Path of file for which number of words to be counted.
    Returns: None
"""
	
def wc(file):
		f=open(file,'r')
		wordcount=0
		for lines in f:
			f1=lines.split()
			wordcount=wordcount+len(f1)
		f.close()
		print ('Number of words : ', str(wordcount))
