#reading files usinf for loop:

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

#this will print out all the information in the file in this case employees.
