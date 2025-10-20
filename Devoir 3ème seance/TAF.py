with open("Table_de_multiplication.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"Table de multiplication de {i}:\n")
        for j in range(1, 11):
            file.write(f"{i} x {j} = {i * j}\n")
        file.write("\n")