from threading import Timer
import time
import datetime
import pygame # Load the required library to play music
from db_manage import DbManage
from helpmessage import HelpMessage


class TimerThread(object):
    ''' This will hold the main implementation of the  project   '''

    #Class variables
    RUNNING = {}
    ACTIVE = {}
    PENDING = {}
    FINISHED = {}
    CREATED = {'uuid': str(uuid.uuid4()), 
                'title':'',
                'start_time' : int(time.time()), 
                'duration': 25, 
                'shortbreak':5,
                'longbreak' : 15, 
                'cycle':0, 
                'statusuuid':'37806757-4391-4c40-8cae-6bbfd71e893e', #Status active
                'sounduuid':'510b9503-7899-4d69-83c0-690342daf271'} #sound on
    #statusuuid
    active = '37806757-4391-4c40-8cae-6bbfd71e893e'
    pending = '0eaec4f3-c524-40ab-b295-2db5cb7a0770'
    finished = 'f82db8cc-a969-4495-bffd-bb0ce0ba877a'
    running = '6c25b6d2-75cc-42c3-9c8c-ccf7b54ba585'

    #sounduuid
    on = '510b9503-7899-4d69-83c0-690342daf271'
    off = '05797a63-51f5-4c1d-9068-215c593bba8d'   



    def __init(self):             
        self.response = ''
        self.db = DbManage()

    def timestamp_to_normal(self, timestamp):
        '''Method coverts timestamp to Normal time'''
        return str(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

    def populate_tt_dict(self, key, value, msg):
        '''Manages the dict and returns the appropriate message'''
        if len(self.tt_dict) > 0 and len(key) > 0:
            self.tt_dict[key] = value
            response  = msg
        response = "Run the command 'pomodoro help' To get help!"

    def add_two_lists(self, list1):
        seconds = [86400,3600,60,1]
        list1 = [seconds[i] * item for i, item in enumerate(list1)]
        return sum(list1)

    def implement_time_methods(self, command):
        ''' Implement the time methods '''

        cmd = command.split('*',1)[1].split(':')
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




    def command_type(self, command):
        self.command = command 
        # if command is create*Migwi     
        if 'create*' in self.command:
            msg = "The task name you selected is still active, Please select another one"
            cmd = self.command.split('*',1)[1]
            data = self.db.get_all_tasks_by_name(cmd)
            if len(data) > 0:
                self.tt_dict = TimerThread.CREATED          
                msg = 'You have created a task called %s'%cmd
            self.populate_tt_dict('title', cmd, msg)


        # time*1:3:2         
        elif 'time*' in self.command:
           self.implement_time_methods(self.command) 

        elif 'config_time*' in self.command:
            self.implement_time_methods(self.command)

        elif 'config_shortbreak*' in self.command:
            self.implement_time_methods(self.command)

        elif 'config_longbreak*' in self.command:
            self.implement_time_methods(self.command)
            

        #  sound*on       
        elif 'sound*' in self.command:
            cmd = self.command.split('*',1)  
            if 'off' in cmd:
                msg = 'Sound Ringing is OFF'
                self.populate_tt_dict('sounduuid', TimerThread.off, msg)
            msg = 'Sound Ringing is ON'
            self.populate_tt_dict('sounduuid', TimerThread.on, msg)

        #  else if command start*Migwi
        elif 'start*' in self.command: 
            cmd = self.command.split('*',1)
            msg = 'You provided an incorrect command'
            data = self.db.get_entries_with_status(self, TimerThread.pending, cmd)

            if len(self.tt_dict) > 0 and self.tt_dict['title'] == cmd:
                if data: #Will contain at most one entry
                    uuid = data[0][0] 
                    end_time = data[0][2] + data[0][3]
                else:
                    uuid = self.tt_dict['uuid']
                    end_time = self.tt_dict['start_time'] + self.tt_dict['duration']

                TimerThread.ACTIVE[uuid] = end_time
                msg = 'Your task is active and is due at %s'%self.timestamp_to_normal(end_time)
                self.tt_dict['statusuuid'] = TimerThread.active
                self.db.store_a_new_record(self.tt_dict)   
                self.tt_dict = None 
                self.populate_tt_dict('', 'Display', msg) 

            self.populate_tt_dict('', '', msg) #Should raise an error with a help message



        #  else if command pause*migwi
        elif 'pause*' in self.command:
            cmd =  self.command.split('*',1)
            title = None
            msg = 'Your task wasn\'t found'
            data = self.db.get_entries_with_status(self, TimerThread.active, cmd) 
            if len(data) > 0:
                msg = 'Your task has been paused.'
                uuid = data[0][0] #should contain atmost one item
                TimerThread.ACTIVE.remove[uuid]
                TimerThread.PENDING[uuid] = data['start_time'] + data['duration'] 
                self.db.update_the_status(TimerThread.pending, uuid)
                self.populate_tt_dict('', 'Display', msg)####

            self.populate_tt_dict('', '', msg) #Should raise an error with a help message

        #  else if command stop*migwi        
        elif 'stop*' in self.command:
            cmd =  self.command.split('*',1) 
            uuid = None
            msg = 'Your task wasn\'t found'
            data = self.db.get_entries_with_status(self, TimerThread.pending, cmd)
            if len(data) > 0:
                msg = 'Your task has been stopped.'
                uuid = data[0][0]                             
                TimerThread.PENDING.remove[uuid] 
                self.db.update_the_status(TimerThread.finished, uuid) 
                self.populate_tt_dict('', 'Display', msg)

            self.populate_tt_dict('', '', msg) #Should raise an error with a help message           

        # #  else if command list       
        # elif 'list' == self.command:
        # #Select all the entries an display them 

       
        # #  else if command list*12:07:2016       
        # elif 'list*' in self.command:
        #     cmd = self.command.split('*',1)      
        #     times = int(datetime.datetime.strptime(cmd, '%d:%m:%Y').strftime("%s"))
        #     #retrieve all details with timestamps greater than times


        print HelpMessage.help_message

    # def check_time(self):
    #     ''' after 30 second execute thread_timer() and execute_alarm() '''
    #     task1 = Timer(30.0, thread_timer)
    #     task1.start()

    #     task2 = Timer(30.0, execute_alarm) 
    #     task2.start()


    def thread_timer(self):
        '''
        maintain active dict and pending dict:
        if the said timestamp is in active dict push the task in running dict
        else its in pending dict change its statusuuid to finished
        remove it from pending items
        '''
        current_time = int(time.time())
        TimerThread.RUNNING = { k:v for k,v in TimerThread.ACTIVE.iteritem() if v >= current_time }
        TimerThread.FINISHED = { k:v for k,v in TimerThread.PENDING.iteritem() if v >= current_time }

    def execute_alarm(self):
        ''' Execute tasks in TimerThread.RUNNING dict  '''

        if len(TimerThread.RUNNING): #is greater than zero do run a task 
            for k,v in TimerThread.RUNNING.iteritems():
                data = {}#Retrieve title,sounduuid of the key/uuid from the database
                if len(data):
                    print 'Your %s task is over'%data['title']
                    self.play_music(data['sounduuid'])
                    

            
    def play_music(self, sounduuid):
        ''' plays songs '''
        if sounduuid == TimerThread.on: #play the music
            pygame.mixer.init()
            pygame.mixer.music.load('song/track.mp3')
            pygame.mixer.music.play()

            # p = vlc.MediaPlayer("song/track.mp3")
            # p.play()
            # p.stop()





#def check_time(self):
''' after 30 second execute thread_timer() and execute_alarm() '''
task1 = Timer(30.0, self.thread_timer)
task1.start()

task2 = Timer(30.0, self.execute_alarm) 
task2.start()