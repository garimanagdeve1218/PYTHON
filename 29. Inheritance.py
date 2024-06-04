#we have a py file named app.py :
#then we got a another py file named Chef.py which contains some functionalites of a Chef with Chef class:
#then we got one more py file ChineseChef.py which conatains all the functionalities of a Chef and may be few more of own:

#instead of copying everything from Chef class and pasting to ChineseChef class we can inherit ChineseChef class from Chef class:

#Chef.py contains:
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The Chef makes a salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


#ChineseChef.py contains:
#(so to inherit from Chef.py)
from Chef import Chef

class ChineseChef(Chef):     #from this ChineseChef(Chef) function i will be able to use all the function in this ChineseChef class from the Chef class:
    def make_chicken(self):
        print("The chef makes a chicken")
        
    def make_egg(self):
        print("The chef makes egg")
        
    def make_special_dish(self):
        print("the chef makes rasmalai")



#app.py contains:
#(so now if our app.py contains these things):
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()           #making a new chef
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_egg()
myChineseChef.make_special_dish()




"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
The chef makes bbq ribs
The chef makes a chicken
The chef makes egg
the chef makes rasmalai

Process finished with exit code 0
