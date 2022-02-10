numbre = int(input("Veuillez saisir un nombre:\t"))
post = 1
for position in range(2, 11):
    numbre2 = int(input("Veuillez saisir un nombre:\t"))
    if numbre2 > numbre :
        numbre = numbre2
        post = position
print("Value", numbre)
print('post', post )
    
