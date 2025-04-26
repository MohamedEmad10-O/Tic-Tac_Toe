import os
def clear_screen():
    os.system("cls") 
class Player:
    def __init__(self):
        self.name = ""
        self.Symbol = ""

    def choose_name(self):
        while True :
            name = input("Enetr you name (Letters only): ").strip()
            if name.isalpha():
                self.name = name
                break
            print("Invaild name, Please use letters only.")

    def choose_symbol(self) :
        while True :
            Symbols = ["X", "O"]
            Symbol = input(f"{self.name} , Choose your symbol (a signal letters [ X , O ]): ")
            if Symbol.upper() in Symbols :
                self.Symbol = Symbol.upper()
                break
            print("invaild symbol.")
          
class Menu :

    def display_main_menu(self):
        
        print("Welcom to my X-O game!")
        print("1. Start Game.")
        print("2. Quit Game.")
        
        while True :
            choose = input("Enter your choice (1 or 2): ")
            if choose  in ["1","2"] :
                return choose
            
            
    def display_endgame_menu(self):
        end = """
        1. Restart Game!
        2. Quite Game !
        - Enter your choice (1 or 2): 
        """
        while True :
            choose = input(end)
            if choose  in ["1","2"] :
                return choose
            
class Board:
    def __init__(self):
        self.board = [str(i) for i in  range(1,10)]
    
    def display_board(self) :
        for i in range(0,9,3) :
            print(" | ".join(self.board[i:i+3])) 
            print("-"*10)

    def update_board(self , choice , symbol) :
        if self.in_valid_choice(choice):
            self.board[choice - 1 ] = symbol
            return True
        return False 
    
    def in_valid_choice(self,choice) :
        return self.board[choice -1 ].isdigit()
    
    def reset_board(self) :
        self.board = [str(i) for i in  range(1,10)]

class Game :
    def __init__(self):
        self.Board = Board()
        self.player = [Player() , Player()]
        self.menu = Menu()
        self.current_index_player = 0

    def start_game(self) :

        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_player()
            self.play_game()
        else :
            self.qiut_Game()
    def setup_player(self) :
        for key , player in enumerate(self.player , start= 1):
            print(f"player {key}, Enetr Your Details......")
            player.choose_name()
            player.choose_symbol()
            print("*" *50)
            self.Switch_Player()
            clear_screen()

    def play_game(self):
        while True :
            self.play_turn()
            if self.check_win() or self.check_draw() :
                self.Board.display_board()

                if self.check_win() :
                    clear_screen()
                    self.Board.display_board()
                    print(f"{self.player[1-self.current_index_player].name} is win!")
                    
                else :

                    print("Game Over!")    

                choice = self.menu.display_endgame_menu()

                if choice == "1" :

                    self.Restart_Game()
                    
                else :

                    self.qiut_Game() 
                  
    def play_turn(self):
        player = self.player[self.current_index_player]

        self.Board.display_board()
        print(f"{player.name} 's {player.Symbol}  turn.")
        
        try :
            while True :
                cell = int(input("Choose a cell Between (1-9): "))
                if 1 <= cell <= 9 and self.Board.update_board(cell , player.Symbol):
                    clear_screen()
                    break 
                else :
                        print("Invalid Move, Try again!")
        except ValueError :
            print("Please, Enetr a number between 1 and 9.")
        self.Switch_Player()
    def check_win(self):
        diagram = [[0,1,2],[3,4,5],[6,7,8],
                   [0,3,6],[1,4,7],[2,5,8],
                   [0,4,8],[2,4,6]]
        
        for i in diagram :
            if self.Board.board[i[0]] == self.Board.board[i[1]] == self.Board.board[i[2]] :
                return True
            
        return False
        

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.Board.board)


    def  Restart_Game(self) :
        clear_screen()
        print("For Replay, Enetr a Username & Password!")
        
        self.Board.reset_board()
        self.current_index_player = 0
        self.play_game()     

    
    def Switch_Player(self):
        self.current_index_player = 1 - self.current_index_player 
    def qiut_Game(self) :
        print("Thank you for playing!")
        quit()



game = Game()
game.start_game()        


#==================================================================
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(0, 0)
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_widgets()
    
    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
    
    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False
    
    def reset_board(self):
        self.board = ["" for _ in range(9)]
        for btn in self.buttons:
            btn["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

