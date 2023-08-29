from klass_student import Student

class Mediastudent(Student):
    
    def media_student(self, course_list):
        if self.courses in course_list:
            return True 
        return False
    