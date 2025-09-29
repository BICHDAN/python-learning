#note the information before print
print("think")
print("do")

#calculation1 
x = 12
y = 250
result = x+y+(((y-x)*5)/2)+y*4
print(result)

#calculation2
k = 192939
m = 93904
result2 = k+m+((k/m)+(k*2-m*2))-((k+k+m-m-k)-(k+m/3))
print(result2)

#calculation3
t=234
d=343
f=890
l=999
end=t+d/2+((t+l+f/3)+(f*3+l))
print(end)

#practise pint only
print("thing")
#practise calculator only
hi = "anh"
hu = "em"
ha = hi+hu 
print(ha)

#test data type
a = 2
b = -5.3
c = "hmm"
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#practise decimal
from decimal import*
getcontext().prec=30

l=Decimal("4.989")
u=Decimal("8.9493")
lu=l+u
print(lu)
print(type(lu))

#Practise again
print("do u mind if I")
from decimal import Decimal, getcontext
getcontext().prec=78
DE1=Decimal("9.33223")
DE2=Decimal("9.77777")
DE3=(DE1+DE2)/2
print(DE3)
print(type(DE3))


#fraction practise
from fractions import Fraction
#Using fraction to calculate
frac1=Fraction(8,8)
frac2=Fraction(35/95)
print(frac1)
print(frac2)
print(type(frac1), type(frac2))

#complex practise
com = complex(2,5)
print(com)

#string practise
str1 = "落ち着く"
str2 = "I`m in and out!"
print(str1)
print(str2)
print(type(str1), type(str2))

#String as a comment
"""comment"""
'''comment anything u want'''

#String using """ string """
str3 = """I'm the robot\nNo\nI'm a 会社員"""
print(str3)

#String using Escape sequence
str4 = "\a"
print(str4)
print("erty\be")
print("line1\nline2")
print("doing1\tdoing2")
print("I\\the flower")
print("hello1234")

#practise Escape sequence
print("hi\"on and on")
print("okey\nfine\nok")
print("jk\tjk2")
print("kiki\bUi\'button\nhmmoak\tlaugh\a")

#Raw String
print(r"hello omygod okay\Fineor")
print(R"cat and dog\ they* are not friend")

#String Concatenation Operator 
conca1="pig\n"
conca2="cereal\n"
print(conca1+" "+conca2)

#String repetition Operator
print(conca1*2+"\n"+conca2*4)

#Membership Operator (in) to check if element is included in string or not
print("app" in "application")
print("banana" in "apple pie")
print("oh" in "ohmygod")

#string Comparision Operator
print("ohwow"=="ohwow")
print("100"<"200")
print("250"!="450")

#Indexing
fruit=["apple", "banana", "watermelon", "cherry", "orange"]
print(fruit[2])
print(fruit[4])

pencil=["red color", "blue color", "black color", "white color", "green color"]
print(pencil[2])
print(pencil[3])

str5="How are you?"
print(str5[3])

#practise combine in and indexing (len and slicing)
anw = "Do and Don't"
anw2 = anw[4]
print(anw2 in anw)
print(len(anw))
print(len(pencil))
print(len(str5))

#slicing
print(anw[0:5])
print(fruit[2:4])
print(pencil[1:4])
print(anw[0:])

#slicing2
uni = "hupipa and hepabu"
print(uni[7::-2])
print(uni[0:8:1])
print(uni[0::3])

ok1 = "HelloMyBestie"
ok2 = ok1[:5:-1]
ok3 = ok2 in ok1
print(ok2)


#Practise 
hun, hue, mai, tina=1/2, -2.5, 3+2j, ["orange", "banana", "cake", "sugar"]
print(hun, hue, mai, tina)
'''combine fractise'''
print(Decimal("0.1")+Decimal("-1.2"))
print(Fraction(6,9)/Fraction(2,3)*Fraction(4/3)/complex(2,5))
print(type(tina), type(hue), hue*2, tina*3)
print(len(tina))

