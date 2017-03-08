"""
    Name: cp
    Description:
        Copies  source file to destination file.
    Params: 
        input_file(String) - Path of source file.
        output_file(String) - Path of destination file.
    Returns: None
""" 
import shutil

def cp(input_file,output_file):
	try:
		shutil.copy(input_file,output_file)
	except Exception as e:
		print("\n"+str(e))
