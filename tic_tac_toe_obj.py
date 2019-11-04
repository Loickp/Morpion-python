from random import randint

class Grille():
    def __init__(self):
        self.board = [' ']*10

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        self.board[key] = value

    def display(self):
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('-----------')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('-----------')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

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

    def tie(self):
        count = 0
        for x in self.board:
            if x != " ":
                count =+ 1
        if count == 9:
            return True
        else:
            return False

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
            return place()

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



board = Grille()
player = Joueur()
ordi = Ordinateur()

print("Joueur voici votre forme : " + player.shape)
print("L'ordinateur à comme forme : " + ordi.shape)

while True:
    player.place()
    if board.verify():
        print("Victory for player")
        break

    if board.tie():
        print("Tie !")
        break

    ordi.place()
    if board.verify():
        print("Victory for computer")
        break
