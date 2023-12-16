def controler(mini:str,nombre:int,maxi:str)->int:
    """
    Fonction qui compare les bornes d'un nombre avec celui ci pour eviter toute erreur de saisie.
    La fonction demande de resaisir le nombre "nombre" s'il est incorrect
    Entree  :  2 chaine de caractere, entier
    Sortie  : entier
    """
    affichage : str

    if mini!='None' and maxi!='None':
        while nombre<int(mini) or nombre>int(maxi):
            print("Erreur, le nombre doit être compris entre "+mini+" et "+maxi)
            affichage="Entrez un nombre compris entre "+mini+" et "+maxi+" : "
            nombre=int(input(affichage))

    elif maxi=='None' and mini!='None':
        while nombre<int(mini) :
            print("Erreur, le nombre doit être supérieur ou égale à "+mini)
            affichage="Entrez un nombre supérieur ou égale à "+mini+" : "
            nombre=int(input(affichage))

    elif mini=='None' and maxi!='None':
        while nombre>int(maxi) :
            print("Erreur, le nombre doit être inférieur ou égale à "+maxi)
            affichage="Entrez un nombre inférieur ou égale à "+maxi+" : "
            nombre=int(input(affichage))
    return nombre

def reglesalumette():


    """
    Procedure qui affiche les regles du jeu
    Entrer :  rien
    sortie : rien
    """


    print("Bienvenue dans le jeu des allumettes")
    print("Les règles sont simples :")
    print("Il y a deux joueurs, chaque joueur peut à tour de rôle prélever 1, 2 ou 3 allumettes")
    print("le joueur qui prend le dernière allumette a perdu : ")

def scorejeu(perdant:int,joueur:list[str])->list[list[str]]:
    """
    Procédure qui definie le gagnant et le perdant
    Entree : entier, liste de chaine de caractere
    Sortie : tableau de tableau de chaine de caractere

    """
    scoregangant:int
    scoreperdant:int
    if perdant==0:
        gagnant=1
    else:
        gagnant=0
    scoregangant=10
    scoreperdant=0
    print(f"Le joueur {joueur[gagnant]} à gagné {scoregangant} pts\nLe joueur {joueur[perdant]} à gagné {scoreperdant} pts")
    return([[str(joueur[gagnant]),str(scoregangant)],[str(joueur[perdant]),str(scoreperdant)]])

def affichermode():
    print("-------------------------------Il existe 3 modes-------------------------------")
    print("  1   -   Humain contre Humain")
    print("  2   -   Humain contre Machine")
    print("  3   -   Machine contre machine")


def principalallumetteshvh()->list[list[str]]: #humain contre humain 

    """
    Fonction qui correspond au programme proncipale du jeu alumettes
    Entrée : rien
    Sortie : chaine de caractere, qui correspond au score.
    """

    nballumettes : int
    nballumettesenlever : int
    joueur1 : str
    tour:int
    joueur2 : str
    allumettes : str
    joueur:list[str]
    affinput :str
    perdu : bool
    score:list[list[str]]
    
    perdu=False
    nballumettesenlever=0
    tour=0
    nballumettes=20
    perdu=False
   
    reglesalumette()
    print()


    joueur1=input("Entrez votre nom joueur 1 : ")
    joueur2=input("Entrez votre nom joueur 2 : ")
    joueur=[joueur1,joueur2]
    allumettes=("|"+" ")*nballumettes
    print("Il reste ---> ",allumettes)
    print()

    while nballumettes!=1 and perdu==False:


        if nballumettes==0:
            perdu=True
            print(None)
            if tour==0:
                tour=1
            else:
                tour=0
        else:
            print()
            affinput=str(joueur[tour])+", entrez le nombre d'allumettes à enlever :"
            nballumettesenlever=int(input(affinput))
            nballumettesenlever=controler('1',nballumettesenlever,'3')
            if nballumettesenlever>len(allumettes)/2:
                print("erreur on ne peut pas enlever plus d'allumettes qu'il y en a")
            else:
                nballumettes=nballumettes-nballumettesenlever
                if tour==0:
                    tour=1
                else:
                    tour=0

        allumettes=("|"+" ")*nballumettes
        print("Il reste ---> ",allumettes)

    score=scorejeu(tour,joueur) #les tours sont inversé : 0 désigne mtn le joueur2 et 1 désigne mtn le joueur1

    return score

if __name__=="__main__":
    print(principalallumetteshvh())
    


    







