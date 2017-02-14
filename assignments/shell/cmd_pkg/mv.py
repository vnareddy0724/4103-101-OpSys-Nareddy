

"""
    Name: mv
    Description:
        It moves the source file and pastes in destination file.
    Params: 
        input_file(String) - Path of source file that to be moved.
        output_file (String) - Path of destination file where the source file gets pasted.
    Returns: None
""" 
import shutil
def mv(input_file,output_file):
		shutil.move(input_file,output_file)
