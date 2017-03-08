

"""
    Name: lsl
    Description:
        long lists files and directories
    Params: 
        file:if there is standard redirect output to file then filename is passed else None.
		count : checks whether output should append to file exists (>>)
		pipe : checking whether commands contains piping
    Returns: None
""" 
import os
import threading
import glob
from pprint import pprint
from subprocess import check_output
from os import listdir
from os.path import isfile, join
import os.path
import sys
from stat import *
import stat
import time,subprocess,shutil
def lsl(file,count,pipe):
	path=os.getcwd()
	files=[]
	files=os.listdir(path)
	
	if pipe == 1:
		f=open("pipe.txt",'w')
		f.write(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
		f.write("-----------        -----      ------------      --------------                 --------------                       ------------")
		f.write("\n")
		for x in range(0,len(files)):
			s = str(oct(os.stat(files[x])[stat.ST_MODE])[-3:])				
			digits=[int(s[0]),int(s[1]),int(s[2])]
			lookup=['','x','w','wx','r','rx','rw','rwx']
			uout=lookup[digits[0]]
			gout=lookup[digits[1]]
			oout=lookup[digits[2]]
			mode=uout+'-'+gout+'-'+oout

			f.write(files[x]+'\t\t \t '+str(os.stat(files[x]).st_size)+'\t\t\t'+str(mode)+'\t\t\t'+str(time.ctime(os.path.getmtime(files[x])))+'\t'+str(time.ctime(os.stat(files[x]).st_atime))+'\t'+str(time.ctime(os.stat(files[x]).st_ctime)))
			f.write("\n")
			
			
	else:
	
		if count == 0 and file != None:
			f=open(file,'w')
		elif count == 1:
			f=open(file,'a')
		if file == None:
			#print(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
			print("-----------        -----      ------------      --------------                 --------------                       ------------")
		else:
			f.write(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
			f.write("-----------        -----      ------------      --------------                 --------------                       ------------")
			f.write("\n")
			
		for x in range(0,len(files)):
			if file == None:
				s = str(oct(os.stat(files[x])[stat.ST_MODE])[-3:])				
				digits=[int(s[0]),int(s[1]),int(s[2])]
				lookup=['','x','w','wx','r','rx','rw','rwx']
				uout=lookup[digits[0]]
				gout=lookup[digits[1]]
				oout=lookup[digits[2]]
				mode=uout+'-'+gout+'-'+oout
				print(mode+"       "+str(os.stat(files[x]).st_size)+"             "+str(time.ctime(os.stat(files[x]).st_atime))+"                 "+str(files[x])+"         ")
			else:
				f.write(files[x]+'\t\t \t '+str(os.stat(files[x]).st_size)+'\t\t\t'+str(mode)+'\t\t\t'+str(time.ctime(os.path.getmtime(files[x])))+'\t'+str(time.ctime(os.stat(files[x]).st_atime))+'\t'+str(time.ctime(os.stat(files[x]).st_ctime)))
				f.write("\n")
				
				
