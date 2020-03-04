prix = int(input(" entrer un prix unitaire : "))
heure = int(input(" entrer une heure suplementaire : " ))
prime = 0


if heure <=39 :
    augmentation1 = 0

elif heure <=40 and heure <=44:
    augmentation1 = ((heure -39) * 1.5 * prix)

elif heure <=45 and heure <=49:
    augmentation1 = ((heure -39) * 1.5 * prix)+ ((heure -44) * 1.75 * prix)

elif nhs >= 50:
    augmentation1 = ((heure -39) * 1.5 * prix) + ((heure -44) * 1.75 * prix) +  ((heure - 49) * 2 * prix)
else:
    augmentation1 = "vide"
print("vous avez une augmentation de ",augmentation1," $")
