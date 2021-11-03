import random

class Buscaminas():
    
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = None
        self.show = None
        self.generate_board(rows,cols,bombs)
        
    def generate_board(self, rows, cols, bombs):
        self.board = [[' ' for y in range(cols)] for x in range(rows)]
        self.show = [['-' for y in range(cols)] for x in range(rows)]
        
        #Colocar bombas
        
        for i in range(bombs):
            while True:
                x_coord = random.randrange(0, rows)
                y_coord = random.randrange(0, cols)
                if self.board[x_coord][y_coord] != 'B':
                    self.board[x_coord][y_coord] = 'B'
                    break
        
        #Colocar números
        
        for x in range(rows):
            for y in range(cols):
                if self.board[x][y] != 'B':
                    aux = []  #contiene las casillas contiguas al casillero
                    for inc1 in (-1,0,1):
                        for inc2 in (-1,0,1):
                            try:
                                if not ((x +  inc1 < 0 or y + inc2 < 0) or (inc1 == 0 and inc2 == 0)):
                                    aux.append(self.board[x + inc1][y + inc2])
                            except Exception:
                                continue
                        self.board[x][y] = str(aux.count('B')) if aux.count('B') != 0 else ' '
        
    def show_board(self):
        for x in range(self.rows):
            print('{}    {}'.format(self.board[x], self.show[x]))
    
    def question(self, movs = ['flag','uncover']):
        
        #Pedir movimiento

        while True:
            mov = input('\n¿Qué desea hacer? (ingrese el nombre correspondiente)\n1.FLAG   2.UNCOVER\n\n')
            if mov.lower() not in ('flag', 'uncover'):
                raise Exception()
            else:
                break
        
        #Pedir fila
        
        while True:
            row = input('\nIngrese el Nº de fila correspondiente: ')
            if str(row) not in [str(x) for x in range(self.rows)]:
                raise Exception()
            else:
                row = int(row)
                break
        
        #Pedir columna
        
        while True:
            col = input('\nIngrese el Nº de columna correspondiente: ')
            if str(col) not in [str(x) for x in range(self.cols)]:
                raise Exception()
            else:
                col = int(col)
                break
        
        return [mov, row, col]
    
    def play(self, mov, row, col):
        if mov == 'flag':
            self.show[row][col] = 'F'
        else:
            self.show[row][col] = self.board[row][col]
        
    def win(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.show == [['-' for y in range(self.cols)] for x in range(self.rows)]:
                    return False
                elif self.board[x][y] == ' ':
                    continue
                if self.board[x][y].isdigit() and self.show[x][y] == 'F':
                    return False
                if self.board[x][y] == 'B' and self.show[x][y] != 'F':
                    return False
        return True

    def lose(self):
        for x in self.show:
            if 'B' in x:
                return True
        return False 

