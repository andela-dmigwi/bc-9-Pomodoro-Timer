import logging
#from cliff.command import Command
from timer import TimerThread
from helpmessage import HelpMessage

class MyCommand(Command):

    timer_obj = TimerThread()
    '''
    This Module will hold the cliff implementation that retrieves the various command input by the user
    This module also will hold cliff framework implementation although with some modification
    '''

    log = logging.getLogger(__name__)
     
    #parses the args passed and returns them
    def get_parser(self, prog_name):
        parser = super(MyCommand, self).get_parser(prog_name)
        parser.add_argument('arg', nargs='?', default=None)

        return parser

    #picks the parsed arguments and uses them
    def take_action(self, parsed_args):
        argv = str(parsed_args.arg)
        if(argv == None):       
            print HelpMessage.help_message
        MyCommand.timer_obj.command_type(argv)