class Test:
    def prt(self):
        print self
        print(self.__class__)

t = Test()
t.prt()
#Self stands for an instance of the class , represents the address of the current object, and self.class points to the class.