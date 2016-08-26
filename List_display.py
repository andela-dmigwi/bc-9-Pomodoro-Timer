import os
import logging
from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.command import Command
from cliff.show import ShowOne
from cliff.lister import Lister
from db_manage import DbManage


class ListItems(Lister):
    #"Show details about a file"

    log = logging.getLogger(__name__)    

    def take_action(self, parsed_args):
        self.db = DbManage()
        self.db.connect_db()
        columns = ('',
                   'Task Title',
                   'Start Time',
                   'Duration',
                   'Short Break',
                   'Long Break',
                   'Cycles',
                   'Status',
                   'Sound Status',
                   )
    
        data = self.db.retrieve_all_entries()        
        return (columns, data)
    
    # def take_action(self, parsed_args):
    #     #argv = str(parsed_args.arg)
    #     msg = "You provided the wrong command use 'pomodoro' for help"
    #     self.db = DbManage()
    #     self.db.connect_db()
    #     columns = ('',
    #                'Task Title',
    #                'Start Time',
    #                'Duration',
    #                'Short Break',
    #                'Long Break',
    #                'Cycles',
    #                'Status',
    #                'Sound Status',)
    #     #if  param == None:
    #     data = self.db.retrieve_all_entries()
    #     # else:            
    #     #     param = argv.split("*",1)[1]
    #     #     if len([x for x in param.split(':') if x.isdigit()]) == 3:
    #     #         argv = self.normal_day_to_timestamps(argv)
    #     #         msg = "List is bieng processed"
    #     #     data = self.db.retrieve_entries_past_timestamp(argv)
    #     return (columns, data)

    # #should be in the format d/m/Y
    # def normal_day_to_timestamps(self, normaltime):
    #     date = datetime.datetime.strptime(normaltime, "%d/%m/%Y")        
    #     return calendar.timegm(date.utctimetuple())
    
        
        