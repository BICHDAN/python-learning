#OOP learning 
class superman:
    pass
superman.name = "thunter storm hero"
superman.color = "yellow and black"
superman.sexual = "woman" 

print("superman name is",superman.name)
print("the color of superman's cloth is", superman.color)
print("superman is a", superman.sexual)

#create class
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        pass
    def bark(self):
        print(f"{self.name} say Woof!")

dog1 = Dog("Lucky", "white")
print(dog1.name)
dog1.bark()

class Cat:
    def __init__(self, name, characteristic, color):
        self.name = name
        self.characteristic = characteristic
        self.color = color
        pass
    def growl(self):
        print(f"{self.name}はいつも'Moewn Moewn'となっています。悲しいなぁ。。。")

cat1 = Cat("Layla", "negative", "black and yellow")
print (cat1.name, "\n", cat1.characteristic)
cat1.growl()

class student:
    def __init__(self, name, age, hobby):
        self.name = name 
        self.age = age
        self.hobby = hobby
        pass
    def Yelling(self):
        print(f"{self.name} attended, teacher!")

student1 = student("John","18", "play video game")
print(student1.name, student1.age)
student1.Yelling()

#attribute of class
class PowerRanger:
    STT = 1
    so_thu_tu = 1
    power = "50%"
    
    def __init__(self, name, weapon, color ):
        self.name = "Power Ranger " + name
        self.weapon = "Power Ranger " + name + "is using "+ weapon
        self.color = color
        
        self.STT = PowerRanger.so_thu_tu
        
        PowerRanger.so_thu_tu += 1 
        
PowerRangerA = PowerRanger("Thunder", "Hammer", "blue")
PowerRangerB = PowerRanger("Light", "Book", "Yellow")

print(PowerRangerA.STT)
print(PowerRangerB.STT)
print(PowerRanger.so_thu_tu)

class House:
    def __init__(self, color, floors):
        self.color = color
        self.floors = floors

house1 = House("red", 2)
house2 = House("blue", 3)        

# Use method to change attribute
class Army:
    def __init__(self, uniform, age, nickname ):
        self.uniform = uniform
        self.age = age
        self.nickname = nickname
    def Yelling(self):
        print(f"yes sir!, {self.nickname} attended \nGot {self.uniform}, {self.age} years old")
    
    def birthday(self):
        self.age += 1 
        print(f"oh that you!, is today your birthday, congrat you are now {self.age}.")
    
    def reply(self):
        print("Thank you sir\n")
        
    def birthday2(self):
        self.age += 10 
        print(f"oh you lier, you're already {self.age} right.\n Don't be silly, you face is much older than me\n Seem like you can born me for sure! HaHa")
    
    def reply2(self):
        print("Does that look obvious? Sir")
        
Army1 = Army("Swimming Uniform", 20, "BigMouth")
Army2 = Army("Casual Uniform", 21, "GreenTomato")

Army1.Yelling()
Army1.birthday()
Army1.reply()

Army2.Yelling()
Army2.birthday2()
Army2.reply2()

#Class method 
class Members:
    total_members = 0 #shared data of the class
    
    def __init__(self, name):
        self.name = name
        Members.total_members += 1
    @classmethod
    def show_total(cls):
        print(f"Total members: {cls.total_members}")

Member1 = Members("Alice")
Member2 = Members("Johnson")
Member3 = Members("Dagota")
Member4 = Members("Okinawa")
Member5 = Members("Bich Dan")

Members.show_total()

# create a special object with class method 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_string(cls, text):
        name, age = text.split("-") # split the string"Alice-20" into ["Alice","20"]
        return cls(name, int(age)) # after using split, Python will turn 20 into "20" 
    #which is a string -> use int(age)to change the variable string into integer again 
    
s1 = Student.from_string("Alice-20")
print(s1.name, s1.age) # Alice 20
    

