from toolbox.__constants__ import DEBUG
from toolbox.__constants__ import DEBUG_LEVEL

global Functions


class Functions(object):

    def __init__(self):
        self.debug_lines = ""

    def debug(self, str, level):
        tags = {0: "",
                1: "[WARN] ",
                2: "[INFO] ",
                3: "[DEBUG] "
                }
        str = tags[level] + str
        if DEBUG is True and level <= DEBUG_LEVEL:
            self.debug_lines += str + "\r\n"

    def print_debug(self):
        print(self.debug_lines)


Functions = Functions()
