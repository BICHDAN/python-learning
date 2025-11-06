# Python Programming Assignment: Classes, Inheritance, and Properties
# exercise 1: Classes and Inheritance
class Person:
    school_name = "TCI Academy"
    Total_population = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        Person.Total_population += 1
    @classmethod
    def Total(cls):
        print(f"The total population is {Person.Total_population} persons")
    @property
    def __str__(self):
        return f"First name: {self.first}\nLast name: {self.last}\nAge: {self.age}"
    @property
    def email (self):
        return f"{self.first}_{self.last}@gmail.com"
    @property
    def fullname (self):
        return f"Fullname: {self.first} {self.last}"
    def introduce(self):
        return f"{self.fullname}\n{self.age}\n{ self.email}" 

class Student(Person):
    Student_count = 0
    Student_list = []
    def __init__(self, first, last, age, year, score):
        super().__init__(first, last, age)
        self.year = year
        self.score = score
        Student.Student_count += 1
        Student.Student_list.append(self)
    @classmethod
    def Enrolled (cls):
        print(f"Student count has reached {Student.Student_count} students")
    @classmethod
    def from_string (cls, s):
        import re
        lst = re.split(r'[,=\s]+',s)
        first, last = lst[0], lst[1]
        age, year, score = int(lst[3]), int(lst[5]), int(lst[7]) # after split we receive a list of strings -> change string into int
        return cls(first, last, age, year, score) 
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if 0<= value <= 100:
            self._score = float(value)
        else:
            raise ValueError("score is invalid, please check again!!!")
    @score.deleter
    def score(self):
        print("delete score...")
        del self._score
    @staticmethod    
    def percent_to_gpa():
        pct = [] #create a list to receive results
        for x in Student.Student_list:    #pick up all scores in list Student_list
            scores = (x.score*4)/100      # assign a expression to calculate 
            pct.append(scores)            # use list comprehension to create a list of results for pct
        return pct
    def introduce(self):
        u = (self.score*4)/100
        return super().introduce() + "\n" + str(u)
            
class Teacher(Person):
    def __init__(self, first, last, age, field):
        super().__init__(first, last, age)
        self.field = field

class Cohort(Student):
    def __init__(self, first, last, age, year, score):
        super().__init__(first, last, age, year, score)
        self.student
        

#test results
Person1 = Person("Peter", "Jonathan", 21)
Person2 = Person("Magot", "Rodrigo", 23)
Person.Total()
print(Person2.__str__)
print(Person2.fullname)
print(Person1.introduce())

stu1 = Student("Miniki", "koneki", 23, 2025, 50)
stu2 = Student("Okiji", "Sinaku", 24, 2023, 90)
Student.from_string("First Last,age=19,year=2025,score=88") 
Student.from_string("Johne Home,age=20,year=2023,score=90") 
Student.Enrolled()
print(Student.percent_to_gpa())
print(stu1.introduce())