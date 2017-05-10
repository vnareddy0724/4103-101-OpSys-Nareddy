
#!/usr/bin/env python3
from sim_components import *
import random


# === Class: Cpu===

class Cpu(object):
	__shared_state = {}
	def __init__(self, process=None):
		self.__dict__ = self.__shared_state

		if len(self.__shared_state.keys()) == 0:
			self.__type_check(process)
			self.running_process = process
			self.system_clock = Clock()
			self.process_start_time = 0
			self.process_run_time = 0

	def run_process(self, process):
		self.__type_check(process)
		if self.running_process is None:
			self.running_process = process
			self.process_start_time = self.system_clock.current_time()
			return True
		else:
			raise Exception("Process already runnin on CPU, remove running process first.")
		return False
		
	def runningprocess(self):
		print(self.running_process)
		
		return self.running_process

	def remove_process(self):
		if self.running_process is None:
			return False
		process = self.running_process
		self.process_run_time = self.system_clock.current_time() - self.process_start_time
		self.running_process = None
		return {"pid":process, "run_time":self.process_run_time}

	def busy(self):
		return not self.running_process is None

	def __type_check(self,process):
		if not process is None and not isinstance(process, Process):
			raise("CPU Error: Attempted to place a non-process on cpu")

	def __str__(self):
		return my_str(self)

def test_cpu_class():
    # Read in a bunch of process data from our test file

    processes = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/../input_data/processes.txt')

    for i in range(len(processes)):
        processes[i] = Process(**processes[i])
    
    print("Running Cpu class test.....\n")

    myclock = Clock()

    # Init clock to 100 ticks
    myclock+= 100

    single_cpu = Cpu()

    print("Placing process on single_cpu")
    print("\t%s"%single_cpu.run_process(processes[0]))

    print("Placing another process on single_cpu (should fail) =>")
    try:
        print(single_cpu.run_process(processes[1]))
    except:
        print("\tError: process already running on cpu")

    print("Test to see if cpu is busy, before loading a process=>")
    if not single_cpu.busy():
        try:
            single_cpu.run_process(processes[1])
        except:
            print("\tprocess already running on cpu")
    else:
        print("\tcpu busy, cannot run process")

    print("Adding some random time to clock, so process run time wont be init value of clock")
    myclock += random.randint(500,1000)

    print("Removing process from single_cpu=>")
    
    print("\t%s"%single_cpu.remove_process())

    print("Adding different process to single_cpu")
    print("\t%s"%single_cpu.run_process(processes[1]))

    print("Adding some random time to clock, so process run time wont be init value of clock")
    myclock += random.randint(500,1000)

    print("Removing process from single_cpu")
    p2 = single_cpu.remove_process()

    print("\t%s"%p2)


    print("Attempting to run a NON process on a cpu=>")
    try:
        single_cpu.run_process("not a process")
    except:
        print("\tError: Not a process, cannot be run.")

if __name__=='__main__':
    test_cpu_class()
   
