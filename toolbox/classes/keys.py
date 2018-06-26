import os
import hashlib
import binascii
import configparser
from toolbox.__constants__ import KEY_HASHES
from toolbox.classes.functions import Functions


global Keys


class Keys(object):

    def __init__(self):
        self.__keys = {}
        self.file_present = os.path.isfile("user_files/keys.ini")
        self.is_valid = self.checkkeys()
        Functions.debug("Keys file present : " + str(self.file_present), 2)
        Functions.debug("Keys valid : " + str(self.is_valid), 2)
        Functions.debug("tsec_key : " + self.__keys["tsec_key"], 2)
        Functions.debug("titlekek_source : " +
                        self.__keys["titlekek_source"], 2)

    def checkkeys(self):
        ret = True
        if(self.file_present):
            file = open('user_files/keys.ini', 'r')
            for line in file:
                key = line.strip().split(' = ')
                self.__keys[key[0]] = key[1]
            for keyname in KEY_HASHES:
                if keyname in self.__keys:
                    Functions.debug("Key Name : " + keyname, 3)
                    Functions.debug("Key : " + self.__keys[keyname], 3)
                    Functions.debug("Hash : " + KEY_HASHES[keyname], 3)
                    compare_result = self.comparehash(
                        self.__keys[keyname], KEY_HASHES[keyname])
                    Functions.debug("Result : " + str(compare_result), 3)
                    if compare_result is not True:
                        Functions.debug("Key " + keyname + " not valid", 1)
                        ret = False
                else:
                    Functions.debug("Key " + keyname + " missing", 1)
                    ret = False
        else:
            Functions.debug("Key file missing", 1)
            ret = False

        return ret

    def comparehash(self, key, hash):
        m = hashlib.sha256()
        try:
            m.update(binascii.unhexlify(key))
        except Exception as e:
            Functions.debug("Invalid key format", 1)
            return False
        Functions.debug("Digest : " + m.hexdigest(), 3)
        if m.hexdigest() == hash.lower():
            return True

        return False


Keys = Keys()
