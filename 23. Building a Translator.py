#to build basic translator in python:

#let's say the language is Giraffe Language
# where whenever vowels apper change it to a g.

def translate(phrase):
    translation =""
    for letter in phrase:

        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter a phrase: hello
hgllg

Process finished with exit code 0




#better version of the same program:

def translate(phrase):
    translation =""
    for letter in phrase:

        if letter.lower() in "aeiou":       #now you don't have to give AEIOU in the string.
            if letter.isupper():
                translation = translation + "G"    #now for capital AEIOU we will get capital G.
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter a phrase: On
Gn

Process finished with exit code 0
