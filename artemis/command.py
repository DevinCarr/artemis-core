from .stdcmd import io

class Commands:
    """Class to handle the commands"""
    def __init__(self):
        # List of default commands
        default = [('lc',Acmd('lc',self.list_commands,'List of all Artemis\'s Current Commands.')),
                    ('help',Acmd('help',print_help,'List the help')),
                    ('newc',Acmd('newc',self.create_command,'Create a new command.')),
                    ('cd',Acmd('cd',io.change_directory,'Change directory.')),
                    ('quit',Acmd('quit','import sys; sys.exit(0)','Quit Artemis.'))]
        self.command_list = dict(default)

    def create_command(self,args):
        prompt = None
        function = None
        helpm = None
        if len(args) == 3:
            prompt = args[0]
            function = args[1]
            helpm = args[2]
        if prompt == None:
            prompt = io.ip('Name: ')
            keys = self.command_list.keys()
            while prompt in keys:
                io.op('Sorry, that function name is taken, please try another.')
                prompt = io.ip('Name: ')
        if function == None:
            function = io.ip('{:s}\'s operation: '.format(prompt))
        if helpm == None:
            helpm = io.ip('{:s}\'s definition: '.format(prompt))
        self.command_list[prompt] = Acmd(prompt,function,helpm)

    def list_commands(self,args):
        """List all of the currently loaded arty-commands"""
        io.op('Artemis\'s current command list:')
        for command in self.command_list:
            self.command_list[command].disp_help()

class Acmd:
    """Standard Artemis (Python-based) Command"""
    def __init__(self,name,function,helpm):
        self.name = name
        self.function = function
        self.helpm = helpm

    def execute(self,args):
        result = None
        passing = args
        if type(args) is list and len(args) > 1:
            passing = args
        if type(self.function) == str:
            result = exec(self.function)
        else:
            result = self.function(passing)
        return result

    def disp_help(self):
        if type(self.helpm) != str:
            io.op('{:s}\t - {:s}'.format(self.name,self.helpm()))
        else:
            io.op('{:s}\t - {:s}'.format(self.name,self.helpm))

def print_help(args):
    """Print the help message"""
    helpMessage = '\nArtemis v{0}\n\nA simple inline configurable shell bot in python.'
    from artemis import VERSION
    io.op(helpMessage.format(VERSION))
