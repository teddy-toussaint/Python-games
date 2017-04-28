# Importations
from random import randrange
from math import ceil

# Initialisation
print("Bienvenue au jeu de la roulette !")

while 1:
    try:
        s = int(input("Combien d'argent avez-vous ? "))
    except ValueError:
        print("Veuillez choisir un nombre entier svp.\n")
        continue
    break

while 1:
    
    # Lecture du nombre sur lequel le joueur mise
    try:
        a = int(input("Sur quel nombre misez-vous (0-49) ? "))
    except ValueError:
        print("Veuillez choisir un nombre svp.")
        continue
    if a not in range(50):
        print("Veuillez choisir un nombre compris entre 0 et 49 inclus svp.\n")
        continue
    
    # Lecture de la mise
    while 1:
        try:
            m = int(input("Combien souhaitez-vous miser ? "))
        except ValueError:
            print("Veuillez choisir un nombre svp.")
            continue
        if m > s:
            print("Vous n'avez pas assez d'argent...\n")
            continue
        else:
            break
    
    s -= m
    print()
    
    # Tirage au sort de la roulette
    print("Tirage au sort...")
    n = randrange(50)
    print("Nombre tiré: {}.\n".format(n))
    
    # Renvoi du résultat
    if a == n:
        print("Félicitations !!! Vous gagnez 3 fois votre mise, soit {}$ !".format(3*m))
        s += m + 3*m
    elif a%2 == n%2:
        print("Bravo ! Vous gagnez 50% de votre mise, soit {}$ !".format(ceil(m/2)))
        s += m + ceil(m/2)
    else:
        print("Pas de chance ! Vous perdez votre mise !")
            
    print("Vous avez donc en votre possession {}$.\n".format(s))
    
    # Fin potentielle du programme
    if s == 0:
        print("Vous n'avez plus d'argent : fin du jeu. Merci de votre participation, et à bientôt !")
        break
        
    while 1:
        y = input("Souhaitez-vous relancer la roulette (y/n) ? ")
        if y.lower() != "y" and y.lower() != "n":
            print("Veuillez choisir 'y' ou 'n' svp.\n")
            continue
        else:
            break
        
    if y.lower() == "y":
        continue
    else:
        print("Fin du jeu. Merci de votre participation, et à bientôt !")
        break
    
            
