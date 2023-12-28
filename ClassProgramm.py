class Student:
    def __init__(self,phone_number,name,std_id): # First Argument is the pointer of the calss is called self or any other
        self.Phone_number = phone_number
        self.name = name
        self.std_id = std_id
    def display(self): # self is used to access data inside of the class
        return self.Phone_number,self.name,self.std_id
    
r1 = Student(70123323232,"Rajan",2019)

print(r1.Phone_number)
print(r1.name)
print(r1.display())

    