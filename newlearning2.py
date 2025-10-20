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

