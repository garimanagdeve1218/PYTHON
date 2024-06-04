#Basically a class function is just a function that can be used by the objects of the class:(it's main thing is to give out the information about the class or also modify the information of the class.):

#in the Students.py file:

class Students:
    def __init__(self, name , major , gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False



#in the app.py file:

from Students import Students

student1 = Students("Oscar", "Accounting",3.1)
student2 = Students("Garima","Business",3.8)

print(student2.on_honor_roll())




"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
True

Process finished with exit code 0
