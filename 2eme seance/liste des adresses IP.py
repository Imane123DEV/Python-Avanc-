import ipaddress

adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1","169.254.0.1"]

# Affiche la premiere adresse IP de la liste
print ("premiere adresse : ", adresses_ip[0])

# Affiche la derniere adresse IP de la liste
print("derniere adresse : ", adresses_ip[-1])

# Affiche la troisieme adresse IP de la liste
print("troisieme adresse : ", adresses_ip[2])

# Ajouter une nouvelle adresse IP a la liste
adresses_ip.append("172.31.0.1")
print("liste apres ajout : ", adresses_ip)

# Supression d'une adresse IP de la liste
adresses_ip.remove("200.100.50.1")

# Nombre d"adresses IP apres modification
print("nombre d'adresses IP : ", len(adresses_ip))

# Verification de la presence d'une adresse IP dans la liste
if "192.168.0.1" in adresses_ip:
    print("192.168.0.1 existe dans la liste")

#  Classe de "10.0.0.1"
def classe(ip):
    n = int(ip.split('.')[0])
    if n < 128:
        return "A"
    elif n < 192:
        return "B"
    else:
        return "C"

print(classe("10.0.0.1"))

# Trier par ordre croissant
adresses_ip.sort()
print("Trie croissant :", adresses_ip)

# Verification si toutes les adresses sont de classe C
print(all(classe(ip) == "C" for ip in adresses_ip))

# nombre des adresses IP publiques de la liste
nb_publiques = sum(not ipaddress.ip_address(ip).is_private for ip in adresses_ip)e
print("Nombre d'adresses IP publiques :", nb_publiques)