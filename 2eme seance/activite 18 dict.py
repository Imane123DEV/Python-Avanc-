machines = {
    "m1":"192.168.0.1",
    "m2":"192.168.0.2",
    "m3":"192.168.0.3",
    "m4":"192.168.0.4",
    "m5":"192.168.0.5",
}
print(f"ladresse de machines2 est:{machines['m2']}")
print("le nombre des machines est :",len(machines))
machines["m6"]="192.168.0.6"
print(machines)
del machines["m4"]
print(machines)
print("m5" in machines)
print(f"entrer le nom de la machine:")
n=input()
if n in machines:
    print(f"ladresse de {n} est :{machines[n]}")
else:
    print(f"La machine {n} n'exixte pas")
    

