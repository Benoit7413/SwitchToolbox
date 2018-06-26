import sys
if sys.version_info < (3, 6):
    sys.stdout.write("Please run this script with Python 3\n")
    sys.exit(1)

import toolbox
import base64
from toolbox.__constants__ import HEADER
print(base64.b64decode(HEADER).decode())
toolbox.main(sys.argv)
