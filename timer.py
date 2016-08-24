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
    CREATED = {'uuid'= str(uuid.uuid4()), 'title'='',
                'start_time'= int(time.time()), 
                'duration'=25, 'shortbreak' = 5,
                'longbreak' = 15, 'cycle'=0, 
                'statusuuid'='37806757-4391-4c40-8cae-6bbfd71e893e', #Status active
                'sounduuid'='510b9503-7899-4d69-83c0-690342daf271'} #sound on
    #statusuuid
    active = '37806757-4391-4c40-8cae-6bbfd71e893e'
    pending = '0eaec4f3-c524-40ab-b295-2db5cb7a0770'
    finished = 'f82db8cc-a969-4495-bffd-bb0ce0ba877a'
    running = '6c25b6d2-75cc-42c3-9c8c-ccf7b54ba585'

    #sounduuid
    on = '510b9503-7899-4d69-83c0-690342daf271'
    off = '05797a63-51f5-4c1d-9068-215c593bba8d'   



    def __init(self, command):
        self.command = command      
        self.response = ''

    def timestamp_to_normal(self, timestamp):
        '''Method coverts timestamp to Normal time'''
        return str(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

    def populate_tt_dict(self, key, value, msg):
        '''Manages the dict and returns the appropriate message'''
        if self.tt_dict not None and key not '':
            self.tt_dict[key] = value
            response  = msg
        response = "Run the command 'pomodoro help' To get help!"

    def add_two_lists(self, list1):
        seconds = [86400,3600,60,1]
        list1 = [seconds[i] * item for i, item in enumerate(list1)]
        return sum(list1)


    def command_type(self):
        
        # if command is start*Migwi     
        if 'start*' in self.command:
            self.tt_dict = TimerThread.CREATED          
            msg = 'You have created a task called %s'%self.command.split('*':1)
            self.populate_tt_dict('title', self.command.split('*':1), msg)

        # time*1:3:2         
        elif 'time*' in self.command or 'config_time*' in self.command or
                elif 'config_shortbreak*' in self.command or 'config_longbreak*' in self.command:
            cmd = self.command.split('*':1).split(':')          
            cmd = [int(x) for x in cdm if x.isdigit()]
            times = self.add_two_lists(cmd)

            if  'time*' in self.command:    
                    times = times + int(time.time())                
                    msg = "Your start time is set at %"%self.timestamp_to_normal(times)
                    self.populate_tt_dict('start_time', time, msg)

            elif  'config_time*' in self.command:                   
                    msg = "Your duration time is set at %"%self.timestamp_to_normal(times)
                    self.populate_tt_dict('duration', time, msg)

            elif  'config_shortbreak*' in self.command:                 
                    msg = "Your short break time is set at %"%self.timestamp_to_normal(times)
                    self.populate_tt_dict('shortbreak', time, msg)

            elif  'config_longbreak*' in self.command:                  
                    msg = "Your long break time is set at %"%self.timestamp_to_normal(times)
                    self.populate_tt_dict('longbreak', time, msg)


        #  sound*on       
        elif 'sound*' in self.command:
            cmd = self.command.split('*':1)  
            if 'off' in cmd:
                msg = 'Sound Ringing is OFF'
                self.populate_tt_dict('sounduuid', TimerThread.off, msg)
            msg = 'Sound Ringing is ON'
            self.populate_tt_dict('sounduuid', TimerThread.on, msg)

        #  else if command create*Migwi
        #   push statusuuid active in dict
        #   push all the data in the dict into the database
        elif 'create*' in self.command:
        #       send self.tt_dict to database
        msg = 'You task has been set'
        self.populate_tt_dict('', TimerThread.on, msg)


        #  else if command pause*migwi
        #   push statusuuid pending in database
        #   remove it from active_dict to pending_dict
        elif 'pause*' in self.command:
        #       send self.command.split('*':1) 

        #  else if command stop*migwi
        #   push statusuuid finished in database
        elif 'stop*' in self.command:
        #       send self.command.split('*':1) 

        #  else if command list
        #   list display all details in database
        elif 'stop*' in self.command:
        #       send self.command.split('*':1) 

        #  else if command list*migwi
        #   get all tasks with title migwi and display them
        elif 'stop*' in self.command:
        #       send self.command.split('*':1) 

        #  else if command list*12d:7m:2016y
        #   get all tasks set on specified date
        elif 'stop*' in self.command:
        #       send self.command.split('*':1)      
        #'''
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



