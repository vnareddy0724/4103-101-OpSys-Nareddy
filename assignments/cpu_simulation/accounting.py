
#!/usr/bin/env python3
from sim_components import *
import random

# === Class: Accounting===

class Accounting(object):
    """The accounting object lets processes keep track of thier own stats.

    - **total_burst_time** (int):
        - Total burst time is dened as the amount of time a process is actually using the CPU.
        Therefore, this measure does not include context switch times. Note that this measure
        can simply be calculated from the given input data.
    - **num_bursts** (int)   :
        - Number of CPU bursts needed to complete job
    - **turnaround_time** (int):
        - Turnaround time is defined as the end-to-end time a process experiences for a single CPU
        burst. More specically, this starts with the arrival time in the ready queue through to
        when the process finishes all of its CPU bursts. As such, this measure includes context
        switch times.
    - **wait_time** (int):
        - Wait time is defined as the amount of time a process spends waiting to use the CPU, which
        equates to the amount of time the given process is in the ready queue and blocked for I/O.
        Therefore, this measure does not include context switch times that the given process
        experiences (i.e., only measure the time the given process is actually in the ready queue).
    - **start_time** (int):
        - Simulation clock time when process entered ready queue.
    - **end_time** (int):
        - Simulation clock time when process left / exited the simulation.
    """
    def __init__(self):
        self.total_burst_time = 0
        self.turnaround_time = 0
        self.wait_time = 0
        self.start_time = 0
        self.end_time = 0
        self.num_bursts = 0
        
    def __setitem__(self, key, val):
        """
        "setitem" allows the '[]' brackets to be used to set a data member. I used this as a
        shortcut to access the many data members used by this class, especially since it is
        composed of a 'Pcb' and 'Accounting' class.
        """
        if hasattr(self, key):
            setattr(self, key, val)
        else:
            setattr(self, key, val)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return None

    def __str__(self):
        """
        Visual dump of class state.
        """
        return my_str(self)

###################################################################################################

# === Class: SystemAccounting===

class SystemAccounting(object):
    """
    This is a GLOBAL singleton class that keeps track of all accounting for the system. Each process
    will register itself with this class and get its own instance of the Accounting class. This
    class maintains a "shared" state based on the Borg pattern by Alex Martelli
    http://code.activestate.com/recipes/66531/
    """
    __shared_state = {}
    def __init__(self, acct_pid=None):
        """***init***: Constructor for Accounting class
        - **Args**:
            - acct_pid (int) : The process id used as a dict key to keep track of its own accounting
        """
        self.__dict__ = self.__shared_state

        # If the 'accounts' dictionary doesn't exist yet, create it.
        if not hasattr(self, 'accounts'):
            print("resetting accounts")
            self.accounts = {}

        # Register process and get own instance of account class
        if not acct_pid is None:
            self.accounts[acct_pid] = Accounting()
			
        if not hasattr(self, 'randomvar'):	
            self.randomvar = random.randint(0,999999999)

    def __str__(self):
        string = ""
        for ss_key, ss_val in self.accounts.items():
            #print(ss_key)
            string += "[ Process_ID: " + str(ss_key) + " \n  " + my_str(ss_val) + "\n"
        return string

    
    def __setitem__(self, key, pair):
        """No error checking!!
        """
        subkey,val = pair
        self.accounts[key][str(subkey)] = val
        #print(self.accounts[key].acct)
        
    def register_process(self,p):
        self.accounts[p.process_id] = p


    def calc_totals(self):
        # To be implemented by you
        for k,v in self.accounts.items():
            print(k,v)


            
            
if __name__=='__main__':

    S = SystemAccounting()
    #p = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_c.txt')
    processes = {}
	
    count = 0
    for i in range(len(p)):
        print(p[i])
        processes[p[i]['pid']] = Process(**p[i])
        S.register_process(processes[p[i]['pid']])
        count += 1
        if count >= 5:
            break
			
    print(S)
    pid = str(5)
    processes[pid]['state'] = 'Running'
    pid = str(4)
    S[pid] = ('turnaround_time','455')
    print(S)

	

    
 
