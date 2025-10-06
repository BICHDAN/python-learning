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
