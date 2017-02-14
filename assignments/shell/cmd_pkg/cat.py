
"""
    Name: cat
    Description:
        Dumps a file
    Params: 
        file (string) - The file to be dumped
    Returns: None
""" 

def cat(file):
		f=open(file,'r')
		print(f.read())
		f.close()
