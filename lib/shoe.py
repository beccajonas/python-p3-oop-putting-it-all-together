#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand

    @property
    def size(self):
        """The size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        # must be integer
        if isinstance(size, int):
            self._size = size
        else:
            print(
                "size must be an integer"
            )
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    


    