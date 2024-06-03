#Try/Except :
#how to handle errors:

#if we have a input field which is supposed to be given an integer but the user provided a string instead of integer.So in that case we will get an error but we can handle that error using try-except block:

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter a number: 3
3

Process finished with exit code 0


"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter a number: abcd
Invalid input value!

Process finished with exit code 0




#now even if we have something written in our program that is meant to throw error even if wasn't the input from user we can handle it.
#the exception block will handle it if we write that in try:

value=10/0
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Traceback (most recent call last):
  File "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py", line 374, in <module>
    value=10/0
          ~~^~
ZeroDivisionError: division by zero

Process finished with exit code 1




#error generated because 10/0 is not allowed and thrown an error to avoid this let's write it in try block:
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Invalid input value!

Process finished with exit code 0






#we can even specify the type of error we wanna check with except:
#this is also considered as the best practice in python to check for specific errors:
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Divided by zero

Process finished with exit code 0




#when we remove the value variable now:
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter a number: rf
Invalid input value!

Process finished with exit code 0




#we can also actually store this error in a variable:
try:
    answe=10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input value!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
division by zero

Process finished with exit code 0
