import os, sys

class File:
    def __init__(self, filename):
        try:
            self.__f = open(filename,'r')
            self.__filename = os.path.splitext(filename)[0]
            self.__dirname = os.path.dirname(self.__f.name)
            if len(self.__dirname)==0:
                self.__dirname = os.path.curdir
            self.__extension = os.path.splitext(filename)[1]
        except:
            pass

    def __getattr__(self, AttributeName):
        try:
            if AttributeName == "filename":
                return self.__filename
            elif AttributeName == "dirname":
                return self.__dirname
            elif AttributeName == "extension":
                return self.__extension
            else:
                return None
        except Exception:
            return None