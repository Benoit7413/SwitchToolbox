import subprocess
import os
from os import environ
from toolbox.classes.functions import Functions

global Build


class Build(object):

    def __init__(self):
        self.check_git()
        self.check_devkit()

    def check_git(self):
        try:
            null = open(os.devnull, "w")
            subprocess.Popen(["git", "--version"], stdout=null, stderr=null)
            null.close()
            self.git_present = True
        except OSError:
            Functions.debug("git not found", 1)
            self.git_present = False

    def check_devkit(self):
        try:
            os.environ["DEVKITPRO"]
            self.devkitPro_present = True
        except KeyError:
            Functions.debug(
                "Please set DEVKITPRO in your environment.\
                 export DEVKITPRO=<path to>/devkitpro", 1)
            self.devkitPro_present = False
        if self.devkitPro_present is True:
            try:
                if 'DomainMessageType' in \
                        open(os.environ["DEVKITPRO"] +
                             "/libnx/include/switch/kernel/ipc.h").read():
                    self.libnx_valid = True
                else:
                    self.libnx_valid = False
                    Functions.debug("Please update libnx", 1)
            except Exception as e:
                self.libnx_valid = False
                Functions.debug("libnx not found", 1)

    def build_atmosphere(self):
        os.system("rm -rf build")
        os.system(
            "git clone \
            https://github.com/Atmosphere-NX/Atmosphere \
            repo/Atmosphere")
        os.chdir("repo/Atmosphere")
        os.system("make clean")
        os.system("make")
        os.chdir("../..")
        os.makedirs("build/fusee")
        os.makedirs("build/kip")
        os.system(
            "cp \
            repo/Atmosphere/fusee/fusee-secondary/fusee-secondary.bin \
            build/fusee")
        os.system(
            "cp repo/Atmosphere/fusee/fusee-primary/fusee-primary.bin \
            build/fusee")
        os.system(
            "cp repo/Atmosphere/thermosphere/thermosphere.bin \
            build/fusee")
        os.system(
            "cp repo/Atmosphere/exosphere/exosphere.bin \
            build/fusee")
        os.system(
            "cp repo/Atmosphere/exosphere/bpmpfw/bpmpfw.bin \
            build/fusee")
        # fs_mitm
        os.chdir("repo/Atmosphere/stratosphere/fs_mitm")
        os.system("make")
        os.chdir("../../../..")
        os.system("cp repo/Atmosphere/stratosphere/*/*.kip build/kip/")


Build = Build()
