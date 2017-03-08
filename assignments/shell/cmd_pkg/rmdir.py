"""
    Name: rmdir
    Description:
        Removes the  directory which is passed as an argument.
    Params: 
        dir(string) - Path of directory to be removed that is given as argument.
    Returns: None
"""

import shutil
def rmdir(dir):
	try:
		shutil.rmtree(dir)
		print("Removed directory")
	except Exception as e:
		print("\n"+str(e))
