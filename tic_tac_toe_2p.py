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
    global form_1
    global form_2

    choose = int(input("Quelle forme voulez vous choisir, X (=0) ou O (=1) ? "))
    if choose == 0:
        print("Joueur 1 : X\nJoueur 2 : O")
        form_1 = "X"
        form_2 = "O"
    elif choose == 1:
        print("Joueur 1 : O\nJoueur 2 : X")
        form_1 = "O"
        form_2 = "X"
    else:
        print("Vous n'avez rien choisi !")


#fonction qui permet au joueur de séléctionner la case ou il veut placer sa forme
def place():
    global turn

    if turn == 1:
        x = int(input("Joueur 1 : Quel case ? "))

        if board[x] == " ":
            board[x] = form_1
            print_board(board)
        else:
            print("Case déjà remplie")
            return place()
    else:
        y = int(input("Joueur 2 : Quel case ? "))
        if board[y] == " ":
            board[y] = form_2
            print_board(board)
        else:
            print("Case déjà remplie")
            return place()


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


choose()

while True:
    turn = 1
    place()
    if verify():
        print("Victory for player 1")
        break
    turn = 2
    place()
    if verify():
        print("Victory for player 2")
        break
