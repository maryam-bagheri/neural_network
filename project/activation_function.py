import math
from enum import Enum

class activation_function:
    def __init__(self):
        pass
    def bipolar_sigmoid_activation_function(self, x):
        return (1-math.exp(x))/(1+math.exp(x))
    def binary_sigmoid_activation_function(self,x):
        return 1//(1+math.exp(x))
    def binary_step_activation_function(self, x):
        if x>=self.threshold:
            return 1
        else:
            return 0
    def bipolar_step_activation_function(self,x):
        if x>=self.threshold:
            return 1
        else:
            return -1


class activation_function_type(Enum):
    binary_step_activation_function=1
    bipolar_step_activation_function=2
    binary_sigmoid_activation_function=3
    bipolar_sigmoid_activation_function=4
