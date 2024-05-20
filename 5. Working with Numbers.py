#working with numbers:


#we can use parenthesis to specify the order of the operations:
print(3 * 6)
print(3 * 6 + 10)
print(3 * (6 + 10) )

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
18
28
48

Process finished with exit code 0



#modulus operator: IT DIVIDES AND THEN SPIT OUTS THE REMAINDER-
print(9 % 2)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
1

Process finished with exit code 0


#storing numbers inside of variables:
num = 5
print(num)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
5

Process finished with exit code 0



#to convert a number into a string:
num = 5
print(str(num))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
5

Process finished with exit code 0


#TO print a number along with a string:
num = 12
print(str(num) + " : this is my fav number!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
12 : this is my fav number!

Process finished with exit code 0

#if we didn't do this above conversion of number into string then there would have been an ERROR:
num = 12
print(num + " : this is my fav number!")

Traceback (most recent call last):
  File "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py", line 77, in <module>
    print(num + " : this is my fav number!")
          ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Process finished with exit code 1



#MATH FUNCTIONS ON NUMBERS:

#abs() function: IT GIVES THE ABSOLUTE VALUE OF ANY NUMBER-
num = -12
print(abs(num))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
12

Process finished with exit code 0


#pow() function: IT TAKES TWO VALUES AND GIVES THE POWER OF NUMBER AS ANSWER:
print(pow(2,3))


num = 12
print(pow(num , 2))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
8
144

Process finished with exit code 0



#max() function: IT TAKES VALUES AND TELLS WHICH NUMBER IS THE HIGHER / MAXIMUM:
print(max(2,3,9))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
9

Process finished with exit code 0


#min() function: JUST LIKE MAX IT GIVES THE MINIMUM:
print(min(2,3,9))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
2

Process finished with exit code 0


#round() function: IT ROUNDS OF THE VALUE
print(round(2.3))
print(round(2.9))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
2
3

Process finished with exit code 0


#functions that we can use after importing math:
from math import *

#there are the basic math functions. There are many others than this.

#floor() function: IT CHOPS OFF THE DECIMAL PART-
print(floor(2.9))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
2

Process finished with exit code 0



#ceil() function: IT IS THE EXACT OPPOSITE OF THE FLOOR THAT MEANS IT WILL ROUND THE NUMBER UP NO MATTER WHAT- 
print(ceil(2.9))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
3

Process finished with exit code 0



#sqrt() function: IT PRINTS THE SQUARE ROOT OF THE NUMBER-
print(sqrt(36))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
6.0

Process finished with exit code 0












