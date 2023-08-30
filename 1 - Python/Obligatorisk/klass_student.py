

class Student():
    
    def __init__(self, name, courses = [], points = 0, percentage = 0.0):
        self.name = name
        self.courses = courses
        self.points = points
        self.percentage = percentage
    
    def add_points(self, points):
        self.points += points
            
    def __str__(self):
        return self.name + " Andel avklarade: " + str(self.percentage)
    
        
    
        

