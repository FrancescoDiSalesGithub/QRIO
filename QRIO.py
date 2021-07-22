import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

import re

class ExtensionException(Exception):
    pass

class FormatException(ExtensionException):
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message


class qrEncoder:

    def __init__(self,content,filename):
        self.__content=content
        self.__filename=filename


    def encode(self,format="png"):

        if self.__checkformat(format) != True:
            raise FormatException("Invalid Extension","Method encode has a wrong extension")

        maker = qrcode.make(self.__content)
        filename_definitive="{}.{}".format(str(self.__filename),str(format))
        maker.save(filename_definitive)

    def __checkformat(self,format):
        rule=re.compile("[a-z]{3}")
        if rule.match(format) == None:
            return False

        return True

    def get_content(self)->str:
        return self.__content

    def set_content(self,value):
        self.__content=str(value)

    def get_filename(self)->str:
        return self.__filename

    def set_filename(self,value):
        self.__filename=str(value)



class qrDecoder:

    def __init__(self,filename):
        self.__filename=filename

    def decode(self):
        return str(decode(Image.open(self.__filename)))


    def get_filename(self)->str:
        return self.__filename

    def set_filename(self,filename):
        self.__filename=filename



