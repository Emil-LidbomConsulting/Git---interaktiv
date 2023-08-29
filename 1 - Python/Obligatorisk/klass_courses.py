

class Courses():
    objects = []
    
    def __init__(self, code, name, points):
        self.name = name
        self.points = points
        Courses.objects.append(self)
    