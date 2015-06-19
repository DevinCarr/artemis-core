import sys
from .core import Core
VERSION = "0.4.0"

def main():
    """Entry point for artemis-core"""
    arty = Core(VERSION)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            return arty.run_tests()
    while True:
        try:
            arty.ask_question()
        except KeyboardInterrupt:
            print("")
