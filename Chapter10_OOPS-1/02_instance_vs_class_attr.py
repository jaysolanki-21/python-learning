class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


John = Employee()
John.language = "JavaScript" # This is an instance attribute
print(John.language, John.salary)
 