# import logging
# import os

# from cliff.lister import Lister
import os
import sys
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
    
        