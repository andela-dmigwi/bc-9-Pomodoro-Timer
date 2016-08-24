from threading import Timer
import time


class TimerThread(object):
    '''
    This will hold the main implementation of the  project  
    '''
    #Class variables
    # dicts will hold key as uuid and value as timestamp
    RUNNING = {}
    ACTIVE = {}
    PENDING = {}
    FINISHED = {}



    def __init(self, command):
    	self.command = command

    def command_type(self):
    	'''Check command type and do the respective action
    	if command is start*Migwi
    	    create a dict to store all the details before pushing data to db
    	else if command  is time*1h:3min:2s
    	    push it in dict as start_time
    	 else if command is config_time*25;
    	 	push it in dict as duration
    	 else if command is config_shortbreak*5
    	 	push it in dict as shortbreak
    	 else if command is sound*on
    	 	push it in dict as sounduuid

    	 else if command create*Migwi
    	 	push statusuuid active in dict
    	 	push all the data in the dict into the database

    	 else if command pause*migwi
    	 	push statusuuid pending in database
    	 	remove it from active_dict to pending_dict

    	 else if command stop*migwi
    	 	push statusuuid finished in database

    	 else if command list
    	 	list display all details in database

    	 else if command list*migwi
    	 	get all tasks with title migwi and display them

    	 else if command list*12d:7m:2016y
    	 	get all tasks set on specified date
		'''
    	print self.command

    def check_time(self):
    	''' after 30 second execute thread_timer() and execute_alarm() '''
    	task1 = Timer(30.0, thread_timer)
    	task1.start()

    	task2 = Timer(30.0, execute_alarm) 
    	task2.start()


    def thread_timer(self):
    	'''
    	maintain active dict and pending dict:
    	after 30 seconds check if current timestamp is greater 
    	or equal to timestamp in those dicts
    	if the said timestamp is in active dict:
    		push the task in running dict
    	else its in pending dict:
    		change its statusuuid to finished
    		remove it from pending list
    	'''
    	current_time = int(time.time())
    	TimerThread.RUNNING = { k:v for k,v in TimerThread.ACTIVE.iteritem() if v >= current_time }
    	TimerThread.FINISHED = { k:v for k,v in TimerThread.PENDING.iteritem() if v >= current_time }

    def execute_alarm(self):
    	'''
    	if a task is in running dict execute it 
    	till it ends after 40 sec or till stopped
    	'''
    	if len(TimerThread.RUNNING): #is greater than zero do run a task 



