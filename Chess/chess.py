def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }
    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9822),
        Queen: chr(9819),
        King: chr(9818),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y+1, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')
    for x in range(8):
        print(chr(65+x), end='\t')
    print()


def filter_moves(moves):  # aby pionki nie wychodzily za szachownice
    output = []
    for move in moves:
        if 0 <= move[0] < 8 and 0 <= move[1] < 8:
            output.append(move)
    return output


class Chessboard:
    def __init__(self):
        self.color = 'white'
        self.board = [
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,  # ten przecinek może być w niczym nie przeszkadza
        ]

    def setup(self):
        self.board[0][0] = Rook('white', 0, 0)
        self.board[1][0] = Knight('white', 1, 0)
        self.board[2][0] = Bishop('white', 2, 0)
        self.board[3][0] = Queen('white', 3, 0)
        self.board[4][0] = King('white', 4, 0)
        self.board[5][0] = Bishop('white', 5, 0)
        self.board[6][0] = Knight('white', 6, 0)
        self.board[7][0] = Rook('white', 7, 0)
        for x in range(0, 8):
            self.board[x][1] = Pawn('white', x, 1)
            self.board[x][6] = Pawn('black', x, 6)
        self.board[0][7] = Rook('black', 0, 7)
        self.board[1][7] = Knight('black', 1, 7)
        self.board[2][7] = Bishop('black', 2, 7)
        self.board[3][7] = Queen('black', 3, 7)
        self.board[4][7] = King('black', 4, 7)
        self.board[5][7] = Bishop('black', 5, 7)
        self.board[6][7] = Knight('black', 6, 7)
        self.board[7][7] = Rook('black', 7, 7)

    def list_allowed_moves(self, x, y):
        if self.board[x][y] == None:  # sprawdzamy czy miejsce x y jest puste
            return None
        if self.board[x][y].color != self.color:  # sprawdzamy czy kolor gracza zgadza sie z kolorem pionka
            return None
        return self.board[x][y].list_allowed_moves(self)  # pionku w miejscu x y jakie sa twoje dozwolone ruchy
        # self w obrebie tej klasy jest chessboardem

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)  # pytamy o dozwolone ruchy z miejsca from_x, from_y
        if allowed_moves == None:
            raise ValueError('Tu nie ma twojego pionka!')

        if (to_x, to_y) not in allowed_moves:  # pytamy czy mozna ruszyc pionek z x to y
            raise ValueError('Ten ruch jest niemożliwy!')

        self.board[to_x][to_y] = self.board[from_x][from_y]  # pionek przesuwa sie na nowe pole

        self.board[from_x][from_y] = None  # miejsce zostaje puste

        self.board[to_x][to_y].move(to_x, to_y)  # informujemy pionek pod nowym adresem o jego nowej pozycji

        if self.color == 'white':  # zmieniamy kolor
            self.color = 'black'
        else:
            self.color = 'white'

    def is_enemy(self, x, y, my_color): #aby zobaczyć czy są wrogowie i moc ich bic lub nie moc sie ruszyc
        if self.board[x][y] is None:
           return False # empty - nie ma wroga
        if self.board[x][y].color != my_color:
            return True # enemy
        return False # jest friend

    def is_friend(self, x, y, my_color): #aby sprawdzic czy na przeciwko jest pionek
        if self.board[x][y] is None:
            return False #empty
        if self.board[x][y].color == my_color:
            return True #friend
        return False #enemy

    def is_anyone(self, x, y):
        return self.board[x][y] is not None #jezeli ktos stoi to nie jest None czyli True

    def is_empty(self, x ,y):
        return not self.is_anyone(x, y) #jeżeli nie jest is_anyone to jest empty

class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Pawn(Piece):
    def list_allowed_moves(self, chessboard):
        moves = []

        if self.color == 'white' and self.y == 7:
            return []
        elif self.color == 'black' and self.y == 0:
            return []
                # koniec planszy to definitywny koniec ruchów wiec return zostaje

        if self.color == "white":
            if chessboard.is_empty(self.x, self.y + 1):
                moves.append((self.x, self.y + 1))
                if self.y == 1 and chessboard.is_empty(self.x, self.y + 2):
                    moves.append((self.x, self.y + 2))
        elif self.color == "black":
            if chessboard.is_empty(self.x, self.y - 1):
                moves.append((self.x, self.y - 1))
                if self.y == 6 and chessboard.is_empty(self.x, self.y - 2):
                    moves.append((self.x, self.y - 2))

        # elif self.color == 'white' and self.y == 1:  # bo pionek sie jeszcze nie ruszal
        #     moves += [(self.x, self.y + 1), (self.x, self.y + 2)]
        # elif self.color == 'black' and self.y == 6:  # bo pionek sie jeszcze nie ruszal
        #     moves += [(self.x, self.y - 1), (self.x, self.y - 2)]
        # elif self.color == 'white':
        #     moves += [(self.x, self.y + 1)]
        # elif self.color == 'black':
        #     moves += [(self.y, self.y - 1)]

        if self.color == 'white':
            if chessboard.is_enemy(self.x+1, self.y+1, self.color):
                moves.append( (self.x+1, self.y+1) )
            if chessboard.is_enemy(self.x-1, self.y+1, self.color):
                moves.append( (self.x-1, self.y+1) )
        elif self.color == 'black':
            if chessboard.is_enemy(self.x + 1, self.y - 1, self.color):
                moves.append((self.x + 1, self.y - 1))
            if chessboard.is_enemy(self.x - 1, self.y - 1, self.color):
                moves.append((self.x - 1, self.y - 1))

        return filter_moves(moves)


class Knight(Piece):
    def list_allowed_moves(self, chessboard):
        moves = [
            (self.x + 1, self.y + 2),
            (self.x + 2, self.y + 1),
            (self.x - 1, self.y + 2),
            (self.x - 2, self.y + 1),
            (self.x + 1, self.y - 2),
            (self.x + 2, self.y - 1),
            (self.x - 1, self.y - 2),
            (self.x - 2, self.y - 1),
        ]
        return filter_moves(moves)


class Rook(Piece):
    def list_allowed_moves(self, chessboard):
        moves = []
        for i in range(1, 8):  # bo musie sie ruszyć a nie
            moves.append((self.x + i, self.y))  # aby dodać do move ale tuple
            moves.append((self.x - i, self.y))
            moves.append((self.x, self.y + i))
            moves.append((self.x, self.y - i))
        good_moves = filter_moves(moves)  # można ale nie trzeba
        return good_moves


class King(Piece):
    def list_allowed_moves(self, chessboard):
        moves = [
            (self.x, self.y + 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y),
            (self.x - 1, self.y),
            (self.x + 1, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y - 1),
        ]
        return filter_moves(moves)


class Bishop(Piece):
    def list_allowed_moves(self, chessboard):
        moves = []
        for i in range(1, 8):
            moves.append((self.x + i, self.y + i))
            moves.append((self.x - i, self.y - i))
            moves.append((self.x - i, self.y + i))
            moves.append((self.x + i, self.y - i))
        return filter_moves(moves)


class Queen(Piece):
    def list_allowed_moves(self, chessboard):
        moves = []
        for i in range(1, 8):
            moves.append((self.x + i, self.y))
            moves.append((self.x - i, self.y))
            moves.append((self.x, self.y + i))
            moves.append((self.x, self.y - i))
            moves.append((self.x + i, self.y + i))
            moves.append((self.x - i, self.y - i))
            moves.append((self.x - i, self.y + i))
            moves.append((self.x + i, self.y - i))
        return filter_moves(moves)
