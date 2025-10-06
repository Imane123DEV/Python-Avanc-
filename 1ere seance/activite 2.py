# Question 1
a=int(input("saisir la variable a :"))
b=int(input("saisir la variable b :"))
print("la somme est :",a+b)
print("la multiplication est :",a*b)
# Question 2
t=a
a=b
b=t
print("a=",a)
print("b=",b)
# Question 3
a=int(input("saisir la variable a :"))
b=int(input("saisir la variable b :"))
if a>b:
    print("a est plus grand ")
else:
    print("b est plus grand ")
# Question 4
c=int(input("saisir la distance:"))
unite=input("saiasir unite :")
if unite=="km":
   print("la distance convertie en mille est ",c*0.624)
elif unite=="mille":
    print("la distance convertie en km est ",c*1.6)