l3=[3,6,7,9,1]
for element in l3:
    print(element)
somme=sum(l3)
print("la somme est :",somme)
produit=1
for i in range(2,5):
    produit=produit*l3[i]
print("le produit est :",produit)
print("le maximum des elements de la liste est :",max(l3))
print("le minimum des elements de la liste est :",min(l3))
#nombre demultiple de 3:
for element in l3:
    if element %3==0:
        compt=+1
print("le nombre des multiples de 3 est :",compt)
l3.reverse()


