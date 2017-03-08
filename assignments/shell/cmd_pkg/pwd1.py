
"""
    Name: pwd
    Description:
        Gives the current directory working in.
    Params: 
        
		file:if there is standard redirect output to file then filename is passed else None.
		count:checks whether standard redirect output or append is given
    Returns: None
"""
import os
def pwd1(file,count):

	if file == None:
		print(os.getcwd())
	else:
		if count == 0:
			f=open(file,'w')
		elif count == 1:
			f=open(file,'a')
			f.write("\n")
			f.write(os.getcwd())
			f.close()
