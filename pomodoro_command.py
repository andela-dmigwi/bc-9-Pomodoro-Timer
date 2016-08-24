import os
import logging
from cliff.command import Command

class MyCommand(Command):
    '''
    This Module will hold the cliff implementation that retrieves the
    various command input by the user
    This module also will hold cliff framework implementation although 
    with some modification
    '''

    log = logging.getLogger(__name__)
     
    #parses the args passed and returns them
    def get_parser(self, prog_name):
        parser = super(MyCommand, self).get_parser(prog_name)
        parser.add_argument('arg', nargs='?', default=None)

        return parser

    #picks the parsed arguments and uses them
    def take_action(self, parsed_args):
        #self.app.stdout.write(str(parsed_args.arg) + "\n")
        print(str(parsed_args.arg))
        #Send argument to timer module