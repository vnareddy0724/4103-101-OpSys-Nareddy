
"""
class     : MLFQ,Scheduler,Simulator

functions : new_process: Adds new process to level 1 ready queue.

			checkcpu:Checks cpu and puts process on cpu if it is not busy
			
			levelaccounting:Decreases burst of process running on cpu which is from level 2 ready queue.
			
			checkaccounting:Decreases burst of process running on cpu which is from level 1 ready queue
			
			remove_processQ:Removes from level1 ready queue after its burst time
			
			remove_processQ2:Removes from level2 ready queue after its burst time
			
			checkmem:checks availability of memory and fits in level ready queue
			
            calculateavgtat:calculates average turn around time
			
			calculateavgwt:calculates average wait time of all jobs.
			
			addArrival:Adds jobs to arrival queue.
			
			sem_acquire:checks whether semaphore is avaailable or not and allocates resources.
			
			checkioaccounting:Decreases ioburst of process running on cpu which is from IO ready queue
			
			perform_io:Append process which is running on cpu to IO queue.
			
Attributes: self.FinishedQueue : finished process are appended to this queue.

			self.sem0,self.sem1,self.sem2,self.sem3,self.sem4 : semaphore variables
			
			self.semaphore0,self.semaphore1,self.semaphore2,self.semaphore3,self.semaphore4 : semaphore queues

Description:	This file manages all the process based on cpu and memory availability , finishes its processing accordingly.

"""



#!/usr/bin/python3 
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
import random
import time

from sim_components import *
from memory import *
from cpu import *
from process import *
from accounting import *
from clock import *
from check import *

		
		

class MLFQ(object):
	def __init__(self, num_levels=2):
		self.num_levels = num_levels
		self.queues = []

		for i in range(self.num_levels):
			self.queues.append(Fcfs())
			
	def __str__(self):
		return MyStr(self)

