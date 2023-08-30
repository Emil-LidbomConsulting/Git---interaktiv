import unittest


class Student():
    
    def __init__(self, name, courses = [], points = 0, percentage = 0.0):
        """Konstruktor där standardvärden tilldelas om studenten i fråga ej har studerat

        Args:
            name (string): Name of student.
            courses (list): Courses the student has completed.
            points (int): Number of points courses equals to. Defaults to 0.
            percentage (float): Percentage of mandatory course points completed. Defaults to 0.0.
        """
        self.name = name
        self.courses = courses
        self.points = points
        self.percentage = percentage
    
            
    def __str__(self):
        """
        Standard method for printing information for object. 
        Returns:
            _type_: string
        """
        return self.name + " Andel avklarade:   " + str(self.percentage) + "%"


class TestKontakt(unittest.TestCase):

    def setUp(self):
        """Creates object of the class to be used in testing"""
        self.object = Student("Bella", ["DM222"], 40, 80)
        
    def tearDown(self):
        pass #  här kan man välja att "städa upp" efter setUp om det behövs

    def test_attribute_values(self):
        """Control if the object attributes have been given their values correctly"""
        self.assertEqual(self.object.points, 40)     # True
        self.assertEqual(self.object.percentage, 80)     # True
        self.assertEqual(self.object.name, "Bella")     # True
    
    def test_printout(self):
        self.assertEqual(self.object.__str__(), "Bella Andel avklarade: 80")     # True
        
        

if __name__ == '__main__':
    unittest.main()