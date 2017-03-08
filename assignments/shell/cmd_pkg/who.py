
"""
    Name: who
    Description:
        displays the user .
    Params: 
        None
    Returns: None
""" 


import subprocess

def who():
	y=subprocess.check_output("who")
	print(y)

