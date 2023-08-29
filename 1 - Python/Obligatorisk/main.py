
#import module
import pandas as pd

"""Import data"""
media_courses, results = pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\ObligatoriskaMediaKurser.csv"), names= 
                       ["Course_code","Course_name", "Points"], sep=";"), pd.read_csv((r"Git---interaktiv\1 - Python\Obligatorisk\Studieresultat.csv"), sep=";", names= [i for i in range(17)])
                    
#print(media_courses)
#print(results)

def media_student(student_courses, media_courses):
        if student_courses in media_courses:
            return True 
        return False

for row in media_courses.iloc:
    print(row.Course_code)
    
#if media_student:
    

