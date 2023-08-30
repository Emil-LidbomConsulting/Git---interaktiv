import unittest

class Courses():
    total_points = 0
    
    def __init__(self, code, name, points):
        self.name = name
        self.points = points
        self.code = code
        Courses.total_points += points
    
    def __str__(self):
        return self.code +" "+ self.name +" "+  str(self.points)
    
    @staticmethod
    def return_total_point():
        return Courses.total_points
    

class TestKontakt(unittest.TestCase):

    def setUp(self):
        """Creates object of the class to be used in testing"""
        self.object = Courses("DM123", "Testcourse", 7.5)
        
    def tearDown(self):
        pass #  här kan man välja att "städa upp" efter setUp om det behövs

    def test_attribute_values(self):
        """Control if the object attributes have been given their values correctly and that all methods in super class has been inherited"""
        self.assertEqual(self.object.points, 7.5)     # True
        self.assertEqual(self.object.name, "Testcourse")     # True
        self.assertEqual(self.object.code, "DM123")     # True
    
    def test_printout(self):
        self.assertEqual(self.object.__str__(), "DM123 Testcourse 7.5")     # True
        
        

if __name__ == '__main__':
    unittest.main()