#type casting practise 
#original string
ain = "4.5"
ain1 = "100"
ain2 = "1010"
#change string -> numeric
ain3 = float("4.5")
ain4 = int("100")+230
ain5 = int("1010",2)
print(type(ain), type(ain1),type(ain2), type(ain3), type(ain4), type(ain5))
print(ain, ain1, ain2, ain3, ain4, ain5)
#change numeric -> string
ain6 = str(123)
ain7 = str(2.34)
print(type(ain6), type(ain7))
#change between containers
#tuple -> list
ain8 = list((1, 2, 3))
#list -> tuple
ain9 = tuple([4, 5, 6])
print(type(ain8), type(ain9))
#list -> set 
ain10 = set([1,2,3,4,5])
#list of pairs -> dict 

#change selected element of a string into another element
#ok1 = "HelloMyBestie"
ok4 = ok1[:2]+ "i" + ok1[3:]
print(ok4)

#String Formatting
ok5 = 'My team is %s' %('okay and earns a lot of meme')

ok6 = 'My team is {}'
format('okay and earns a lot of meme')
name2 = 'okay and earns a lot of meme'
ok7 = f'My team is {name2}'
print(ok5, ok6, ok7) 

#string formatting 2

iu = '天気がいいから%sしょう。%s'
assign1 = iu %('散歩しま','そのうえ、アイスクリームを食べましょう。')
print(assign1)
iu2 =  '天気がいいから'
iu3 = f'{iu2},アイスクリームを食べましょう'
print(iu3)

#case1
name3 = "ズオン　ホアイ　ビック　ダン"
address = "三原市"
phone = "0709175"
情報 = f'社員：{name3}\n場所：{address}\n携帯電話：{phone}'
print(情報)

#case2
情報 = f'社員：{{name3}}\n場所：{{address}}\n携帯電話：{phone}'
print(情報)


#format operation

#the value {0} said pick the value from position 0 in the format 
#which is 1
jn = "only one value: {0}\n".format(1, 2)
# The value that has position 1 is 2 in format
jn2 = "only one value: {1}".format(1,2)
print(jn + "\n" + jn2)
#we can actually change the name of the position similar to the one in string
#to have a accurate value.
jn3 = 'ok: {one}, no: {two}'.format(one=163, two=214)
print(jn3+"\n"+jn2)

o = '{:*^50}'.format('the weather is hot today')
oo = '{:*^50}'.format('the weather is hot today')
print( ("$"*3)+('>'*5) + oo + ('<'*5)+("$"*3) )

#practice with format operation
row1 = "+ {:-<6} + {:-^15} + {:->10} +".format('','', '')
row2 = "| {:<6} | {:^15} | {:>10} |".format('ID', 'Ho va Ten', 'Noi sinh')
row3 = "| {:<6} | {:^15} | {:>10} |".format('123', 'BICH DAN', 'Viet Nam')
row4 = "+ {:-<6} + {:-^15} + {:->10} +".format('', '', '')
print(row1 + "\n" + row2 + "\n" + row3 + "\n" + row4)

#capitalize -> only cap the first alphabet of the first word. 
row5 = jn.capitalize()
#Upper -> change lower to uppercase
row6 = jn.upper()
#lower -> change upper to lowercase
row7 = jn.lower()
#swapcase -> change upper case to lower case and opposite
row8 = jn.swapcase()
#tittle -> only cap the first alphabet of words
row9 = jn.title()
print(row5, row6, row7, row8, row9)
#center -> align word in the center 
row10 = jn.center(50, "~")
row11 = jn.center(50)
print(row10 + "\n" + row11)

#encode
ia = "Cause I'm only B" 
ib = ia.encode(encoding='utf-8', errors='strict')
print(ib)

#join
ic = "The episode "
il = ic.join([" ", "1\t", "2\t", "3\t"])
# this means -> space + (ic + 1 big space) + (ic + 2 big space) + (ic + 3 big space)
print(il)

#replace 
ig = ic.replace("The", "The next")
print(ig)
ig2 = ic.replace("e", "E", 2)
print(ig2)


#LIST
#list
lst = [-0.5, 0.5, 1, 0, "okok", 2+2j, 1/2]
lst0 = [-0.3, 0.3, 2, 3, "oh", 3+3j, 2/3]
print(lst+lst0)
lst1 = [2, 3]

