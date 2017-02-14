

"""
    Name: rm
    Description:
        Removes the file in the directory which is passed as an argument.
    Params: 
        file(string) - Path of file to be removed that is given as argument.
    Returns: None
""" 
	
def rm(file):
		os.remove(file)
		print("file removed successfully")
		
