
#!/usr/bin/env python3
from sim_components import *



# === Class: FCFS===

class Fifo(list):
	def __init__(self,init=[]):
		self.Q = []
		self.Arrival_Q=[]
		self.IO_Q=[]
		self.IO_Q1=[]
		self.Q2=[]
		if len(init) > 0:
			for i in init:
				self.add(i)
	def printFifo(self):
		for i in self.Q:
			print(i)
			
	def add(self,proc):
		if not isinstance(proc,Process):
			raise Exception("Queue requires items added to be of type 'Process'")
		self.Q.append(proc)
		print(len(self.Q))
		
	def IOadd(self,proc):
		if not isinstance(proc,Process):
			raise Exception("Queue requires items added to be of type 'Process'")
		self.IO_Q.append(proc)
		
	def leveladd(self,proc):
		if not isinstance(proc,Process):
			raise Exception("Queue requires items added to be of type 'Process'")
		self.Q2.append(proc)	
		
		
	def IOremove(self):
		return self.IO_Q.pop(0)
		
		
	def Arrivaladd(self,proc):
		if not isinstance(proc,Process):
			raise Exception("Queue requires items added to be of type 'Process'")
		self.Arrival_Q.append(proc)
	
		
	def remove(self):
		return self.Q.pop(0)
		
	def Arrivalremove(self):
		return self.Arrival_Q.pop(0)
		

	def empty(self):
		return len(self.Q) == 0
		
	def Arrivalempty(self):
		return len(self.Arrival_Q) == 0	
		
	def Arrivalfirst(self,key=None):
		if self.empty():
			return False 

		if key is None:
			return self.Arrival_Q[0]
		else:
			return self.Arrival_Q[0][key]	

	def first(self,key=None):
		if self.empty():
			return False 

		if key is None:
			return self.Q[0]
		else:
			return self.Q[0][key]            

	def last(self,key=None):
		if key is None:
			return self.Q[-1]
		else:
			return self.Q[-1][key]   

	def __str__(self):
		return my_str(self)

	def __iter__(self):
		for elem in self.Q:
			yield elem

if __name__=='__main__':

    # read process information from file
    p = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/../input_data/processes.txt')

    # create a fifo queue
    processes = Fifo()
    count = 0

    # create processes from data from file
    for i in range(len(p)):
        processes.add(Process(**p[i]))
        count += 1
        
        # stop at 5 for testing purposes
        if count >= 5:
            break
    
    while not processes.empty():
        # get memory_required from process at front of queue
        mr = processes.first('mem_required')

        # print memory_required
        print(mr)

        processes.remove()
