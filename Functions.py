#functions in python:

def sayhi():
    print("Hello User")
sayhi()

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Hello User

Process finished with exit code 0

#understand the execution:

def sayhi():
    print("Hello User")
print("Top")
sayhi()
print("Bottom")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Top
Hello User
Bottom 

#giving the functions parameters:

def say_hi(name):
    print("Hello User")
say_hi("Mike")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Hello User

Process finished with exit code 0

#we can also do this:

def say_hi(name):
    print("Hello " + name)
say_hi("Mike")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Hello Mike

Process finished with exit code 0



#we can also do this:

def say_hi(name):
    print("Hello " + name)
say_hi("Mike")
say_hi("Steve")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Hello Mike
Hello Steve

Process finished with exit code 0



#we can even pass more than one parameter:

def say_hi(name,age):
    print("Hello " + name + " you are " + age)
say_hi("Mike","30")
say_hi("Steve","20")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Hello Mike you are 30
Hello Steve you are 20

Process finished with exit code 0