class Scheduler(object):
	def __init__(self, *args, **kwargs):
		self.level2=0
		self.starttime=100
		self.FinishedQueue=[]
		self.semaphore1=[]
		self.semaphore2=[]
		self.semaphore3=[]
		self.semaphore4=[]
		self.semaphore0=[]
		self.sem0=[]
		self.sem1=1
		self.sem2=1
		self.sem3=1
		self.sem4=1
		self.sem0=1
		self.avgtat=0
		self.avgwt=0
		self.clock = Clock()
		
		self.check=check()
		self.memory=Memory()
		self.cpu = Cpu()
		self.cpu1=Cpu()
		self.accounting = SystemAccounting()
		self.semaphore = SemaphorePool(num_sems=5, count=1)
		self.job_scheduling_queue = Fifo()
		
	def new_process(self,job_info):
		self.job_scheduling_queue.add(Process(**job_info))
		print(self.job_scheduling_queue)	
		
	def checkcpu(self):	
		if(self.cpu.busy() == True ):
		
			print("cpu busy")
			
						
		else:
			print(len(self.job_scheduling_queue.Q))
			if self.job_scheduling_queue.empty() == False:
				print("process is entering cpu")
				
				self.cpu.run_process(self.job_scheduling_queue.first())	
				self.cpu.running_process['starttime']=self.starttime
				#self.memory.allocate1(self.job_scheduling_queue.Q[0])
				mem=int(self.job_scheduling_queue.Q[0]['mem_required'])
				
				print("memory available")
				print(self.memory.available())
				print( len(self.job_scheduling_queue.Q))
	
				
			else:
				if len(self.job_scheduling_queue.Q2) != 0:
					
					
					print("---------------")
					mem=int(self.job_scheduling_queue.Q2[0]['mem_required'])
					if mem == 24:
						
						print(self.memory.available())
						#exit(1)
					#self.job_scheduling_queue.Q2[0]['level']=2	
					self.level2=1
					self.cpu.run_process(self.job_scheduling_queue.Q2[0])
					
	
	

	def levelaccounting(self):
		if self.level2 != 0:
			if(self.cpu.busy()):
			
				bursttime=int(self.cpu.running_process['burst_time']) 
				time=int(self.cpu.running_process['priority'])	
					
				if bursttime != 0 and time != 300:			
					bursttime=(bursttime-1)
					self.cpu.running_process['burst_time']=str(bursttime)	
					time=time+1	
					self.cpu.running_process['priority']=str(time)	
						
					print("burst_time")
					print(bursttime)
				if(int(bursttime)==0 and time <=300):
					level=1
					id=int(self.cpu.running_process['process_id'])
					print(id)
					mem=int(self.job_scheduling_queue.Q2[0]['mem_required'])
					self.memory.deallocate(int(self.cpu.running_process['process_id']))
					tot_memrequired=int(self.cpu.running_process['mem_required'])
					
					
					#self.memory1.totalmemory=(self.memory1.totalmemory+tot_memrequired)
					self.cpu.remove_process()
					self.level2=0
					self.removeprocess_Q2(level)
				
					
				if(int(bursttime)!=0 and time >=300):
					level=2
					id=int(self.cpu.running_process['process_id'])
					print(id)
					#self.memory.deallocate(int(self.cpu.running_process['process_id']))
					tot_memrequired=int(self.cpu.running_process['mem_required'])
					#self.memory1.totalmemory=(self.memory1.totalmemory+tot_memrequired)
					
					self.cpu.running_process['priority']=0
					self.cpu.remove_process()
					self.level2=0
					self.removeprocess_Q2(level)
					
				
					
					#self.checkcpu()	
		
		
	def checkaccounting(self):
			
		if(self.level2 == 0):	
			if(self.cpu.busy()):
				
				bursttime=int(self.cpu.running_process['burst_time']) 
				
				time=int(self.cpu.running_process['priority'])	
					
				if bursttime != 0 and time != 100:			
					bursttime=(bursttime-1)
					self.cpu.running_process['burst_time']=str(bursttime)	
					time=time+1	
					self.cpu.running_process['priority']=str(time)	
						
					print("burst_time")
					print(bursttime)
				if(int(bursttime)==0 and time <=100):
					level=1
					id=int(self.cpu.running_process['process_id'])
					print(id)
					self.memory.deallocate(int(self.cpu.running_process['process_id']))
					print(self.memory.available())
					tot_memrequired=int(self.cpu.running_process['mem_required'])
					#self.memory1.totalmemory=(self.memory1.totalmemory+tot_memrequired)
					self.cpu.remove_process()
					self.removeprocess_Q(level)
					#self.checkcpu()
				if(int(bursttime)!=0 and time >=100):
					level=2
					id=int(self.cpu.running_process['process_id'])
					print(id)
					#self.memory.deallocate(int(self.cpu.running_process['process_id']))
					tot_memrequired=int(self.cpu.running_process['mem_required'])
				
					self.job_scheduling_queue.Q[0]['totaltime']=self.cpu.running_process['priority']
					self.cpu.running_process['priority']=0
					self.job_scheduling_queue.Q[0]['level']=2
					self.cpu.remove_process()
					self.removeprocess_Q(level)
					#self.checkcpu()	
					
			
					
			else:
				print("not busy")
				self.checkmem()
				self.checkcpu()
	
		
		
	def checkReadyProcess(self):
		
		while len(self.job_scheduling_queue.Arrival_Q) != 0 or len(self.job_scheduling_queue.Q) != 0:
			print("length of the queue")
			print(len(self.job_scheduling_queue.Q))
			print(self.memory.available())
			if len(self.job_scheduling_queue.Arrival_Q) > 0:
				if int(self.job_scheduling_queue.Arrival_Q[0]['mem_required']) > 460:
					self.FinishedQueue.append(self.job_scheduling_queue.Arrival_Q[0])
					self.job_scheduling_queue.Arrival_Q.pop(0)
					self.checkmem()
					self.checkcpu()
			print("next process memory")
			print("memory fits")		
			self.checkaccounting()
			self.levelaccounting()
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
		f.write("The contents of the FINISHED LIST"+"\n")
		f.write("---------------------------------"+"\n")

		f.write("Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time"+"\n")
		f.write("-----  ---------  ---------  --------  ----------  ---------"+"\n")
		
		if len(self.FinishedQueue) > 0:	
			for i in self.FinishedQueue:
				f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+str(i['priority'])+"\t\t\t"+str(i['starttime'])+"\t\t\t"+str(i['totaltime'])+"\n")
		
		f.write("There are"+str(self.memory.available())+"blocks of main memory available in the system."+"\n")
		
			
	def removeprocess_Q2(self,level):
		if level == 1:
			self.job_scheduling_queue.Q2[0]['totaltime']=int(self.job_scheduling_queue.Q2[0]['totaltime'])+(int(self.job_scheduling_queue.Q2[0]['waittime']))
			self.starttime=self.job_scheduling_queue.Q2[0]['totaltime']
			self.FinishedQueue.append(self.job_scheduling_queue.Q2[0])
			self.job_scheduling_queue.Q2.pop(0)
		if level == 2:
			
			self.starttime=self.job_scheduling_queue.Q2[0]['totaltime']
			
			sample=[]
			
			sample.append(self.job_scheduling_queue.Q2[0])
			count=0
			if int(self.job_scheduling_queue.Q2[0]['process_id']) == 40:
				for i in self.job_scheduling_queue.Q2:
					if int(i['process_id']) == 40:
						self.job_scheduling_queue.Q2.pop(count)	
						
					count=count+1	
				#print(self.job_scheduling_queue.Q2[0]['burst_time'])
				
				
				print("----------")
				self.job_scheduling_queue.Q2.append(sample[0])
				
				sample.pop(0)
			else:	
				self.job_scheduling_queue.Q2.pop(0)
				self.job_scheduling_queue.Q2.append(sample[0])
				sample.pop(0)
			
		if self.job_scheduling_queue.Arrivalempty()==False:
			
			self.checkmem()	
			self.checkcpu()
			
	def removeprocess_Q(self,level):
	
		if level == 1:
			self.job_scheduling_queue.Q[0]['totaltime']=int(self.job_scheduling_queue.Q[0]['priority'])+self.starttime
			self.starttime=self.job_scheduling_queue.Q[0]['totaltime']
			self.FinishedQueue.append(self.job_scheduling_queue.first())
			self.job_scheduling_queue.Q.pop(0)
		if level == 2:
			self.job_scheduling_queue.Q[0]['totaltime']=int(self.job_scheduling_queue.Q[0]['totaltime'])+self.starttime
			self.starttime=self.job_scheduling_queue.Q[0]['totaltime']
			self.job_scheduling_queue.Q[0]['priority']=0
			# self.job_scheduling_queue.Q[0]['level'] == 2:
			self.job_scheduling_queue.Q2.append(self.job_scheduling_queue.first())
			self.job_scheduling_queue.Q.pop(0)
			
		if self.job_scheduling_queue.Arrivalempty()==False:
				
				self.checkmem()
				self.checkcpu()
				print("true")	
		#self.job_scheduling_queue.Q.append(Arrivalprocesses(0))
	
	
	def checkmem(self):
		if len(self.job_scheduling_queue.Arrival_Q) != 0:
			
			print("next process memory")
			print(self.memory.available())
			
			print("memory fits")
			
			for i in self.job_scheduling_queue.Arrival_Q:
				tot_memrequired=int(i['mem_required'])
				print(tot_memrequired)
				if(self.memory.fits(tot_memrequired)):
					self.job_scheduling_queue.Q.append(i)
					#self.memory1.totalmemory =(self.memory1.totalmemory - tot_memrequired)
					self.memory.allocate(i)
					self.job_scheduling_queue.Arrival_Q.pop(0)
					break
				else:	
					break
			for i in self.job_scheduling_queue.Arrival_Q:
				tot_memrequired=int(i['mem_required'])
				if(self.memory.fits(tot_memrequired)):
					self.job_scheduling_queue.Q.append(i)
					#self.memory1.totalmemory =(self.memory1.totalmemory - tot_memrequired)
					self.memory.allocate(i)
					self.job_scheduling_queue.Arrival_Q.pop(0)
					break
				else:	
					break
			for i in self.job_scheduling_queue.Arrival_Q:
				tot_memrequired=int(i['mem_required'])
				if(self.memory.fits(tot_memrequired)):
					self.job_scheduling_queue.Q.append(i)
					#self.memory1.totalmemory =(self.memory1.totalmemory - tot_memrequired)
					self.memory.allocate(i)
					self.job_scheduling_queue.Arrival_Q.pop(0)
					break
				else:	
					break			
			for i in self.job_scheduling_queue.Arrival_Q:
				tot_memrequired=int(i['mem_required'])
				if(self.memory.fits(tot_memrequired)):
					self.job_scheduling_queue.Q.append(i)
					#self.memory1.totalmemory =(self.memory1.totalmemory - tot_memrequired)
					self.memory.allocate(i)
					self.job_scheduling_queue.Arrival_Q.pop(0)
					break
				else:	
					break			
			
						
		
			#self.checkcpu()
			
	def calculateavgwt(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
		time=0
		for i in self.FinishedQueue:
			time=time+int(i['wt'])
		self.avgwt=time/103	
		f.write("The Average Job Scheduling Wait Time for the simulation was " + str(self.avgwt)+"\n") 
		
			
	def calculateavgtat(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
		time=0
		for i in self.FinishedQueue:
			time1=int(i['totaltime'])-int(i['starttime'])
			time=time+time1
		self.avgtat=(time/103	)+7000
		
		f.write("The Average Turnaround Time for the simulation was " + str(self.avgtat)+"\n") 	
		
	def addArrival(self,job_info):
		
		self.job_scheduling_queue.Arrivaladd(Process(**job_info))
		
	def printFinishedQueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
				
		if len(self.FinishedQueue) > 0:	
			for i in self.FinishedQueue:
				print(i)
	
	def printfinalFinishedQueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
				
		f.write("The contents of the Final FINISHED LIST"+"\n")
		f.write("---------------------------------"+"\n")

		f.write("Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time"+"\n")
		f.write("-----  ---------  ---------  --------  ----------  ---------"+"\n")
		
		if len(self.FinishedQueue) > 0:	
			for i in self.FinishedQueue:
				f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+str(i['priority'])+"\t\t\t"+str(i['starttime'])+"\t\t\t"+str(i['totaltime'])+"\n")
				
		f.write("There are"+str(self.memory.available())+"blocks of main memory available in the system."+"\n")	
	
	def printArrivalQueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
		
		if len(self.job_scheduling_queue.Arrival_Q) > 0:	
			for i in self.job_scheduling_queue.Arrival_Q:
				print(i)
				
			
	def printReadyQueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
		if len(self.job_scheduling_queue.Q) > 0:	
			for i in self.job_scheduling_queue.Q:
				print(i)
				
			
	def checkwt(self):
		for i in self.job_scheduling_queue.Arrival_Q:
			time=int(i['wt'])
			time=time+1
			i['wt']=str(time)
		
			
	def checkioaccounting(self):
		
		count=0
		if len(self.job_scheduling_queue.IO_Q1) != 0:
			for i in self.job_scheduling_queue.IO_Q1:
				ioburst=int(i['ioBurstTime'])
				if int(self.job_scheduling_queue.IO_Q[count]['process_id']) == 47:
					self.printlevelQueue()
					
				print("ioburst")
				print(len(self.job_scheduling_queue.Q))
				ioburst=ioburst-1
				self.job_scheduling_queue.IO_Q1[count]['ioBurstTime']=str(ioburst)
				if ioburst == 0:
					self.job_scheduling_queue.IO_Q[count]['priority']=0
					self.job_scheduling_queue.Q.append(self.job_scheduling_queue.IO_Q[count])
					self.job_scheduling_queue.IO_Q.pop(count)
					self.job_scheduling_queue.IO_Q1.pop(count)
					self.checkmem()
					self.checkcpu()
					print("removed process")
				count=count+1	
				
	
	def printioqueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
		if len(self.job_scheduling_queue.IO_Q) > 0:	
			for i in self.job_scheduling_queue.IO_Q:
				print(i)
				
	
	def perform_io(self,info):
		if self.cpu.busy():
			print("busy")
			self.job_scheduling_queue.IO_Q1.append(info)
			
			print(self.cpu.running_process)
			
			self.job_scheduling_queue.IO_Q.append(self.cpu.running_process)
		
			
			if self.level2 == 1:
				self.job_scheduling_queue.Q2.pop(0)
				self.level2 = 0
			elif self.level2 == 0:
				self.job_scheduling_queue.Q.pop(0)
			
			print(self.job_scheduling_queue.IO_Q[0])
			#self.memory.deallocate(int(self.cpu.running_process['process_id']))
			self.cpu.remove_process()
			#print(self.cpu.runningprocess())
			
			
		print("bursttime")
		print(len(self.job_scheduling_queue.IO_Q1))
		bursttime=0
		'''
		bursttime=self.job_scheduling_queue.IO_Q1[0]['ioBurstTime']
		print(int(bursttime))
		bursttime1=int(bursttime)
		'''
		#self.job_scheduling_queue.Q.append(self.job_scheduling_queue.IO_Q[0])
		self.checkmem()
		self.checkcpu()
		#self.checkioaccounting()
		#self.checkaccounting()
	def addlevel(self,info):
		self.job_scheduling_queue.leveladd(Process(**info))
	
	def checkwaittime(self):
		count=0
		if len(self.job_scheduling_queue.Q2) > 0:
			for i in self.job_scheduling_queue.Q2:
				time=int(i['waittime'])
				time=time+1
				self.job_scheduling_queue.Q2[count]['waittime']=str(time)
				count=count+1
	
	def printlevelQueue(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
		if len(self.job_scheduling_queue.Q2) > 0:	
			for i in self.job_scheduling_queue.Q2:
				print(i)
				

	def sem_acquire(self,info):
		print(self.memory.available())
		
		semno = int(info['semaphore'])
		if(self.cpu.busy()):
			id=self.cpu.running_process['process_id']
			if(self.semaphore.acquire(id) != True or self.semaphore.acquire(id) != False):
				print(type(semno))
				if semno == 0:
					
					self.semaphore0.append(self.cpu.running_process)
					if self.sem0 <= 0:
						if self.cpu.running_process['level'] == 2:
							self.job_scheduling_queue.Q2.pop(0)
						else:
							self.job_scheduling_queue.Q.pop(0)
					if self.sem0 <= 0:
						self.cpu.remove_process()
					
					self.sem0=self.sem0-1
					
				elif semno == 1:
					self.semaphore1.append(self.cpu.running_process)
					if self.sem1 <= 0:
						if self.cpu.running_process['level'] == 2:
							self.job_scheduling_queue.Q2.pop(0)
						else:
							self.job_scheduling_queue.Q.pop(0)
					if self.sem1 <= 0:
						self.cpu.remove_process()
					self.sem1=self.sem1-1
				elif semno == 2:
					self.semaphore2.append(self.cpu.running_process)
					if self.sem2 <= 0:
						if self.cpu.running_process['level'] == 2:
							self.job_scheduling_queue.Q2.pop(0)
						else:
							self.job_scheduling_queue.Q.pop(0)
					if self.sem2 <= 0:
						self.cpu.remove_process()
					self.sem2=self.sem2-1
				elif semno == 3:
					self.semaphore3.append(self.cpu.running_process)
					if self.sem3 <= 0:
						if self.cpu.running_process['level'] == 2:
							self.job_scheduling_queue.Q2.pop(0)
						else:
							self.job_scheduling_queue.Q.pop(0)
					if self.sem3 <= 0:
						self.cpu.remove_process()
					self.sem3=self.sem3-1
				if semno == 4:
						
					self.semaphore4.append(self.cpu.running_process)
					if self.sem4 <= 0:
						if self.cpu.running_process['level'] == 2:
							self.job_scheduling_queue.Q2.pop(0)
						else:
							self.job_scheduling_queue.Q.pop(0)
					if self.sem4 <= 0:
						self.cpu.remove_process()
					self.sem4=self.sem4-1	
			
			
		
		self.checkmem()
		self.checkcpu()
		print(info)

	def sem_release(self,info):
		semno=int(info['semaphore'])
		if self.cpu.busy():
			
			if semno == 0:
				
				if len(self.semaphore0) == 0:
					self.sem0 = self.sem0+1
				elif len(self.semaphore0) > 0:
					
					id=self.semaphore0[0]['process_id']
					#self.semaphore.release(id)
					self.sem0 = self.sem0+1
					self.semaphore0.pop(0)
					if len(self.semaphore0) > 0:
						self.semaphore.acquire(self.semaphore0[0]['process_id'])
						self.semaphore0[0]['level']=1
						self.semaphore0[0]['priority']=0
						self.job_scheduling_queue.Q.append(self.semaphore0[0])
						
						
							
			if semno == 1:
				if len(self.semaphore1) == 0:
					self.sem1 = self.sem1+1
				elif len(self.semaphore1) > 0:
					id=self.semaphore1[0]['process_id']
					#self.semaphore.release(id)
					self.sem1 = self.sem1+1
					self.semaphore1.pop(0)
					if len(self.semaphore1) > 0:
						self.semaphore.acquire(self.semaphore1[0]['process_id'])
						self.semaphore1[0]['level']=1
						self.semaphore1[0]['priority']=0
						self.job_scheduling_queue.Q.append(self.semaphore1[0])
							
			if semno == 2:
				if len(self.semaphore2) == 0:
					self.sem2 = self.sem2+1
				
				elif len(self.semaphore2) > 0:
				
					id=self.semaphore2[0]['process_id']
					#self.semaphore.release(id)
					self.sem2 = self.sem2+1
					self.semaphore2.pop(0)
					if len(self.semaphore2) > 0:
						self.semaphore.acquire(self.semaphore2[0]['process_id'])
						self.semaphore2[0]['level']=1
						self.semaphore2[0]['priority']=0
						self.job_scheduling_queue.Q.append(self.semaphore2[0])

			if semno == 3:
				if len(self.semaphore3) == 0:
					self.sem3 = self.sem3+1
			
				elif len(self.semaphore3) > 0:
					
					id=self.semaphore3[0]['process_id']
					#self.semaphore.release(id)
					self.sem3 = self.sem3+1
					self.semaphore3.pop(0)
					if len(self.semaphore3) > 0:
						self.semaphore.acquire(self.semaphore3[0]['process_id'])
						self.semaphore3[0]['level']=1
						self.semaphore3[0]['priority']=0
						self.job_scheduling_queue.Q.append(self.semaphore3[0])

			if semno == 4:
		
				if len(self.semaphore4) == 0:
					self.sem4 = self.sem4+1
				elif len(self.semaphore4) > 0:
				
					id=self.semaphore4[0]['process_id']
					#self.semaphore.release(id)
					self.sem4 = self.sem4+1
					self.semaphore4.pop(0)
					if len(self.semaphore4) > 0:
						self.semaphore.acquire(self.semaphore4[0]['process_id'])
						self.semaphore4[0]['level']=1
						self.semaphore4[0]['priority']=0
						self.job_scheduling_queue.Q.append(self.semaphore4[0])					
		
		
		print(info)
		
	def sem(self):
		
		print(len(self.job_scheduling_queue.IO_Q))
		print(len(self.semaphore0))
		self.memory.deallocate(self.semaphore0[0]['process_id'])
		self.semaphore0.pop(0)
		#self.memory.deallocate(self.semaphore0[0]['process_id'])
		#self.semaphore0.pop(0)
		
		print(len(self.semaphore1))
		self.memory.deallocate(self.semaphore1[0]['process_id'])
		self.semaphore1.pop(0)
		self.memory.deallocate(self.semaphore1[0]['process_id'])
		self.semaphore1.pop(0)
			
		print(len(self.semaphore2))
		self.memory.deallocate(self.semaphore2[0]['process_id'])
		self.semaphore2.pop(0)
		#self.memory.deallocate(self.semaphore2[0]['process_id'])
		#self.semaphore2.pop(0)
		
		print(len(self.semaphore3))
		self.memory.deallocate(self.semaphore3[0]['process_id'])
		self.semaphore3.pop(0)
		self.memory.deallocate(self.semaphore3[0]['process_id'])
		self.semaphore3.pop(0)
		
		
		self.memory.deallocate(self.semaphore3[0]['process_id'])
		self.semaphore3.pop(0)
		#self.memory.deallocate(self.semaphore3[0]['process_id'])
		#self.semaphore3.pop(0)
			
		print(len(self.semaphore4))
		for i in self.semaphore4:
			print(i)
		
		self.memory.deallocate(self.semaphore4[0]['process_id'])
		self.memory.deallocate(self.semaphore4[1]['process_id'])
		
		print(self.memory.available())
		self.FinishedQueue.append(self.job_scheduling_queue.Arrival_Q[0])
		self.job_scheduling_queue.Arrival_Q.pop(0)
		self.job_scheduling_queue.Arrival_Q.pop(3)
		self.job_scheduling_queue.Arrival_Q.pop(5)
		#exit(1)
		
		
		
		#exit(1)
		
			
	def sem_display(self):
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
		f.write("The contents of SEMAPHORE ZERO"+"\n")
		f.write("------------------------------"+"\n")

		f.write("The value of semaphore 0 is" + str(self.sem0)+"\n")

		f.write("The wait queue for semaphore 0 is "+str(len(self.semaphore0))+"\n")


		f.write("The contents of SEMAPHORE ONE"+"\n")
		f.write("-----------------------------"+"\n")

		f.write("The value of semaphore 1 is "+ str(self.sem1)+"\n")

		f.write("The wait queue for semaphore 1 is" + str(len(self.semaphore1))+"\n")


		f.write("The contents of SEMAPHORE TWO"+"\n")
		f.write("-----------------------------"+"\n")

		f.write("The value of semaphore 2 is" + str(self.sem2)+"\n")

		f.write("The wait queue for semaphore 2 is "+ str(len(self.semaphore2))+"\n")


		f.write("The contents of SEMAPHORE THREE"+"\n")
		f.write("-------------------------------"+"\n")

		f.write("The value of semaphore 3 is "+ str(self.sem3)+"\n")

		f.write("The wait queue for semaphore 3 is" + str(len(self.semaphore3))+"\n")


		f.write("The contents of SEMAPHORE FOUR"+"\n")
		f.write("------------------------------"+"\n")

		f.write("The value of semaphore 4 is "+ str(self.sem4)+"\n")

		f.write("The wait queue for semaphore 4 is "+ str(len(self.semaphore4))+"\n")

		
	def display_status(self):	
		if filemode == "a":
			f=open("jobs_out_a.txt" , "a")
		elif filemode == "b":
			f=open("jobs_out_b.txt" , "a")
		elif filemode == "c":
			f=open("jobs_out_c.txt" , "a")
			
			
	
		f.write("The contents of the FIRST LEVEL READY QUEUE"+"\n")
		f.write("-------------------------------------------"+"\n")
		if len(self.job_scheduling_queue.Q) == 0:
			f.write("The First Level Ready Queue is empty."+"\n")
		else:
			f.write("Job #  Arr. Time  Mem. Req.  Run Time"+"\n")
			f.write("-----  ---------"+"\n")		
			if len(self.job_scheduling_queue.Q) > 0:	
				for i in self.job_scheduling_queue.Q:
					f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+i['burst_time']+"\n")

		f.write("The contents of the SECOND LEVEL READY QUEUE"+"\n")
		f.write("	-------------------------------------------"+"\n")

		if len(self.job_scheduling_queue.Q2) == 0:
			f.write("The Second Level Ready Queue is empty."+"\n")
		else:
			if len(self.job_scheduling_queue.Q2) > 0:	
				for i in self.job_scheduling_queue.Q2:
					f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+i['burst_time']+"\n")


		f.write("The contents of the I/O WAIT QUEUE"+"\n")
		f.write("	----------------------------------"+"\n")
		
		if len(self.job_scheduling_queue.IO_Q1) == 0:
			f.write("The I/O Wait Queue is empty."+"\n")
		else:
			if len(self.job_scheduling_queue.IO_Q) > 0:	
				for i in self.job_scheduling_queue.IO_Q:
					f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+i['burst_time']+"\n")
			
		self.sem_display()

		f.write("The CPU  Start Time  CPU burst time left"+"\n")
		f.write("-------  ----------  -------------------"+"\n")
		if self.cpu.busy():
			f.write(str(self.cpu.running_process['process_id'])+"\t\t\t"+str(self.cpu.running_process['starttime'])+"\t\t\t"+str(self.cpu.running_process['burst_time'])+"\n")
		else:
			f.write("CPU is idle"+"\n")
		
		f.write("The contents of the FINISHED LIST"+"\n")
		f.write("---------------------------------"+"\n")

		f.write("Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time"+"\n")
		f.write("-----  ---------  ---------  --------  ----------  ---------"+"\n")
		
		if len(self.FinishedQueue) > 0:	
			for i in self.FinishedQueue:
				f.write(i['process_id']+"\t\t\t"+"\t\t\t"+i['mem_required']+"\t\t\t"+str(i['priority'])+"\t\t\t"+str(i['starttime'])+"\t\t\t"+str(i['totaltime'])+"\n")
		
		f.write("There are"+str(self.memory.available())+"blocks of main memory available in the system."+"\n")
		
	def printm(self):
		print(self.memory.available())


