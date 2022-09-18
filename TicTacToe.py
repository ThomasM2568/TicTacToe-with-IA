# Créé par Thomas MIRBEY, le 16/09/2022 en Python 3.7
# Création du jeu tictactoe, avec comme but de mettre en place une IA
# comme deuxième joueur

#Importation du module random pour tirer au sort le joueur qui commence à jouer
import random

#Création de la classe TicTacToe avec comme arguments deux noms de joueurs
#On va générer une liste de listes qui va gérer les cases du jeu
class TicTacToe:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.game=["_","_","_"],["_","_","_"],["_","_","_"]
        self.icon=""
        self.value=0

    #Cette méthode permet d'obtenir le symbole de la case dont les coordonnées
    #seront les variables
    def __getValue__(self,x,y):
        if (type(x)==int and type(y)==int):
            if(abs(x)>=0 and abs(x)<=len(self.game) and abs(y)>=0 and abs(y)<=len(self.game)):

                return self.game[abs(x)][abs(y)]
            else:

                return("Wrong value for x or y")
        else:
            try:
                int(x)
            except:
               return("Error, type of x must be integer ",type(x)," given")
            try:
                int(y)
            except:
                return("Error, type of y must be integer ",type(y)," given")

    #Cette méthode permet d'afficher la grille du jeu
    def __printGame__(self):
        for i in range(0,len(self.game)):
            print(self.game[i])
    #Cette méthode permet de décider aléatoirement le joueur qui va
    #démarrer la partie
    def __decideStart__(self):
        self.start=random.randint(1, 2)
        if(self.start==2):
            #Le joueur 2 a l'icone O
            self.start=2
            self.icon="O"
        else:
            #Le joueur 1 a l'icone X
            self.start=1
            self.icon="X"
        return self.start

    #Cette méthode permet d'afficher le joueur qui doit jouer
    def __whoPlays__(self):
        if(self.start)==1:
            self.current=self.player1
        else:
            self.current=self.player2
        return (self.start)

    #Cette méthode permet de changer le joueur qui joue
    #Elle est utilisée à chaque coup valide
    def __changePlayer__(self):
        print("Whoplays=",self.__whoPlays__(),"START=",self.start)

        if(self.start%2==0):
            self.start=1
            self.icon="X"

        elif(self.start%2!=0):
            self.start=2
            self.icon="O"

    #Cette méthode permet à un joueur de choisir une case
    #Elle va remplacer la valeur vide par le symbole du joueur en question
    def __PickACase__(self,x,y):
        if (self.__getValue__(x,y)=="_"):


            self.__changePlayer__()
            self.game[x][y]=self.icon
            self.value+=1
            #return self.__printGame__()
        else:
            print("Case déjà occupée")
            x=int(input("Entrez une nouvelle valeur pour x"))
            y=int(input("Entrez une nouvelle valeur pour y"))
            self.__PickACase__(x,y)

    def __End__(self):
        #Permet de vérifier si une partie est finie
        #Soit elle est gagnée
        #Vérification des lignes
        for i in range(0,3):
            if (self.__getValue__(i,0)!="_" and self.__getValue__(i,1)!="_" and self.__getValue__(i,2)!="_"):
                if (self.__getValue__(i,0)==self.__getValue__(i,1)==self.__getValue__(i,2)):
                    print("Le joueur ",self.current," a gagné (symbole",self.icon,")")
                    return("Game is Over")

        #Vérification des colonnes
        for j in range(0,3):
            if (self.__getValue__(0,j)!="_" and self.__getValue__(1,j)!="_" and self.__getValue__(2,j)!="_"):
                if (self.__getValue__(0,j)==self.__getValue__(1,j)==self.__getValue__(2,j)):
                    print("Le joueur ",self.current," a gagné (symbole",self.icon,")")
                    return("Game is Over")

        #Vérification des diagonales
        if (self.__getValue__(0,0)!="_" and self.__getValue__(1,1)!="_" and self.__getValue__(2,2)!="_"):
                if (self.__getValue__(0,0)==self.__getValue__(1,1)==self.__getValue__(2,2)):
                    print("Le joueur ",self.current," a gagné (symbole",self.icon,")")
                    return("Game is Over")

        if (self.__getValue__(0,2)!="_" and self.__getValue__(1,1)!="_" and self.__getValue__(2,0)!="_"):
                if (self.__getValue__(0,2)==self.__getValue__(1,1)==self.__getValue__(2,0)):
                    print("Le joueur ",self.current," a gagné (symbole",self.icon,")")
                    return("Game is Over")

        #Soit elle est perdue si 9 coups valides ont été effectués

        if (self.value==9):
            print("Egalité, personne n'a gagné")
            return("Game is Over")






toto=TicTacToe("Thomas","Yohann")
print(toto.__printGame__())
print(toto.__decideStart__())
#Le joueur 1 a l'icone X
#Le joueur 2 a l'icone O

while(toto.__End__()!="Game is Over"):
    print(toto.__printGame__())


    print(toto.__whoPlays__())
    x1=int(input("Entrez une valeur pour x "))
    y1=int(input("Entrez une valeur pour y "))
    toto.__PickACase__(x1,y1)
    toto.__printGame__()
    print("coup:",toto.value)

    if(toto.__End__()=="Game is Over"):
        break

    print(toto.__whoPlays__())
    x2=int(input("Entrez une valeur pour x "))
    y2=int(input("Entrez une valeur pour y "))
    toto.__PickACase__(x2,y2)
    toto.__printGame__()
    print("coup:",toto.value)

    print(toto.__End__())