class Flower:
    def __init__(self, name, types, color):
        self.name = name
        self.types = types
        self.color = color
    @classmethod
    def from_string(cls, s): #from method
        lst = s.split('-') # split string by '-' EX: ok-ik --> "ok","ik"
        new_lst = [st.strip() for st in lst] #st.strip()is for delete, 
        #unnessary space before and after a string after split,
        #st is a temporary variable, you can change it into ok/ki/oj/v.v
        name, types, color = new_lst #to assign name, types, color along with the vararibles in new_list
        return cls(name, types, color) # use return cls () to create new object

infor_str = "Camilia-garden flower-Red"
FlowerA = Flower.from_string(infor_str)
FlowerB = Flower.from_string("Ogchid-garden flower-Yellow and White")
FlowerC = Flower.from_string("Rose - normal flower - Red and Black")
print(FlowerA.__dict__, "\n", FlowerB.__dict__, "\n", FlowerC.__dict__) # print as a dict

#static method 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    @staticmethod
    def account_number (accountNum) :
        #only approve number that contain 10 numbers
        return len(str(accountNum)) == 10 and str(accountNum).isdigit()
    
print (BankAccount.account_number(1298374751))
print(BankAccount.account_number("d9883949993"))

#Inheritance in OOP

#parent class
class Animal:
    def speak(self):
        print("Animal is making sound")

#child class
class dog (Animal):
    def bark (self):
        print("wow wow!")

犬 = dog()
犬.speak()
犬.bark()

#Method Overriding:
class Parents:
    def Punish (self):
        print("you will be grounded for 2 weeks with no phone!")
class Child(Parents):
    def Punish (self):
        print("you will be grounded for 2 days with no phone")

FirstChild = Child()
FirstChild.Punish()

#expand method
class Child2(Parents):
    def Punish(self):
        super().Punish()
        print("no need")
SeChild = Child2()
SeChild.Punish()


