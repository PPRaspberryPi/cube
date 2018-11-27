import time
class LED(object):
    '''
    Einfache LED-Klasse mit (privaten) RGB-Variablen
    '''
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b
    def setR(self,val):
        self.r=val
    def getR(self):
        return self.r
    def setG(self,val):
        self.g=val
    def getG(self):
        return self.g
    def setB(self,val):
        self.b=val
    def getB(self):
        return self.b
    def getAll(self):
        tmp = [self.r,self.g,self.b]
        return tmp
    def incToMax(self, light):
        '''
        1=R, 2=G, 3=B
        :param light:
        :return:
        '''
        if light==1:
            while self.r!=255:
                self.r+=1
                print("Setting red to",self.r)
                time.sleep(0.3)
            print("Done increasing.")
        if light==2:
            while self.g!=255:
                self.g+=1
                print("Setting green to",self.g)
                time.sleep(0.3)
            print("Done increasing.")
        if light==3:
            while self.b!=255:
                self.b+=1
                print("Setting blue to",self.b)
                time.sleep(0.3)
            print("Done increasing.")
    def resetAll(self):
        self.r=self.g=self.b=0
    def maxAll(self):
        self.r=self.g=self.b=255