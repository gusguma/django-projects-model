from typing import Any


class Person(object):

    __name = ""
    __surname = ""

    def __init__(self,name,surname):
        self.__name = name
        self.__surname = surname

    def get_nombre(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname
