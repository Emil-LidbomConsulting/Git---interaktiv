number  = 1
letter = "a"

if number == letter:
    print("yes")
else:
    print("correct")
    
    
class Testklass:
    def __init__(self, test):
        self.test = test

objekt = Testklass("här står det test")

print(objekt.test)
