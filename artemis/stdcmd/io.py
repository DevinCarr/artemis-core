import os

def op(message):
    """Standard output handler"""
    if message is not None:
        print(str(message))
        return message

def ip(message=''):
    """Standard input handler"""
    return input('^Arty: {0}'.format(message))

def change_directory(args):
    if type(args) is list and args:
        args = args[0]
    try:
        os.chdir(args)
    except FileNotFoundError:
        op('No such file or directory: \'{}\''.format(args))
