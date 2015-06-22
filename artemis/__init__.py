import sys
from .core import Core
from .loader import Loader
VERSION = "0.5.0"

def main():
    """Entry point for artemis-core"""
    arty = Core(VERSION)
    load = Loader(arty)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            return arty.run_tests()
    while True:
        try:
            arty.ask_question()
        except KeyboardInterrupt:
            print("")
