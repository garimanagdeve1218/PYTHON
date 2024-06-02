#Lists in python:

friends = ["Garima" , "doll" , "kevin"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll', 'kevin']
Garima
doll
kevin

Process finished with exit code 0





#we can even eccess the index of the lists starting from the behind of the list:

friends = ["Garima" , "doll" , "kevin"]
print(friends)
print(friends[-1])
print(friends[-2])
print(friends[-3])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['Garima', 'doll', 'kevin']
kevin
doll
Garima

Process finished with exit code 0




#to print from listusing colan:

friends = ["Garima" , "doll" , "kevin"]
print(friends[1:])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['doll', 'kevin']

Process finished with exit code 0


#to print from listusing colan:

friends = ["Garima" , "doll" , "kevin", "tomy", "jungkook"]
print(friends[1:4])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
['doll', 'kevin', 'tomy']

Process finished with exit code 0



#we can modify values in list :
friends = ["Garima" , "doll" , "kevin", "tomy", "jungkook"]
friends[3] = "V"
print(friends[3])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
V

Process finished with exit code 0

