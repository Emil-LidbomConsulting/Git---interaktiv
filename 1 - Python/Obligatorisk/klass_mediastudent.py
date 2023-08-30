from klass_student import Student
import unittest


class Mediastudent(Student):
    pass


class TestKontakt(unittest.TestCase):

    def setUp(self):
        """Creates object of the class to be used in testing"""
        self.object = Mediastudent("Bella", ["DM222"], 40, 80)
        
    def tearDown(self):
        pass #  här kan man välja att "städa upp" efter setUp om det behövs

    def test_attribute_values(self):
        """Control if the object attributes have been given their values correctly and that all methods in super class has been inherited"""
        self.assertEqual(self.object.points, 40)     # True
        self.assertEqual(self.object.percentage, 80)     # True
        self.assertEqual(self.object.name, "Bella")     # True
    
    def test_printout(self):
        self.assertEqual(self.object.__str__(), "Bella Andel avklarade: 80")     # True
        
        

if __name__ == '__main__':
    unittest.main()