#list comprehension
#Type 1
lst2 = [ds for ds in range (34)]
lst3 = [ts for ts in range (29)]
print(lst1, lst2, lst3)

#Type 2
olst = [[a/2, a*2+1, a*4/3] for a in range (2,4)]
lst4 = [[n,n*2, n*4] for n in range (1,6)]
print(lst4, olst)
#another way of Type 2
lst5 = []
for n in range(1,6):
    lst5.append([n, n*2, n*4])
print(lst5)

lst6 = list("SmartTelegram")
print(lst6)
lst7 = list( ) 
lst8 = list( [1, 2, 4] )  
lst9 = list( (4, 5, 6) )    
lst10 = list( "programe" )  
"\n"
print(lst7, lst7, lst8, lst9, lst10)

#list concatenate
lst11 = [2,3,4]
lst11 += ["ok", "apple", "fine"]
print(lst11) 
lst12 = [2,5,6]
lst12.extend(["🌹", "🌺", "🪻", "🌻"])
print(lst12)

lst13 = ["🙂", "😣", "😭", "🥶", "🥵"]
print(lst13*3)

op = lst13[0]
op1 = lst13[2]
op2 = lst13[1:3]
op3 = lst13[::-1]
print(op, op1, op2, op3, sep="\n")

#replace in list 
lst13[2] = "🩵" 
lst13[4] = "😡"
lst13[0] = "😼"
print(lst13)

#Matrix
#Matrix with 4 columns, 3 rows
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(matrix)
print(matrix[2][3])
print(matrix[1][2])

#Note
#should not
u = ["🐖", "🐏", "🐫", "🐘"]
uu = u
uu[1] = "🐶" 
print(uu)
print(u)
#should
u2 = ["🐳", "🐬", "🦐", "🦑"]
ui = list(u2)
ui[2] = "🐷"
print(ui)
print(u2)


#dict 
student = {"Name":"thi mau", "age":"22"}
print(student)
#add new key in dict
student["class"]="A235"
student["weight"]=50
student["height"]="1m60"
student["subjects' scores"] = [{"math":10, "math plus":8}, {"biology":8, "science lab":9}, "Art:5"]
print(student)
print(type(student))

Worker = {"Worker's information": [{"Full name":"Dagota Johnson", "year of birth": 1998},\
{"Full name":"Candy Ken", "year of birth": 1989}, \
{"Full name":"Cristen Woody", "year of birth": 1995}],\
"Job field":["Architecture", "Landscape Architecture", "Construction"]
}
print(Worker["Worker's information"][1]["Full name"])
print(Worker["Worker's information"][0]["year of birth"])
print(Worker["Job field"][2])


#dict 2
cat = {"name" : "kitty blue", "type" : "england long fur cat", "country":"England"}
print(cat)
#add list into a dict
cat["fur's color"] = ["yellow", "blue", "white"]
cat["age"] = 2
cat["weight"] = 10
print(cat)

# print the first value of the dict 
print(cat["fur's color"][0])
print(cat["fur's color"][2])
print(student["subjects' scores"][2])

#delete key or value in dict
del cat["type"]
theResult = cat.pop("name")
print(cat)

#function in dict
print(Worker.keys())
print(Worker.values())
print(Worker.items())


#set comprehension
da = {key : value for key, value in [('Name', 'age'), ('member', 69)]}
print(da)
subject = ["Math", "English", "IT", "Biology"]
score = [6, 8, 6, 9]
report = {subject : score for subject, score in zip(subject, score)}
print(report)

#built-in function
keys = ["名前", "クラス", "生年月日"]
d = dict.fromkeys(keys)
print(d)

e = dict.fromkeys(keys, "なし")
print(e)

#change value of a key in dict
d["名前"] = "検討"
d["クラス"] = 108
print(d)

#add/ reduce the old value 
d["クラス"] = d["クラス"]+1
print(d)
d["名前"] = d["名前"]+"山崎"
print(d)

