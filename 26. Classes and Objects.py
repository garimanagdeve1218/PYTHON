#so we have a file name Student.py
class Student:        #this is a class named Student

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation




#classes and objects:
#in other file:
from Student import Student    #this means from file Student.py import the class Student

student1 = Student("Jim", "Business", 3.1 , False)       #this is a object that we creadted by name student1 which actually contains the information of a student.

print(student1.name)   #to access the name of the student1.

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Jim

Process finished with exit code 0

#we can have as many objects as we want.
