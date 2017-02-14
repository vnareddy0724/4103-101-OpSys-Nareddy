

import threading
import time
import sys
import os
import shutil
from cat import cat
from cp import cp
from mv import mv
from pwd import pwd
from rm import rm
from wc import wc
from history import history
from rmdir import rmdir


"""
    ClassName: Driver
    Description:
        Runs all the shell commands which is given by the user.
""" 

class Driver(object):
	def __init__(self):
		pass
			
	if __name__ == '__main__':
		Commands={}
		var=input("%")
		var=var.split(" ")
		command0=var[0]
		history(*var)
		
		if command0 == 'cat':
			command1=var[1]
			c = threading.Thread(target=cat,args=(command1,))
			c.start()
			c.join()
		elif command0 == 'cp':
			command1=var[1]
			command2=var[2]
			c= threading.Thread(target=cp,args=(command1,command2,))
			c.start()
			c.join()
			print("copied successfully")
		elif command0 == 'mv':
			command1=var[1]
			command2=var[2]
			c=threading.Thread(target=mv,args=(command1,command2,))
			c.start()
			c.join()
			print("moved successfully")
		elif command0 == 'pwd':
			c=threading.Thread(target=pwd)
			c.start()
			c.join()
		elif command0 == 'rm':
			command1=var[1]
			c=threading.Thread(target=rm,args=(command1,))
			c.start()
			c.join()
		elif command0 == 'wc':
			command1=var[1]
			c=threading.Thread(target=wc,args=(command1,))
			c.start()
			c.join()
		
		elif command0 == 'rmdir':
			command1=var[1]
			c=threading.Thread(target=rmdir,args=(command1,))
			c.start()
			c.join()
		
		