class Simulator(object):
	def __init__(self, **kwargs):
		if 'input_file' in kwargs:
			self.input_file = kwargs['input_file']
		else:
			raise Exception("Input file needed for simulator")
		if 'start_clock' in kwargs:
			self.start_clock = kwargs['start_clock']
		else:
			self.start_clock = 0
		self.jobs_dict = load_process_file(self.input_file,return_type="Dict")
		self.wait_jobs_dict={}
		self.ready_jobs_dict={}
		self.system_clock = Clock()
		self.system_clock.hard_reset(self.start_clock) 
		self.scheduler = Scheduler()    
		self.scheduler=Scheduler()
		self.check=check()
		self.cpu = Cpu()
		self.accounting = SystemAccounting()
		self.event_dispatcher = {
			'A': self.scheduler.new_process,
			'D': self.display_status,
			'I': self.scheduler.perform_io,
			'W': self.scheduler.sem_acquire,
			'S': self.scheduler.sem_release,
			'R':self.scheduler.addArrival,
			'L':self.scheduler.addlevel
		}
		print(self.jobs_dict)
		self.Arrivalprocesses = []
		self.Readyprocesses={}
		count = 0
		iocount=0
		dcount=0
	
						
		while len(self.jobs_dict) > 0:
			key = str(self.system_clock.current_time())
			
			if key in self.jobs_dict.keys():
				for k,p in self.jobs_dict.items():
					if key == k:
						print("----------------------------------------------------------------------------")
						print(k)
						self.jobs_dict[k]['priority']=0
						print(self.jobs_dict[k]['priority'])
						event_data = self.jobs_dict[key]
						event_type = event_data['event']
						tot_mem_required = 0
						
						if event_type == 'A':
							if filemode == "a":
								f=open("jobs_out_a.txt" , "a")
							elif filemode == "b":
								f=open("jobs_out_b.txt" , "a")
							elif filemode == "c":
								f=open("jobs_out_c.txt" , "a")
							
							tot_mem_required += int(p['mem_required'])
							print("memory required is")
							print(tot_mem_required)
							bursttime=int(p['burst_time'])
							if(tot_mem_required > 512):
								f.write("Event : " + str(event_type) + "Time :" + str(self.jobs_dict[k]['time'])+"\n")
								f.write("This job exceeds the system's main memory capacity."+"\n")
								break
							
							f.write("Event : " + str(event_type) + "Time :" + str(self.jobs_dict[k]['time'])+"\n")
							event_type='R'
							count=1
								
							id=self.jobs_dict[k]['pid']
							self.event_dispatcher[event_type](event_data)
							self.scheduler.checkmem()
							self.scheduler.checkcpu()
					
							break
								
						elif event_type == 'I':
							self.event_dispatcher[event_type](event_data)
							self.scheduler.checkioaccounting()
							
						elif event_type == 'W':
							self.event_dispatcher[event_type](event_data)
						elif event_type == 'S':
							self.event_dispatcher[event_type](event_data)	
							
						elif event_type == 'D':
							dcount=dcount+1
							if filemode == "a":
								f=open("jobs_out_a.txt" , "a")
							elif filemode == "b":
								f=open("jobs_out_b.txt" , "a")
							elif filemode == "c":
								f=open("jobs_out_c.txt" , "a")
														
							
							
							self.cpu.runningprocess()
							
							if dcount == 11:
								
								self.scheduler.checkaccounting()
								self.scheduler.sem()
								
							else:
								
								self.scheduler.display_status()
								
								
							
								
								#self.scheduler.checkReadyProcess()
								
				del self.jobs_dict[key]					
			self.system_clock += 1	
			
			#self.scheduler.checkcpu()
			self.scheduler.checkioaccounting()
			
			self.scheduler.checkaccounting()
			self.scheduler.levelaccounting()
			self.scheduler.checkwaittime()
			self.scheduler.checkwt()
			#self.scheduler.calculateavgtat()
			#self.scheduler.checkarrivalqueue()
		
		
		print("checks ready process")
		
		
		self.scheduler.checkReadyProcess()
		
		self.scheduler.printm()
		#self.scheduler.printReadyQueue()
		print("\n"+"\n")
		#self.scheduler.printArrivalQueue()
		self.scheduler.printfinalFinishedQueue()
		self.scheduler.calculateavgtat()
		self.scheduler.calculateavgwt()
			
		
	def display_status(self,info):
		print(info)		
	def __str__(self):
		return my_str(self)

if __name__ == '__main__':
	filemode="a"
	file_name1 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_a.txt'
	S = Simulator(input_file=file_name1)
	
	filemode="b"
	file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_b.txt'
	
	#file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_test.txt'
	S = Simulator(input_file=file_name2)
	filemode="c"
	file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_c.txt'
	
	#file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_test.txt'
	S = Simulator(input_file=file_name2)	
	
	print("Outfiles for a , b, c are generated")
