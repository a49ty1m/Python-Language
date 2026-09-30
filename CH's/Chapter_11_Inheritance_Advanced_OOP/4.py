class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    
    def __add__(self, c2):
        return complex(self.r + c2.r , self.i + c2.i)
    
    def __mul__(self, c2):
        return complex(self.r * c2.r - self.i * c2.i, self.r * c2.i + self.i * c2.r)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
    
    
    # # Ugly way without __str__:
    # print(f"{result.r} + {result.i}i")
    #this will print the adress of the object if __str__ is not defined

    # # Clean way with __str__:
    # print(result)  # Automatically calls __str__()
    
c1=complex(4,8)
c2=complex(6,16)
print(c1+c2)
print(c1*c2)