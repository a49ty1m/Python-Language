class twoD_vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"twoD_vector initialized with {self.x}x + {self.y}y")
        
class threeD_vector(twoD_vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call the constructor of the parent class (twoD_vector)
        self.z = z  # Initialize the z coordinate for the 3D vector
        print(f"threeD_vector initialized with {self.x}x + {self.y}y + {self.z}z")
    
a= twoD_vector(1, 2)  # Create a 2D vector with x=1, y=2
b= threeD_vector(3, 4, 5)  # Create a 3D vector with x=3, y=4, z=5