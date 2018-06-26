from toolbox.__version__ import __version__
from toolbox.__version__ import __title__
from toolbox import classes
from toolbox.classes.keys import Keys
from toolbox.classes.functions import Functions
from toolbox.classes.menu import Menu


def main(argv):
    print("Runing " + __title__ + " version : " + __version__)
    Menu.main(argv)
    Functions.print_debug()
