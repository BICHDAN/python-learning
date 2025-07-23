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

#Membership Operator (in)
print("app" in "application")
print("banana" in "apple pie")

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

