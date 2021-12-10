import random
from colorama import init, Fore

#certains mots du code sont en anglais mais c'est juste quelque chose que je préfère pour me retrouver.
#message de présentation classique pour acceuillir le joueur.
WelcomeToMotus = input("Bienvenue dans Motus, veuillez appuyer sur entrée pour commencer le jeu, et bonne chance!")
#La liste des mots à 6 lettres (français et quelque-uns en anglais car je n'avais pas d'idée)
ListOfWord = ["CASTOR", "CINEMA", "CYPRUS", "CITRON" , "SOLIDE" , "OCELOT", "LIQUID" , "RANDOM", "FRENCH"]
wordtofind = random.choice(ListOfWord)
#le mots secret contient X lettres, c'est une indication.
print("Le mots secret contient ", len(wordtofind), "lettres")
while True:
    #la consigne au joueur : c'est la chose que le joueur doit faire. Pas de tentatives limites car je ne sais plus comment les créers, c'est donc un Motus sans malus. La chance vous sourit.
    WordToGuess = input("veuillez deviner le mot! Ecrivez en majuscule.")
    #tentative de code ayant un résultat assez mitigé et indications en cas d'échec
    if len(WordToGuess) != len(wordtofind): print("Marquer un chiffre avec"), len(wordtofind),"chiffres"
    elif WordToGuess == wordtofind :  break
    elif WordToGuess != wordtofind:
        if WordToGuess != wordtofind : print ("Ce n'est pas le bon mot! Veuillez réssayer.")
    
#Indication si le joueur réussit
print("Vous avez trouvez le bon mot! Félicitation!")







#Techniquement ça marche mais ce n'est pas vraiment la consigne : il n'y a pas de couleurs et des fonctions manquantes, et ce programme ne demande pas de chercher des lettres mais des mots, c'est juste une version simplifié du jeu de base...


