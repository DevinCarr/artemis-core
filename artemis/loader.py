import os
import sys
import importlib
from .stdcmd import io

class Loader:
    def __init__(self,artemis_core):
        self.core = artemis_core
        self.user_folder = os.path.expanduser("~")
        self.FOLDERSTORE = "{}/{}".format(self.user_folder,".artemis")
        self.check_folder()

    def check_folder(self):
        """Check and create the folder for artemis external modules"""
        try:
            write_ok = os.access(self.user_folder,os.W_OK)
            os.mkdir(self.FOLDERSTORE)
        except PermissionError as e:
            io.op(e)
        except OSError as e:
            pass
        self.load_modules()
        self.add_loader_commmands()

    def add_module(self,args):
        """Take a github link and download the module into the FOLDERSTORE"""
        if args:
            folder = '{}/{}'.format(self.FOLDERSTORE,args[0].split('/')[-1].split('.')[0])
            cmd = 'git clone {} {}'.format(args[0],folder).split(' ')
            self.core.check_bash(cmd)
            self.load_modules()
        else:
            io.op('No plugin url provided')

    def load_modules(self):
        """Check extra modules loaded into the FOLDERSTORE"""
        list_of_imports = os.listdir(self.FOLDERSTORE)
        # Add all of the modules to the path
        for item in list_of_imports:
            path = '{0}/{1}'.format(self.FOLDERSTORE,item)
            inner_items = os.listdir(path)
            module_name = ''
            items = [x for x in inner_items if self.check_item(x)]

            if len(items) > 1:
                io.op('Import: {} could not be loaded because the module couldn\'t be found'.format(path))
                print(items)
            else:
                module_name = items[0]
            sys.path.append(path)
            # Import the new module
            module = importlib.import_module(module_name)
            self.add_command(module.__name__,module.execute,module.help_message)
            io.op('Imported: {}'.format(module_name))

    def check_item(self,item):
        if item.find('.') != -1:
            return False
        elif item.find('LICENSE') != -1:
            return False
        elif item.find('README') != -1:
            return False
        elif item.find('tests') != -1:
            return False
        else:
            return True

    def add_command(self,name,func,helpm):
        self.core.commands.create_command([name,func,helpm])

    def add_loader_commmands(self):
        new_command = ["get",self.add_module,"Add a new module from github"]
        self.core.commands.create_command(new_command)
