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