def F1(n):
    n=int(input("entrer combien de fois afficher bonjour:" ))
    for i in range(n):
        print("bonjour")
F1()
def F2(n):
    n=int(input("entrer un nombre: "))
    if n%10==0:
        print(f"{n} est divisible par 10")
    else:
        print(f"{n} non divisible par 10") 
F2()
def F4(n):
    n=int(input("entrer un nombre: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"la factorielle de {n} est :{fact}")
F4()
def F3():
    n=input("entrer le mot: ")
    num=0
    l=['i','a','e','y','u','o']
    for element  in n:
        for v in l:
           if element==v:
               num+=1
    print("nombre de voyelles est : ", num)
F3()
def F5():
   n=int(input("entrer un nombre:"))
   for i in range(1,11):
       print(f"{n}*{i}={n*i}")
F5()
def F6():
    n=(input("entrer un mot : "))
    print("le nombre des caracteres est :",len(n))
F6()
def F7():
    n=int(input("entrer un nombre:"))
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b
F7() 