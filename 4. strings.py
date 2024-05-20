#how to write a string.
print("this is how you write a string")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
this is how you write a string

Process finished with exit code 0



#or
print("this\nis how\nyou write a string.")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
this
is how
you write a string.

Process finished with exit code 0



#put quotation mark inside a string.
print("this is how you \"write\" a string.")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
this is how you "write" a 

Process finished with exit code 0



#string with variables:
phrase=("My name is Garima Nagdeve.")
print(phrase)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
this is how you "write" a 



#concatination: Appending one with to another string.
phrase="My name is "
print(phrase + "Garima.")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
My name is Garima.

Process finished with exit code 0


#using functions on string:

#lower() function:
phrase="MY NAME IS GARIMA. "
print(phrase.lower())

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
my name is garima. 

Process finished with exit code 0

#upper() function:
phrase="my name is garima"
print(phrase.upper())

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
MY NAME IS GARIMA

Process finished with exit code 0

#to check if the string is in upper case:
phrase="my name is garima"
print(phrase.isupper())

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
False

Process finished with exit code 0

#to check if the string is in lower:
phrase="my name is garima"
print(phrase.islower())

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
True


#to get the length of the string: output will be the number of characters inside the string-
phrase="my name is garima"
print(len(phrase))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
17

Process finished with exit code 0


#to print a centrain character in the string:
phrase="My name is Garima"
print(phrase[0])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
M

Process finished with exit code 0


#index function: IT WILL TELL WHERE A SPECIFIC CHARACTER OR STRING IS LOCATED IN THE STRING-
phrase="My name is Garima"
print(phrase.index("G"))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
11

Process finished with exit code 0

#we can also put string in there : IT WILL TELL THE INDEX WHERE THE STRING IS STARTING-
phrase="My name is Garima"
print(phrase.index("Gari"))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
11


#replace() function: IT TAKES TWO PARAMETERS-
phrase="My name is Garima"
print(phrase.replace("Garima","Doll"))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
My name is Doll

Process finished with exit code 0


#the above functions were some most basic functions to use with strings in python.