#dict method
#dict.copy()
d2 = d.copy()
print(d2)
#dict.clear()
d2.clear()
print(d2)
#dict.get(key, default)
print(d.get("名前"))
print(d.get("ok","???"))
print(Worker.get("Job field"))
print(Worker.get("information", "???"))
#dict.items()
print(d.items())
print(Worker.items())
ong = list(d.items())
print(ong[1])
#dict.keys()
print(Worker.keys())
print(d.keys())
#dict.values()
print(Worker.values())
print(d.values())
#dict.pop(key, default)
print(d.pop("名前","???"))
print(d.pop("cator", "???")) 

#dict practice
keys2 = ["The name", "level", "university"]
uni = dict.fromkeys(keys2,"none")

uni["The name"]=["岡村さん", "美咲さん"]
uni["level"]=["N2","N4"]
uni["university"]="University of Architecture "
print(uni)
print(uni.keys())
print(uni.values())
print(uni.get("The name"))
print(uni.get("problem", "???")) 



#Boolean learning 
print(bool(0))
print(bool(29))
print(bool(""))

#if with Boolean 
s = 48
if s < 45: print("s is greater than 45")
if s > 45: print("s is smaller than 45")


r = []
if r: print("there is a value")
else: print("this list is empty")


#Boolean with if, elif, else
rrr = 7
w = 19
if rrr < w : print("rrr is smaller than w")
elif rrr > w : print("rrr is bigger than w")
else : print("rrr is equal to w")

#Boolean with logic operators
print(0 and 12)
print(2 and 2)
print("" or 2)
print(not "")


#Branching Statement
x = 3
if x > 5:
    print("x is bigger than 5")
elif x <9:
    print("x is smaller than 9")
else:
    print("x is nothing at all")
    
age = 17
if age < 18: 
    print("age is eligal")
elif age >= 18:
    print("age is not eligal at all")
else:
    print("can not be identified ")
    
x = 19
if x > 10 and x < 20:
    print("x is greater than 10 but smaller than 20")
elif x <10 or x <= 0:
    print("x is smaller than 10 and maybe = 0 ")
elif x == 19:
    print("x = 19")
else:
    print("another circumstance")
    
Raining = False
if not Raining:
    print("it is not raining at all, Let's play outside")
else :
    print("let'S just stay inside the house")
    
#ternary operator
age=20
status = "大人" if age >= 18 else "子供"
print(status)



#While loop 
e = 1
while e <= 10:
    print(e)
    e = e + 1 
    
while True:
    nameofyou = input("type your name (type 's' if you want to stop):")
    if nameofyou == 's':
        break
    print("hello", nameofyou,"really nice to meet you 🥳")

while True:
    location = input("type your location ( type 's'to stop):")
    if location == 's':
        break
    print("oh my god, you are in",location,"where have you been, dear🥹?\nso you actually in",location,"\n","how do you feel now?🤓")


while True:
    feeling = input("type your feeling(type 's' to stop):")
    if feeling == 's':
        break
    print("so you actually feel",feeling, "right now😶‍🌫️")


while True:
    ageofyou = input("type your age (type's' to stop):")
    if ageofyou == 's':
        break
    print("I know it is impolite to ask your age is", ageofyou, "🥹, but by the ways thanks for letting me know🩵")
    

s = "the word that fly away"
idx = 0 
length = len(s)

while idx <length:
    print(idx, 'stands for', s[idx])
    idx += 1



#For loop 
for i in ["🍌","🍍","🍓","🫐","🥭"]:
    print("buy me a",i)
    
for li in range(2,9):
    print(li,"next")

for le in range(1,19,3):
    print(le,"jump")

kl = "dog"
for uk in kl:
    print(uk)

#learning Function
def say_hello():
    print("hello and xin chao")
    print("ok, nice to meet you")

for i in range(3):
    say_hello()


def lottery_ticket():
    return "please bye a lottery ticket\n then check the range of numbers\n"

print(lottery_ticket() * 3)

def greet(name) : 
    print("Hello honey", name)
greet("Nam") 

def age_asking (age):
    print("oh how old are you bae?\nyou are" ,age,
".really, you look so young with that age!" )

age_asking(27)

def location_asking (location):
    print("So can I ask you one more question\n"
,"where do you live? I'm from Okinawa, and you are?\n",
"nice!you are living in",location,"now")

location_asking("Mihara")

def calculate(a, b):
    return a+b

print(calculate(10, 29))

