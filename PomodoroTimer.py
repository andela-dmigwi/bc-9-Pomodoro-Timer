import sys
import logging
from cliff.app import App
from cliff.commandmanager import CommandManager
from pomodoro_command import MyCommand
from cliff.show import ShowOne
from cliff.lister import Lister
from List_display import ListItems

class PomodoroTimer(App):
    '''
    This module will hold main file that will be run.
    This is where the cliff implementation begins from
    '''

    log = logging.getLogger(__name__)
    def __init__(self):
        command = CommandManager('PomodoroTimer.app')
        super(PomodoroTimer, self).__init__(
            description = 'sample app',
            version = '0.1',
            command_manager = command,
        )
        commands = {
        'pomodoro': MyCommand,
        'listitems': ListItems
        }

        for k, v in commands.iteritems():
            command.add_command(k, v)


    def initialize_app(self, argv):
        self.log.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

def main(argv=sys.argv[1:]):
    app = PomodoroTimer()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))