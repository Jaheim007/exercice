import numbers


numbers = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
numbre = input("Veuillez saisir un nombre entre 10 et 20 ")

for i in numbers:
    if numbre < 10:
        print("Plus Grand")
    elif numbre > 20: 


num = 20
nut = 10
while num > 20 and num < 10:
    if numbre > num:
        print("Plus Petit")
    elif numbre < nut:
        print("Plus Grand") 
    else:
        print("Felicitations")