
"""
    Name: rm
    Description:
        Removes the file in the directory which is passed as an argument.
    Params: 
        file(string) - Path of file to be removed that is given as argument.
    Returns: None
""" 
import os	
def rm(file):
	try:
		os.remove(file)
		print("file removed successfully")
	except FileNotFoundError as e:
		print("\n"+str(e))	
