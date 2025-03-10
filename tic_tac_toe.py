from random import randint

#création d'une liste pour la grille à afficher
board = [' ' for x in range(10)]

#fonction qui permet d'afficher la grille de jeu
def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


#fonction qui permet au joueur de choisir la forme qu'il veut utiliser
def choose():
    global form

    choose = int(input("Quelle forme voulez vous choisir, X (=0) ou O (=1) ? "))
    if choose == 0:
        print("Vous avez choisi X")
        form = 0
    elif choose == 1:
        print("Vous avez choisi O")
        form = 1
    else:
        print("Vous n'avez rien choisi !")


#fonction qui verifie la victoire, horizontalement, verticalement et les diagonales
def verify():
    x = 1
    z = 1

    #verification horizontale
    for i in range(3):
        if (board[x] == board[x+1] == board[x+2]) and board[x] != " ":
            return 1
        else:
            x += 3
    #verification verticale
    for j in range(3):
        if (board[z] == board[z+3] == board[z+6]) and board[z] != " ":
            return 1
        else:
            z += 1
    #verification des diagonales
    if (board[1] == board[5] == board[9]) and board[1] != " ":
        return 1
    elif (board[3] == board[5] == board[7]) and board[3] != " ":
        return 1

#fonction qui permet au joueur de séléctionner la case ou il veut placer sa forme
def place():
    x = int(input("Quel case ? "))
    if board[x] == " ":
        if form == 0:
            board[x] = "X"
        else:
            board[x] = "O"
        print("Joueur : ")
        print_board(board)
    else:
        print("Case déjà remplie")
        return place()

#fonction qui détermine la forme de l'ordinateur et place la forme sur la grille
def ordi():
    rand = randint(1, 9)

    if form == 0:
        ordi_form = "O"
    else:
        ordi_form = "X"

    if board[rand] == " ":
        board[rand] = ordi_form
        print("Ordi : ")
        print_board(board)
    else:
        return ordi()

choose()

#boucle while qui permet de lancer le jeu
while True:
    place()
    verify()
    if verify():
        print("Victory for player")
        break
    ordi()
    verify()
    if verify():
        print("Victory for computer")
        break