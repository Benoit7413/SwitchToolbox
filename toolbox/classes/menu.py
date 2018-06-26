from toolbox.classes.keys import Keys
from toolbox.classes.build import Build
from libs.colorama import init, Fore, Back, Style
init()

global Menu


class Menu():

    def main(self, argv):
        print("Keys.file_present : " + self.color_boolean(Keys.file_present))
        print("Keys.is_valid : " + self.color_boolean(Keys.is_valid))
        print("Build.git_present : " + self.color_boolean(Build.git_present))
        print("Build.devkitPro_present : " +
              self.color_boolean(Build.devkitPro_present))
        print("Build.libnx_valid : " + self.color_boolean(Build.libnx_valid))
        print('')
        if len(argv) > 1:
            if argv[1] == "build":
                Build.build_atmosphere()

    def color_boolean(self, boolean):
        if boolean is True:
            return Fore.GREEN + str(boolean) + Style.RESET_ALL
        elif boolean is False:
            return Fore.RED + str(boolean) + Style.RESET_ALL
        return Fore.ORANGE + str(boolean) + Style.RESET_ALL


Menu = Menu()
