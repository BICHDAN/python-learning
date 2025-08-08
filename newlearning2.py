print("do u mind if I")
from decimal import Decimal, getcontext
getcontext().prec=78
DE1=Decimal("9.33223")
DE2=Decimal("9.77777")
DE3=(DE1+DE2)/2
print(DE3)
print(type(DE3))


#fraction
from fractions import Fraction
#Using fraction to calculate
frac1=Fraction(8,8)
frac2=Fraction(35/95)
print(frac1)
print(frac2)
print(type(frac1), type(frac2))

#Raw String
print(r"hello omygod okay\Fineor")
print(R"cat and dog\ they* are not friend")


