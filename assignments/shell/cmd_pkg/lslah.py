

"""
    Name: lslah
    Description:
        long lists files and directories with hidden files and human readable file sizes
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
import stat
import time,subprocess,shutil
import math

def lslah(file,count,pipe):
		path=os.getcwd()
		files=[]
		files=os.listdir(path) 

		if pipe == 1:
			f1=open("pipe.txt",'w')
			f1.write(" File Name         Size       Permissions       Accessed Time                  Modified Time                        changed time")
			f1.write("-----------        -----      ------------      --------------                 --------------                       ------------")
			f1.write("\n")
			path=os.getcwd()
			result=[os.curdir, os.pardir]+os.listdir(path)
			for x in range(0,len(result)):
				s = str(oct(os.stat(result[x])[stat.ST_MODE])[-3:])				
				digits=[int(s[0]),int(s[1]),int(s[2])]
				lookup=['','x','w','wx','r','rx','rw','rwx']
				uout=lookup[digits[0]]
				gout=lookup[digits[1]]
				oout=lookup[digits[2]]
				mode=uout+'-'+gout+'-'+oout

				size=(os.stat(result[x]).st_size)
				filesize=size
				if size > 1024:
					size1=int(size/1024)

					size2= size -(size1*1024)

					size3 = float(size2/1024)
					size4=math.ceil(size3*100)/100
					size5= float(size1+size4)
					result1=(math.ceil(size5*100)/100)
					if size < 1048576 and size > 1024:
						filesize= str(result1)+"KB"
					elif size > 1048576 and size < 1073741824:
						filesize = str(result1)+"MB"
					elif size > 1073741824 and size < 1099511627776 :
						filesize = str(result1)+"GB"
						
				else:
					filesize=str(size)
					
				f1.write(result[x]+'\t\t  '+filesize+'\t\t'+str(mode)+'\t\t'+str(time.ctime(os.path.getmtime(result[x])))+'\t'+str(time.ctime(os.stat(result[x]).st_atime))+'\t'+str(time.ctime(os.stat(result[x]).st_ctime)))
				f1.write("\n")
			f1.close()
		else:	
			path=os.getcwd()
			result=[os.curdir, os.pardir]+os.listdir(path)
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
				
			for x in range(0,len(result)):
				s = str(oct(os.stat(result[x])[stat.ST_MODE])[-3:])				
				digits=[int(s[0]),int(s[1]),int(s[2])]
				lookup=['','x','w','wx','r','rx','rw','rwx']
				uout=lookup[digits[0]]
				gout=lookup[digits[1]]
				oout=lookup[digits[2]]
				mode=uout+'-'+gout+'-'+oout

				size=(os.stat(result[x]).st_size)
				filesize=size
				if size > 1024:
					size1=int(size/1024)

					size2= size -(size1*1024)

					size3 = float(size2/1024)
					size4=math.ceil(size3*100)/100
					size5= float(size1+size4)
					result1=(math.ceil(size5*100)/100)
					if size < 1048576 and size > 1024:
						filesize= str(result1)+"KB"
					elif size > 1048576 and size < 1073741824:
						filesize = str(result1)+"MB"
					elif size > 1073741824 and size < 1099511627776 :
						filesize = str(result1)+"GB"
						
				else:
					filesize=str(size)
					
				if file == None:
					print(str(mode)+"      "+str(filesize)+"          "+str(time.ctime(os.stat(result[x]).st_atime))+"            "+str(result[x]))
				else:
					f.write(result[x]+'\t\t  '+filesize+'\t\t'+str(mode)+'\t\t'+str(time.ctime(os.path.getmtime(result[x])))+'\t'+str(time.ctime(os.stat(result[x]).st_atime))+'\t'+str(time.ctime(os.stat(result[x]).st_ctime)))
					f.write("\n")
			
