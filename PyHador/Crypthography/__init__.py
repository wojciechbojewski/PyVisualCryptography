from PIL import Image
from random import randint, choice
import PyHador.Files

class BitmapCryptography:

    def __white(self):
        return (255,255,255)

    def __black(self):
        return (0,0,0)

    def __init__(self, f):
        self.__f = f
        #print(f.dirname + "/" + f.filename + f.extension)
        self.__img = Image.open(f.dirname + "/" + f.filename + f.extension)
        self.__pixels = self.__img.load()
        self.__x, self.__y = self.__img.size[0], self.__img.size[1]
        self.__img1 = Image.new("RGB", (self.__x*2, self.__y*2)) 
        self.__pixels1 = self.__img1.load() 
        self.__img2 = Image.new("RGB", (self.__x*2, self.__y*2)) 
        self.__pixels2 = self.__img2.load() 
        self.__img3 = Image.new("RGB", (self.__x*2, self.__y*2)) 
        self.__pixels3 = self.__img3.load() 
        for i in range(self.__x):    
            for j in range(self.__y):
                if self.__pixels[i, j] == self.__black():
                    mode = choice([1,2,3,4,5,6])
                    if mode == 1: 
                        self.__BlackPixels((i,j),(1,0,0,0))
                    elif mode == 2:
                        self.__BlackPixels((i,j),(0,1,1,0))
                    elif mode == 3:
                        self.__BlackPixels((i,j),(1,1,1,1))
                    elif mode == 4:
                        self.__BlackPixels((i,j),(0,0,1,0))
                    elif mode == 5:
                        self.__BlackPixels((i,j),(1,0,0,1))
                    elif mode == 6:
                        self.__BlackPixels((i,j),(0,1,0,1))
                    else:
                        pass
                else:
                    self.__WhitePixels((i,j),(1,1,1,1))

        for i in range(self.__x*2):    
            for j in range(self.__y*2):
                if self.__pixels1[i,j] == self.__black() or self.__pixels2[i,j] == self.__black():
                    self.__pixels3[i,j] = self.__black()
                else:
                    self.__pixels3[i,j] = self.__white()
    def Save(self):
        self.__img1.save(self.__f.dirname + "/" + self.__f.filename + "_1" + self.__f.extension)
        self.__img2.save(self.__f.dirname + "/" + self.__f.filename + "_2" + self.__f.extension)
        self.__img3.save(self.__f.dirname + "/" + self.__f.filename + "_3" + self.__f.extension)


    def __BlackPixels(self, (i,j),(p11, p12, p21, p22)) :
        if p11 == 1:
            self.__pixels1[2*i,2*j] = self.__black()
            self.__pixels2[2*i,2*j] = self.__white()
        else:
            self.__pixels1[2*i,2*j] = self.__white()
            self.__pixels2[2*i,2*j] = self.__black()
        if p12 == 1:
            self.__pixels1[2*i,2*j+1] = self.__black()
            self.__pixels2[2*i,2*j+1] = self.__white()
        else:
            self.__pixels1[2*i,2*j+1] = self.__white()
            self.__pixels2[2*i,2*j+1] = self.__black()
        if p21 == 1:
            self.__pixels1[2*i+1,2*j] = self.__black()
            self.__pixels2[2*i+1,2*j] = self.__white()
        else:
            self.__pixels1[2*i+1,2*j] = self.__white()
            self.__pixels2[2*i+1,2*j] = self.__black()
        if p22 == 1:
            self.__pixels1[2*i+1,2*j+1] = self.__black()
            self.__pixels2[2*i+1,2*j+1] = self.__white()
        else:
            self.__pixels1[2*i+1,2*j+1] = self.__white()
            self.__pixels2[2*i+1,2*j+1] = self.__black()

    def __WhitePixels(self,(i,j),(p11, p12, p21, p22)) :
        if p11 == 1:
            self.__pixels1[2*i,2*j] = choice([self.__black(), self.__white()])
            if self.__pixels1[2*i,2*j] == self.__black():
                self.__pixels2[2*i,2*j] = choice([self.__white(), self.__black()])
            else:
                self.__pixels2[2*i,2*j] = choice([self.__white(), self.__black()])
                
        if p12 == 1:
            self.__pixels1[2*i,2*j+1] = choice([self.__black(), self.__white()])
            if self.__pixels1[2*i,2*j+1] == self.__black():
                self.__pixels2[2*i,2*j+1] = choice([self.__white(), self.__black()])
            else:
                self.__pixels2[2*i,2*j+1] = choice([self.__white(), self.__black()])
        if p21 == 1:
            self.__pixels1[2*i+1,2*j] = choice([self.__black(), self.__white()])
            if self.__pixels1[2*i+1,2*j] == self.__black():
                self.__pixels2[2*i+1,2*j] = choice([self.__white(), self.__black()])
            else:
                self.__pixels2[2*i+1,2*j] = choice([self.__white(), self.__black()])
        if p22 == 1:
            self.__pixels1[2*i+1,2*j+1] = choice([self.__black(), self.__white()])
            if self.__pixels1[2*i+1,2*j+1] == self.__black():
                self.__pixels2[2*i+1,2*j+1] = choice([self.__white(), self.__black()])
            else:
                self.__pixels2[2*i+1,2*j+1] = choice([self.__white(), self.__black()])





