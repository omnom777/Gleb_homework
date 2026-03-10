class TicTacToe:
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.current_player = 'X'
        self.game_over = False
        self.win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    
    def display_board(self):
        print("# # # # # # #")
        print(f"# {self.board[0]} # {self.board[1]} # {self.board[2]} #")
        print("# # # # # # #")
        print(f"# {self.board[3]} # {self.board[4]} # {self.board[5]} #")
        print("# # # # # # #")
        print(f"# {self.board[6]} # {self.board[7]} # {self.board[8]} #")
        print("# # # # # # #")
    
    def move(self, pos):
        if pos < 1 or pos > 9:
            print("Ошибка: номер клетки должен быть от 1 до 9!")
            return False
        
        index = pos - 1
        if self.board[index] != ' ':
            print(f"Ошибка: клетка {pos} уже занята символом {self.board[index]}!")
            return False
        
        self.board[index] = self.current_player
        return True
    
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
    
    def check_win(self):
        if self.board[0] == self.board[1] == self.board[2] == self.current_player:
            return True
        if self.board[3] == self.board[4] == self.board[5] == self.current_player:
            return True
        if self.board[6] == self.board[7] == self.board[8] == self.current_player:
            return True
        if self.board[0] == self.board[3] == self.board[6] == self.current_player:
            return True
        if self.board[1] == self.board[4] == self.board[7] == self.current_player:
            return True
        if self.board[2] == self.board[5] == self.board[8] == self.current_player:
            return True
        if self.board[0] == self.board[4] == self.board[8] == self.current_player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == self.current_player:
            return True
        return False   
    def check_draw(self):
        for cell in self.board:
            if cell == ' ':
                return False
        return True
def get_player_input(game):
    while True:
        user_input = input(f"Игрок {game.current_player}, введите номер клетки")
        position = int(user_input)
        if game.move(position):
            return position
def play_game():
    print("Номера клеток:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")   
    g = TicTacToe()    
    while not g.game_over:
        g.display_board()
        get_player_input()        
        if g.check_win():
            g.display_board()
            print(f"Игрок {g.current_player} победил!")
            g.game_over = True
        elif g.check_draw():
            g.display_board()
            print("Ничья")
            g.game_over = True
        else:
            g.switch_player()
    
    print("Спасибо за игру!")
play_game()