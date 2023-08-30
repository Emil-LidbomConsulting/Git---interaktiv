

class Courses():
    total_points = 0
    
    def __init__(self, code, name, points):
        self.name = name
        self.points = points
        self.code = code
        Courses.total_points += points
    
    def __str__(self):
        return self.code +" "+ self.name +" "+  str(self.points)
    