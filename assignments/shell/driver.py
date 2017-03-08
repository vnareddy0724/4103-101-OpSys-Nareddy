
#!usr/bin/env python
import threading
import time
import sys
import os
import shutil
import re
from cat import cat
from cp import cp
from mv import mv
from rm import rm
from wc import wc
from who import who
from pwd1 import pwd1
from history import history
from rmdir import rmdir
from printHistory import printHistory
from head import head
from grep import grep
from concat import concat
from mkdir import mkdir
from sort import sort
from tail import tail
from ls import ls
from lsl import lsl
from lsa import lsa
from lsh import lsh
from chmod import chmod
from cd import cd
from cddot import cddot
from cdh import cdh
from lslh import lslh
from lsla import lsla
from lslah import lslah
from lsah import lsah
from less import less
"""
    ClassName: Driver
    Description:
        Runs all the shell commands which is given by the user.
""" 
	
	
class Driver(object):
	def __init__(self):
		pass

	
				
	"""
    Name: runShell
    Description:
        Runs the respective command which is passed as argument using thread instance .
    Params: 
        var1(string) - command is passed which is to be executed.
    Returns: None
"""					
	def runShell(var1,pipe):
			
			var=var1.split(" ") 
								#splits the command into list
			command0=var[0]			#stores command in a variable
			
			
			occurance=var.count('>') #checking whether command has redirect ouput
			count=var.count('>>')  #checking whether command has to append ouput
		  
			input=var.count('<') #checking whether command has redirect input
			
			#Checks whether & exists to set daemon status
			daemoncount=var.count('&')
			if daemoncount == 1:
				daemonstatus="true"
			else:
				daemonstatus="false"
				
			#checks whether loop matching the command given as input	
				
			#if command entered is cat , then cat method will be called using thread instance and also checks proper syntax
			
			if command0 == 'cat' and occurance==0 and count == 0:
			
				if len(var) == 1:
					print("Invalid command")
				else:	
					if input == 0:
						command1=var[1]
					else:
						command1=var[2]
					c = threading.Thread(target=cat,args=(command1,None,count,pipe,))
					#c.daemon=daemonstatus
					c.start()
					if daemonstatus == 'false':
						c.join()
						
			elif command0 == 'who':
				c=threading.Thread(target=who)
				c.start()
				c.join()	
			#if command entered is cp, calls cp method 		
							
			elif command0 == 'cp':
				if len(var) < 3 or var[1].count('.') == 0 :
					print("Invalid command")
				else:
					command1=var[1]
					command2=var[2]
					c= threading.Thread(target=cp,args=(command1,command2,))
					
					c.start()
					if daemonstatus == 'false':
						c.join()
										
			#if command entered is ls , calls ls method		
				
			elif command0 == 'ls' and occurance == 0 and count == 0:
				
				if len(var) == 1:
					l = threading.Thread(target=ls,args=(None,count,pipe,))
					
					l.start()
					if daemonstatus == 'false':
						l.join()
				else:
					command1=var[1]
					if command1 == '-l':  # calls ls -l
						l = threading.Thread(target=lsl,args=(None,count,pipe,))
						
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-a': #calls ls -a
						l = threading.Thread(target=lsa,args=(None,count,pipe,))
						
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-h':  #calls ls -h
						l = threading.Thread(target=lsh,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join() 
					elif command1 == '-lh' or command1 == '-hl':
						l=threading.Thread(target=lslh,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-la' or command1 == '-al':
						l=threading.Thread(target=lsla,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-lah':
						
						l=threading.Thread(target=lslah,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-ah' or command1 == '-ha':
							l=threading.Thread(target=lsah,args=(None,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()	

			#if command entered is cd, then calls cd method
			
			elif command0 == 'cd':
				command1=var[1]
				if command1 == '~':
					c=threading.Thread(target=cdh)
					c.start()
					if daemonstatus == 'false':
						c.join()
				elif command1 == '..':
					c=threading.Thread(target=cddot)
					c.start()
					if daemonstatus == 'false':
						c.join()	
					
				else:
					c=threading.Thread(target=cd,args=(command1,))
					c.start()
					if daemonstatus == 'false':
						c.join()
				
			#if command entered is chmod , then calls chmod method
			
			elif command0 == 'chmod':
				command1=var[1]
				command2=var[2]
				c=threading.Thread(target=chmod,args=(command1,command2,))
				c.start()
				if daemonstatus == 'false':
					c.join()
				
			#if command entered is mkdir , then calls mkdir method
			
			elif command0 == 'mkdir':
				if len(var) == 1:
					print("Invalid command")
				else:
					command1=var[1]
					c=threading.Thread(target=mkdir,args=(command1,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command entered is mv , then calls mv method		
				
			elif command0 == 'mv':
				if len(var) == 1 or var[1].count('.') == 0 :
					print("Invalid command")
				else:
					command1=var[1]
					command2=var[2]
					c=threading.Thread(target=mv,args=(command1,command2,))
					c.start()
					if daemonstatus == 'false':
						c.join()
										
			#if command entered is pwd,then calls pwd method
			
			elif command0 == 'pwd' and occurance == 0 and count ==0:
				c=threading.Thread(target=pwd1,args=(None,count,))
				c.start()
				if daemonstatus == 'false':
					c.join()
				
			#if command entered is rm , then calls rm method	
				
			elif command0 == 'rm':
				if len(var) == 1 :
					print("Invalid command")
				else:	
					command1=var[1]
					c=threading.Thread(target=rm,args=(command1,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command entered is wc , then calls wc method		
					
			elif command0 == 'wc' and occurance == 0 and count == 0:
				if len(var) == 1 :
					print("Invalid command")
				else:
					if input == 0:
						command1=var[1]
					else:
						command1=var[2]
					c=threading.Thread(target=wc,args=(command1,None,count,pipe,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command entered is rmdir , then calls rmdir method		
			
			elif command0 == 'rmdir':
			
				if len(var) == 1:
					print("Invalid command")
				else:	
					command1=var[1]
					c=threading.Thread(target=rmdir,args=(command1,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command represents concatination then concat method is called		
					
			elif command0 == 'cat' and len(var)==5 and occurance==1:
				if len(var) == 1 :
					print("Invalid command")
				else:
					command1=var[1]
					command2=var[2]
					command3=var[4]
					c=threading.Thread(target=concat,args=(command1,command2,command3,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command entered is grep then it calls grep method		
					
			elif command0 == 'grep' and occurance == 0 and count == 0:
				if len(var) < 3:
					print("Invalid command")
				else:	
					if input == 0:
						command1=var[1]
						command2=var[2]
					else:
						command1=var[1]

						command2=var[3]
					c=threading.Thread(target=grep,args=(command1,command2,None,count,pipe,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
			#if command represents sort the it calls sort method		
					
			elif command0 == 'sort' and occurance == 0 and count == 0 :
			
				if len(var) == 1:
xx					print("Invalid command")
				else:	
					if input == 0:
						command1=var[1]
					else:
						command1=var[2]
					c=threading.Thread(target=sort,args=(command1,None,count,pipe,))
					c.start()
					if daemonstatus == 'false':
						c.join()
					
				#if command is tail then calls tail method	
					
			elif command0 == 'tail' and occurance == 0 and count == 0 :
				if len(var) == 1:
					print("Invalid command")
				else:	
					if input == 0:
						command1=var[1]
					else:
						command1=var[2]
					c=threading.Thread(target=tail,args=(command1,None,count,pipe,))
					c.start()
					if daemonstatus == 'false':
						c.join()
				
			#command to display history , it calls history method	
					
			elif command0 == 'history' and occurance == 0 and count == 0 :
				c=threading.Thread(target=printHistory,args=(None,count,pipe,))
				c.start()
				if daemonstatus == 'false':
					c.join()
				
			#if command is head then calls head method	
				
			elif command0 == 'head' and occurance == 0 and count == 0 :	
			
				if len(var) == 1:
					print("Invalid command")
				else:				
					if input == 0:
						command1=var[1]
					else:
						command1=var[2]
					c=threading.Thread(target=head,args=(command1,None,count,pipe,))
					c.start()
					if daemonstatus == 'false':
						c.join()
			#if command is less then calls less method			
			elif command0 == 'less':
				c=threading.Thread(target=less,args=(var[1],pipe,))
				c.start()
				c.join()
					
			#Executes when standard redirect output / append command is given then calls respective command methods	
				
			elif occurance == 1 or count == 1:
				if command0 == 'cat':
					if len(var) < 4 or var[1].count('.') == 0 or var[3].count('.') == 0:
						print("Invalid command")
						
					else:	
						command1 = var[1]
						command2=var[3]
						c=threading.Thread(target=cat,args=(command1,command2,count,pipe,))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
				elif command0 == 'history':
					if len(var) < 3 or var[2].count('.') == 0:
						print("Invalid command")
					else:	
						command1=var[2]
						c=threading.Thread(target=printHistory,args=(command1,count,pipe))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
				elif command0 == 'grep':
					if len(var) < 5 or var[4].count('.') == 0 or var[2].count('.') == 0:
						print("Invalid command")
					else:	
						command1=var[1]
						command2=var[2]
						command3=var[4]
						c=threading.Thread(target=grep,args=(command1,command2,command3,count,pipe,))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
				elif command0 == 'sort':
					if len(var) < 4 or var[1].count('.') == 0 or var[3].count('.') == 0:
						print("Invalid command")
					else:	
						command1=var[1]
						command2=var[3]
						c=threading.Thread(target=sort,args=(command1,command2,count,pipe,))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
				elif command0 == 'tail':
				
					if len(var) < 4 or var[1].count('.') == 0 or var[3].count('.') == 0:
						print("Invalid command")
					else:	
						command1=var[1]
						command2=var[3]
						c=threading.Thread(target=tail,args=(command1,command2,count,pipe,))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
				elif command0 == 'head':
					if len(var) < 4 or var[1].count('.') == 0 or var[3].count('.') == 0:
						print("Invalid command")
					else:	
						command1=var[1]
						command2=var[3]
						c=threading.Thread(target=head,args=(command1,command2,count,pipe,))
						
						c.start()
						
						if daemonstatus == 'false':
							c.join()
						
				elif command0 == 'pwd':
					command1=var[2]
					c=threading.Thread(target=pwd,args=(command1,count,))
					
					c.start()
					if daemonstatus == 'false':
						c.join()
					
				elif command0 == 'wc':
					command1=var[1]
					command2=var[3]
					c=threading.Thread(target=wc,args=(command1,command2,count,pipe,))
					
					c.start()
					if daemonstatus == 'false':
						c.join()
					
						
				elif command0 == 'ls':
					if len(var) == 3:
						command1=var[2]
						c=threading.Thread(target=ls,args=(command1,count,pipe,))
						
						c.start()
						if daemonstatus == 'false':
							c.join()
					else:
						command1=var[1]
						command2=var[3]
						if command1 == '-l':  # calls ls -l
							l = threading.Thread(target=lsl,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-a': #calls ls -a
							l = threading.Thread(target=lsa,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-h':  #calls ls -h
							l = threading.Thread(target=lsh,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join() 
						elif command1 == '-lh' or command1 == 'hl':
							l=threading.Thread(target=lslh,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-la' or command1 == 'al':
							l=threading.Thread(target=lsla,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-lah':
							l=threading.Thread(target=lslah,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-ah' or command1 == '-ha':
							l=threading.Thread(target=lsah,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()
					
					
			
		#Exits from the shell 
				
	def exit():
		raise SystemExit
		
		
	if __name__ == '__main__':
	
	
		#Asks input for entering commands to user till exiting from shell

		
		
		while True:
			print("\n")
			var=raw_input("%")  # takes input from shell
			if len(var) == 0:
				continue
			var1=var.split(" ")
			history(*var1)#command entered by user will be stored in history file   
			

			pipe=0
			
			#if piping to be implemented
			
			if '|' in var:
				commands=var.split("|")
				pipe=1
				if len(commands) == 2:
					firstcommand=commands[0]
					firstcommand=firstcommand.strip()
					
					runShell(firstcommand,pipe)
					pipe=0
					redirect=commands[1].count('>')
					append=commands[1].count('>>')
					if redirect == 0 and append == 0:
						secondcommand=commands[1]+'\t'+"pipe.txt"
						secondcommand=secondcommand.lstrip()
						secondcommand=' '.join(secondcommand.split())
						
						runShell(secondcommand,pipe)
					elif redirect == 1 :
						commandlist=commands[1].split(">")
						
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						
						runShell(passedcommand,pipe)
					elif append == 1:
						commandlist=commands[1].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)	
						
					
				elif len(commands) == 3:
					runShell(commands[0],pipe)
					
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					pipe=0
					redirect=commands[2].count('>')
					append=commands[2].count('>>')
					if redirect == 0 and append == 0:
						thirdcommand=commands[2]+'\t'+"pipe.txt"
						thirdcommand=thirdcommand.lstrip();
						thirdcommand=' '.join(thirdcommand.split())
						
						runShell(thirdcommand,pipe)
					elif redirect == 1:
						commandlist=commands[2].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[2].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
				
				elif len(commands) == 4:
					runShell(commands[0],pipe)
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					thirdcommand=commands[2]+'\t'+"pipe.txt"
					thirdcommand=thirdcommand.lstrip();
					thirdcommand=' '.join(thirdcommand.split())
					runShell(thirdcommand,pipe)
					redirect=commands[3].count('>')
					append=commands[3].count('>>')
					pipe=0
					if redirect == 0 and append == 0:
						fourthcommand=commands[3]+'\t'+"pipe.txt"
						fourthcommand=fourthcommand.lstrip();
						fourthcommand=' '.join(fourthcommand.split())
						runShell(fourthcommand,pipe)
					elif redirect == 1:
						commandlist=commands[3].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[3].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)

				elif len(commands) == 5:
					runShell(commands[0],pipe)
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					thirdcommand=commands[2]+'\t'+"pipe.txt"
					thirdcommand=thirdcommand.lstrip();
					thirdcommand=' '.join(thirdcommand.split())
					runShell(thirdcommand,pipe)
					fourthcommand=commands[3]+'\t'+"pipe.txt"
					fourthcommand=fourthcommand.lstrip();
					fourthcommand=' '.join(fourthcommand.split())
					runShell(fourthcommand,pipe)
					
					
					redirect=commands[4].count('>')
					append=commands[4].count('>>')
					pipe=0
					if redirect == 0 and append == 0:
						fifthcommand=commands[4]+'\t'+"pipe.txt"
						fifthcommand=fifthcommand.lstrip();
						fifthcommand=' '.join(fifthcommand.split())
						runShell(fifthcommand,pipe)
					elif redirect == 1:
						commandlist=commands[4].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[4].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
						
						
						
			
			#if command to be executed from history then..
			
			elif var[0] == '!':
				f=open("history.txt",'r')
				num=int(var[1:])
				num=num-1
				for i, line in enumerate(f):
					if i == num:
						var=line
						number=str(num)
						length=len(number)
						var1=var[length:]
						var1=var1.lstrip()
						var2=' '.join(var1.split())
						runShell(var2,pipe)
							
							
							
			#if entered command is exit				
			
			
			elif str.lower(var) == 'exit':
				exit()
				
			#if any commands entered ,then passed to runShell method as parameter	
			else:
				runShell(var,pipe)
			
	
	
		
		
