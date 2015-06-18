from .core import Core
VERSION = "0.2.0"

def main():
    """Entry point for artemis-core"""
    arty = Core(VERSION)
    while True:
        try:
            arty.ask_question()
        except KeyboardInterrupt:
            print("")