def Date_of_birth(date = []):
    date. append("F")
    print(date)

Date_of_birth()
Date_of_birth()

#the long method
def Food(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print("end",d)
lstn = ["popcorn", "black bean sweet soup", "chicken rice", "fry seafood pancake"]
Food(lstn[0], lstn[1], lstn[2], lstn[3])

#the upadte method
def Drink(g,h,i,j):
    print(g, "\n",h,"\n",i,)
    print("and the last one is",j)
list1 = ["soda", "lemond water", "matcha latte", "mango ice yogust"]
Drink(*list1)


def animal(w, x, y, *, j="elephant"):
    print(w, x, y, j)
    print(r)

list2 = ["lion", "rabbit", "mouse"]
animal(*list2, j="hourse")

def crown(*kings):
    print(kings)
    print(type(kings))
crown(*(x for x in range(39))) #unpack then pack 

def online(a,b):
    print(a)
    print(b)
dic = {"name":"juuwon", "age":23}
online(*dic)

def keo(**kwargs):
    for key, value in kwargs.items():
        print(key, '->', value)
        
keo(name='Calem', location='USA')

def fruit_list(**fruits):
    for key,value in fruits.items():
        print(key, ":", value) 
fruit_list(types = ["banana", "waterlemon", "apple"], 
date_of_expire=["2025/09/09", "2025/09/08","2025/09/18"])

#global and local 
def make_global():
    global x 
    x = 1
    
def local():
    x = 5
    print('x in local', x)
    
make_global()
print(x)
local()
print(x)

def change_number(l):
    l = l+9
    print("Inside function:", l)
v = 2
change_number(v)
print("Outside function:", v)

def add_item(mylist):
    mylist.append("apple")
    print("inside:", mylist)
fruits = ["banana"]
add_item(fruits)
print("outside:", fruits)


#return in funtion 
def cal_rec_per(width, height):
    per = (width+height)*2
    return per
rec_1_width = 5
rec_1_height = 7
#create a varibale to recevie the result:
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)

#this case is when you think you don't need to reused it at all:
print(cal_rec_per(7,4))

def return_ter_func():
    print("this sentence can be read")
    return 
    print("this sentence can not be read")
none1 = return_ter_func()
print(type(none1))

def  cal_rec_area_per(width, height):
    perimeter = (width + height)*2
    area = width * height
    return perimeter, area
rec_width = 9
rec_height = 6
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)
print(rec_per, rec_area)

#Lambda
okj = lambda a, b, c: ((a+b-c)*3)/2
print(okj(1,38,9))
#defaut argument
okh = lambda a, y = 9: a * y
print(okh(2))
#using local and global variables in Lambda
def DTeam():
    member = lambda x: "from now on " + x + " is DTeam's member, please give an applause!"
    return member # return a anonymous function
call_member = DTeam() # assign a variable to recevie DTeam's variable
print (call_member("Little Owl"))
print (call_member("FunnyBunny"))

Dteam_list = [lambda x:x**2, lambda x:x**3, lambda x:x**4]
print(Dteam_list[1](2))
print(Dteam_list[0](3))

#Using Loop in lambda
Dteam_list2 = [lambda y:y*2, lambda y:y*3, lambda y:y*4]
for okin in Dteam_list2:
    print(okin(4))

#Map () function
inue = [3, 4, 5, 1]
theend = map(lambda x : (x+2)/2, inue)
print(list(theend))

oij = [3, 5, 9, 20]
ketka = map(lambda y:(y/3)*2, oij)
print(list(ketka))

express = lambda x, y: (x*y)-(x+y)
o1 = [2, 3, 4, 5]
o2 = [6, 7, 8, 9]
o3 = map(express, o1, o2)
print (list(o3))

#filter function
func1 = lambda x: x>0
oj = [2, -1, 3, 0, -3, 5]
oj2 = filter (func1, oj)
print(list(oj2))
#similar way to filter function:
func1 = lambda x: x>0
oj = [2, -1, 3, 0, -3, 5]
print([x for x in oj if x>0])

#reduce functool
from functools import reduce
num = [2, 3, 4, 5]
output = reduce(lambda x,y: x + y, num)
print(output)
