#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
      
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if (isinstance(size, int)):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self, condition = "New"):
        self.condition = condition

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        if condition == "New":
            self._condition = condition
            return print("Your shoe is as good as new!")
    
    condition = property(get_condition, set_condition)