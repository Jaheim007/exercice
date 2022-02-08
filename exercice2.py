numbre = int(input("Veuillez saisir un nombre entre 10 et 20:\t "))  

nut = 10
num = 20

while numbre != 0:
    if numbre >= num:
        print("Plus Petit! ")
    elif numbre <= nut:
        print("Plus Grand! ") 
    else:
        print("Felicitations")
        break
    numbre = int(input("Veuillez saisir un nombre entre 10 et 20:\t"))

        