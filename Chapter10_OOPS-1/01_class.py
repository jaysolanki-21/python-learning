class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


John = Employee()
John.name = "John" # This is an instance attribute
print(John.name, John.language, John.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class