#exercise 1:　（ビックダン）
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdrawn (self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insuddicient funds")
    def show_balance(self):
        print(f"balance = {self.balance}")

a1 = BankAccount("Taro", 1000)
a1.deposit(500)
a1.withdrawn(2000)
a1.withdrawn(800)
a1.show_balance()

#exercise 2: （ビックダン）
class Member:
    total = 0
    def __init__(self, name):
        self.name = name
        Member.total += 1 #Member.total is a class attribute 
        #-> init create a object will in crease total.
        # -> if put in method -> Only update total 1 time  
    @classmethod
    def show_total(cls):
        print(f"Total members: {Member.total}")
m1 = Member("Aki")
m2 = Member("Sora")
Member.show_total()

#exercise 3: Inheritance and Method Overriding:(ビックダン)
class Animal:
    def speak (self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal()
d = Dog()
a.speak()
d.speak()

#exercise 4: Static Method Example　（ビックダン）
class Converter:
    def __init__(self, amount):
        self.amount = amount
    @staticmethod
    def yen_to_usd (amount):
        return amount / 150
    
print(Converter.yen_to_usd(3000))

#exercise 5: Inheritance and Extended Behavior (ビックダン)
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed 
    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")
class Car (Vehicle):
    def __init__(self, name, speed,fuel):
        super().__init__(name, speed)
        self.fuel = fuel 
    def refuel(self, refuel):
        return self.fuel + refuel 
    
v = Vehicle("Bike", 20)
v.move()

c= Car("Prius", 60, 10)
c.move()
c.refuel(5)
c.move()

#exercise 5: Inheritance and Extended Behavior (ChatGPT)
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def move (self):
        print(f"{self.name} is moving at {self.speed} km/h")
class Car (Vehicle):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel 
    def move(self):
        super().move()
        if self.fuel <= 0:
            print("running out of fuel")
        else:
            print(f"{self.name} is moving at {self.speed} km/h")
            self.fuel -= 2
    def refuel (self, amount):
        self.fuel += amount 

v = Vehicle("Bike", 20)
v.move()

c= Car("Prius", 60, 10)
c.move()
c.refuel(5)
c.move()        
        
#exercise 6: Collaboration between classes (ビックダン)
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
class Classroom():
    def __init__(self):
        self.total_students= []
    def add_students(self, student):
        self.total_students.append(student)
    def average_score(self):
        total = sum(s.score for s in self.total_students)
        return total/len(self.total_students)
c = Classroom()
c.add_students(Student("Taro", 80))
c.add_students(Student("Hanako", 90))
print(c.average_score())

        
#exercise 7: (ビックダン)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
class Library:
    def __init__(self):
        self.Total_pages = []
    def add_book(self,book):
        self.Total_pages.append(book)
    def total_pages(self):
        return sum(b.pages for b in self.Total_pages)
lib = Library()
lib.add_book(Book("the silence of the lambs", 300))
lib.add_book(Book("Yellow flower on the green field", 250))
print(lib.total_pages())

#exercise 7: (Chat GPT)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
class Library:
    def __init__(self):
        self.Total_pages = []
    def add_book(self,book):
        self.Total_pages.append(book)
    def total_pages(self):
        total = 0 
        for x in self.Total_pages:
            total += x.pages
        return total 
lib = Library()
lib.add_book(Book("the silence of the lambs", 300))
lib.add_book(Book("Yellow flower on the green field", 250))
print(lib.total_pages())


#special method
#usual way:
class Student:
    def __init__(self, name, score):
        self.name = name 
        self.score = score
    def score_student(self):
        return(f"{self.name} gains {self.score} scores")
c = Student("Timmy", 89)
print(c.score_student())

#__str__:
class Student:
    def __init__(self, name, score):
        self.name = name 
        self.score = score
    def __str__(self):
        return(f"{self.name} gains {self.score} scores")
c = Student("Timmy", 89)
print(c)
#__add__:
class Student:
    def __init__(self, name, score):
        self.name = name 
        self.score = score 
    def __add__(self, other):
        return self.score + other.score
a = Student("Johnson", 39)
b = Student("Dagota", 90)
print(a + b)

#__len__:
class Classroom:
    def __init__(self):
        self.total = []
        
    def add_student (self,student):
        self.total.append(student)
        
    def __len__(self):
        return len(self.total)
c = Classroom()
c.add_student("Neko")
c.add_student("Miki")
print(len(c)) # python will call __len__ method when typing len(c)

#__eq__:
class Student:
    def __init__(self, name, score):
        self.name = name 
        self.score = score 
    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

s1 = Student("Taro", 80)
s2 = Student("Taro", 80)
s3 = Student("Kenji", 90)

print(s1 == s2)
print(s2 == s3)

#Getter, Setter, Deleter
#Getter:
class Group:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def First_Lastname(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def email(self):
        return self.first_name + self.last_name + "@gmail.com"
    
    @property
    def score (self):
        return self._score 
    
    @score.setter
    def score (self, value):
        if 0 <= value <=100:
            self._score = value
        else:
            print("invalid score!!!")
    @score.deleter
    def score(self):
        print("Deleting score...")
        del self._score
o = Group("John", "Dagota")
print(o.first_name)
print(o.last_name)
print(o.email)
print(o.First_Lastname)
o.score = 90
o.score = 110
print(o.score)

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
            
class Teacher(Person):
    def __init__(self, first, last, age, field):
        super().__init__(first, last, age)
        self.field = field

Persion1 = Person("Peter", "Jonathan", 21)
Person2 = Person("Magot", "Rodrigo", 23)
Person.Total()
print(Person2.__str__)

stu1 = Student("Miniki", "koneki", 23, 2025, 50)
stu2 = Student("Okiji", "Sinaku", 24, 2023, 90)
Student.from_string("First Last,age=19,year=2025,score=88") 
Student.from_string("Johne Home,age=20,year=2023,score=90") 
Student.Enrolled()
print(Student.percent_to_gpa())