
#import module
import pandas as pd
from klass_courses import Courses
from klass_mediastudent import Mediastudent
from klass_student import Student

"""Import data"""

media_courses, student_results = pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\ObligatoriskaMediaKurser.csv"), names= 
                       ["Course_code","Course_name", "Points"], sep=";"), pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\Studieresultat.csv"), sep=";", names= [i for i in range(18)])
                    
#print(media_courses)
#print(study_results.iloc[0][0:17])

def media_student(student_courses, media_courses):
        if student_courses in media_courses:
            return True 
        return False


def add_courses(pd_df):
    for row in pd_df.iloc:
        Courses(row.Course_code, row.Course_name, row.Points)


def add_students(pd_df):
    for row in pd_df.iloc:
        Mediastudent(row[0])
        
        for i in row[1:17]:
            if str(i) != "nan":
                Mediastudent.objects[-1].add_course(i)
    
    
add_courses(media_courses)
add_students(student_results)

Mediastudent.objects[0].add_points(5)
print(Mediastudent.objects[3])


    

    
#if media_student:
    

