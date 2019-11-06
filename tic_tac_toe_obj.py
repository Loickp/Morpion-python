from random import randint
flag = True

class Grille():
    def __init__(self):
        #self.board = [' ']*10
        self.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', ' ', 'O']

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        self.board[key] = value

    def display(self):
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def verify(self):
        x = 1
        z = 1

        for i in range(3):
            if (self.board[x] == self.board[x + 1] == self.board[x + 2]) and self.board[x] != " ":
                return 1
            else:
                x += 3

        for j in range(3):
            if (self.board[z] == self.board[z + 3] == self.board[z + 6]) and self.board[z] != " ":
                return 1
            else:
                z += 1

        if (self.board[1] == self.board[5] == self.board[9]) and self.board[1] != " ":
            return 1
        elif (self.board[3] == self.board[5] == self.board[7]) and self.board[3] != " ":
            return 1

class Joueur():
    def __init__(self):
        self.name = "Joueur"
        self.shape = "X"

    def place(self):
        x = int(input("Quel case ? "))
        if board[x] == " ":
            board[x] = self.shape
            print("Joueur : ")
            board.display()
        else:
            print("Case déjà remplie")
            return self.place()

class Ordinateur():
    def __init__(self):
        self.name = "Ordinateur"
        self.shape = "O"

    def place(self):
        rand = randint(1, 9)

        if board[rand] == " ":
            board[rand] = self.shape
            print("Ordi : ")
            board.display()
        else:
            return self.place()

def tie(board):
    count = 0
    for i in range(0, 8):
        if board[i] != " ":
            count += 1
            print(count)

    if count == 8:
        return True
    else:
        return False


board = Grille()
player = Joueur()
ordi = Ordinateur()

print("Joueur voici votre forme : " + player.shape)
print("L'ordinateur à comme forme : " + ordi.shape)

while True:
    tie(board)

    player.place()
    if board.verify():
        print("Victory for player")
        break

    if tie(board):
        print("Tie !")
        break

    ordi.place()
    if board.verify():
        print("Victory for computer")
        break