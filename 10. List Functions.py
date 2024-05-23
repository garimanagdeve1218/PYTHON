#functions in lists:

#extend function:
lucky_numbers = [2 , 3, 4]
friends = ["Garima" , "doll" , "kevin"]
friends.extend(lucky_numbers)
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll', 'kevin', 2, 3, 4]

Process finished with exit code 0




#append function:
friends = ["Garima" , "doll" , "kevin"]
friends.append("Creed")
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll', 'kevin', 'Creed']

Process finished with exit code 0




#insert function():

friends = ["Garima" , "doll" , "kevin"]
friends.insert(1, "Cow")
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'Cow', 'doll', 'kevin']

Process finished with exit code 0




#remove function:

friends = ["Garima" , "doll" , "kevin"]
friends.remove("kevin")
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll']

Process finished with exit code 0




#clear function:

friends = ["Garima" , "doll" , "kevin"]
friends.clear()
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
[]

Process finished with exit code 0




#pop function:

friends = ["Garima" , "doll" , "kevin"]
friends.pop()
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll']

Process finished with exit code 0





#to check if the value existes in the list or not;
#if it returns an index value that means it's in the list:
friends = ["Garima" , "doll" , "kevin"]
print(friends.index("doll"))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
1

Process finished with exit code 0

#if it doesn't return an index value and gives error then it is not in the list:    (using index function)
friends = ["Garima" , "doll" , "kevin"]
print(friends.index("mike"))

Traceback (most recent call last):
  File "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py", line 172, in <module>
    print(friends.index("mike"))
          ^^^^^^^^^^^^^^^^^^^^^
ValueError: 'mike' is not in list

Process finished with exit code 1




#how to count the number of similar elements in the list:    (using count function)

friends = ["doll", "Garima" , "doll" , "kevin", "doll"]
print(friends.count("doll"))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
3

Process finished with exit code 0




#sorting the list:   (this sort() will sort the list in ascending order)

friends = ["doll", "Garima" , "doll" , "kevin", "doll"]
friends.sort()
print(friends)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll', 'doll', 'doll', 'kevin']

Process finished with exit code 0




#reversing the list:    

numbers = [42, 8, 15, 16, 23]
numbers.reverse()
print(numbers)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
[23, 16, 15, 8, 42]

Process finished with exit code 0




#we can also make a copy of a list:     (using copy() we made a copy of friends list)
friends = ["doll", "Garima" , "doll" , "kevin", "doll"]
friends2 = friends.copy()
print(friends2)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['doll', 'Garima', 'doll', 'kevin', 'doll']

Process finished with exit code 0


