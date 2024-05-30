#tuples are immutable- can't be changed once made.

coordinates = (4,5)
print (coordinates[1])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
5
Process finished with exit code 0

#tuples can't be modified:

coordinates = (4,5)
coordinates[1] = 10
print(coordinates[1])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Traceback (most recent call last):
  File "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py", line 199, in <module>
    coordinates[1] = 10
    ~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

Process finished with exit code 1






