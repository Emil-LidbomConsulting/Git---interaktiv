

class Student():
    objects = []
    
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.points = 0
        Student.objects.append(self)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def add_points(self, points):
        self.points += points
            
    def __str__(self):
        return str(self.name + " " + str(self.courses) + str(self.points))
    
        
    
        

