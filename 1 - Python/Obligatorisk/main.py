
#import module
import pandas as pd
from klass_courses import Courses
from klass_mediastudent import Mediastudent
from klass_student import Student


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8'") as file:
        temp_list = []
        for row in file:
            temp_list.append(list_filter(row.strip().split(";")))
        return temp_list


def list_filter(list):
    while "" in list:
        list.remove("")
    return list

def media_student(student_courses, media_courses):
        if student_courses in media_courses:
            return True 
        return False


def add_courses(course_list):
    temp_list = []
    for list in course_list:
        temp_list.append(Courses(list[0], list[1], float(list[2])))
    return temp_list

def add_media_students(student_list, course_list, total_points):
    temp_list = []
    for list in student_list:
        if len(list) > 1:
            points = calc_points(list[1:17], course_list)
            percentage = calc_percentage(points, total_points)
            temp_list.append(Mediastudent(list[0], list[1:17], points, percentage))
        else:
            temp_list.append(Mediastudent(list[0]))
    return temp_list


def calc_percentage(points, total_points):
    percentage = points / total_points
    return round(percentage*100)
    

def calc_points(taken_course_list, course_list):
    points = 0
    for course in taken_course_list:
        points += (find_points(course, course_list))
    return points
        
        
def find_points(sought_code, course_list):
        for course in course_list:
            if course.code == sought_code:
                return course.points
        return 0
    
 
def print_objects(object_list):
    for i in object_list:
        print(i)

        
            
"""Import data"""    


def main():
    
    course_list = read_file(r"Git---interaktiv\1 - Python\Obligatorisk\ObligatoriskaMediaKurser.csv")
    student_list = read_file(r"Git---interaktiv\1 - Python\Obligatorisk\Studieresultat.csv")
        
    course_objects = add_courses(course_list)
    student_objects = add_media_students(student_list, course_objects, Courses.total_points)

    print("Alla obligatoriska kurser:")
    print_objects(course_objects)
    print("Total obligatorisk poängsumma: " + str(Courses.total_points))
    print("\nAlla studenter:")
    print_objects(student_objects)


main()
    
    

