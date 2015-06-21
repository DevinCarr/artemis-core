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
        if len(args):
            cmd = "git clone {} {}".format(args[0],self.FOLDERSTORE).split(' ')
            self.core.check_bash(cmd)

    def load_modules(self):
        """Check extra modules loaded into the FOLDERSTORE"""
        list_of_imports = os.listdir(self.FOLDERSTORE)
        # Add all of the modules to the path
        for item in list_of_imports:
            path = '{0}/{1}'.format(self.FOLDERSTORE,item)
            inner_folders = os.listdir(path)
            module_name = inner_folders[0]
            if len(inner_folders) > 1:
                inner_folders.remove('tests')
                module_name = inner_folders[0]
            sys.path.append(path)
            # Import the new module
            module = importlib.import_module(module_name)
            self.add_command(module.__name__,module.execute,module.help_message)
            io.op('Imported: {}'.format(module_name))

    def add_command(self,name,func,helpm):
        self.core.commands.create_command([name,func,helpm])

    def add_loader_commmands(self):
        new_command = ["add",self.add_module,"Add a new module from github"]
        self.core.commands.create_command(new_command)
