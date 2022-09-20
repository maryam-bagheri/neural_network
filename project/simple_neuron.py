import math
from enum import Enum
if __name__=='__main__':
    print('test')

class neuron:
    w=0
    epoch=1
    def __init__(self) -> None:
        pass    
    def train(self,x,y):
        if len(x)!=len(y):
            print('the length of trian and target aren''nt compatible')
            pass
        for e in range(self.epoch):
            for i,j in zip(x,y):
                #this needs a chage
                ###Hebb way
                self.w=self.w+i*j
    def test(self,x):
        return self.w*x
        