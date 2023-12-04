#KLASSEN:

#patruus 
class Picture_patruus:
    def __init__(self, name, path ):
        self.__name = name
        self.__path = path

    #GETTER:
    def getName(self):
        return self.__name
    def getPath(self):
        return self.__path
    
    #FUNKTIONEN:
    def inserta(self):
        pass
    

    
#Hintergrund Bild (Tochter)
class Picture(Picture_patruus):
    def __init__(self):
        pass
        
        
#Logo Klasse
class Logo(Picture_patruus):
    def __init__(self):
        self._alphadata = []
        self._pos = [] #automatisch in der mitte?
        self._resize = 100
        self._key = []
        
    #GETTER:    
    def get_alphadata(self):
        return self._alphadata
    def get_pos(self):
        return self._pos
    def get_resize(self):
        return self._resize
    def get_key(self):
        return self._key

    #FUNKTIONEN:
    def gen_alpha(self):
        pass
        
#Video Klasse
class Video(Picture_patruus):
    def __init__(self, name, path):
        super().__init__(name, path)


def main():
    print("Halli Galloi")
    print("Schnorcheln am Abend")
    pass


if __name__ == "__main__":
    main()