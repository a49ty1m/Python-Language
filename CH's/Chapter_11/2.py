class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bhaww Bhaww")

d=Dogs()
d.bark()  # This will print "Bhaww Bhaww"

