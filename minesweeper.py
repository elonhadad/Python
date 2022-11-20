"""
Student: elon hadad
Assignment no. 3
Program: minesweeper.py
"""
from random import randint


class GamePlay:
    """
    Class for checking win or lose.
    """
    def __init__(self):
        self.game_board = Board()
        self.lose = False
        self.win = False

    def check_win(self):

        opens = 0
        hidden_mines = self.game_board.get_num_of_mines()
        for row in range(self.game_board.get_size()):
            for col in range(self.game_board.get_size()):
                if self.game_board.this_board[row][col].get_has_mine() and not \
                        self.game_board.this_board[row][col].get_hidden():
                    self.lose = True
                if not self.game_board.this_board[row][col].get_has_mine() \
                        and not self.game_board.this_board[row][col].get_hidden():
                    opens += 1

        if self.game_board.get_size() ** 2 == opens + hidden_mines:
            self.win = True
            return

    def player_move(self, row, col):
        x, y = int(row) - 1, int(col) - 1
        if self.game_board.this_board[x][y].get_has_mine():
            self.game_board.this_board[x][y].set_hidden(False)
            self.lose = True
        else:
            self.game_board.show_all_squares(x, y)

    def expose(self):
        if self.lose:
            for row in range(self.game_board.get_size()):
                for col in range(self.game_board.get_size()):
                    if self.game_board.this_board[row][col].get_has_mine():
                        self.game_board.this_board[row][col].set_hidden(False)

    def get_lose(self):
        return self.lose

    def get_game_board(self):
        return self.game_board

    # ----------setters--------

    def set_game_board(self, size, min_num):
        self.game_board = Board(size, min_num)

    def set_lose(self, value):
        if type(value) != bool:
            return
        self.lose = value


class Board:
    """
    Class for build the game board from size that the user ask,
    adding neighbors and mines
    """
    def __init__(self, size=4, num_of_mines=8):
        self.size = size
        self.num_of_mines = num_of_mines
        self.this_board = self._create_board
        self.populate()
        self.add_neighbors()

    def show_all_squares(self, row, col):  # recursive
        if not 0 <= row < self.size or not 0 <= col < self.size:
            return
        if self.this_board[row][col].get_neighbor_mines() > 0:
            self.this_board[row][col].set_hidden(False)
            return
        if self.this_board[row][col].get_hidden() is True and \
                self.this_board[row][col].get_has_mine() is not True:
            self.this_board[row][col].set_hidden(False)
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    self.show_all_squares(row + i, col + j)

    @property
    def _create_board(self):
        """
        List comprehension for minesweeper square, Defines a slot on the board.
        :return:
        """
        return [[MSSquare() for _ in range(self.size)] for _ in range(self.size)]

    def populate(self):
        counter = self.num_of_mines
        while counter > 0:
            x, y = randint(0, self.size - 1), randint(0, self.size - 1)
            if self.this_board[x][y].get_has_mine():
                continue
            self.this_board[x][y].set_has_mine(True)
            counter -= 1

    def add_neighbors(self):
        """
        Adding neighbors around th mines.
        """
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.this_board[row][col].get_has_mine():
                    for i in range(-1, 2, 1):
                        for j in range(-1, 2, 1):
                            if not 0 <= col + j < self.size or not 0 <= row + i < self.size:
                                continue
                            if not self.this_board[row + i][col + j].get_has_mine():
                                self.this_board[row + i][col + j].set_neighbor_mines(1)

    def get_size(self):
        return self.size

    def get_num_of_mines(self):
        return self.num_of_mines

    def set_size(self, value):
        self.size = value

    def set_num_of_mines(self, value):
        self.num_of_mines = value

    def __str__(self):
        """
        Build the game board for user request size.
        :return: `s` is the game board
        """
        s = ""
        for row in range(self.size):
            s += " +---+" + "---+" * (self.size - 1) + "\n"
            s += f"{row + 1}|"
            for col in range(self.size):
                s += f" {self.this_board[row][col]} |"
            s += '\n'
        s += " +---+" + "---+" * (self.size - 1) + "\n"
        for i in range(1, self.size + 1):
            s += f"   {i}"
        return s


class MSSquare:
    """
    Class that defines a slot in the board.
    """
    def __init__(self, has_mine=False, hidden=True, neighbor_mines=0):
        self._has_mine = has_mine
        self._hidden = hidden
        self._neighbor_mines = neighbor_mines

    def get_has_mine(self):
        return self._has_mine

    def get_hidden(self):
        return self._hidden

    def get_neighbor_mines(self):
        return self._neighbor_mines

    def set_has_mine(self, value):
        if type(value) != bool:
            raise Exception("Only boolean type can go here!")
        self._has_mine = value
        return self._has_mine

    def set_hidden(self, value):
        self._hidden = value

    def set_neighbor_mines(self, value):
        self._neighbor_mines += value

    def __str__(self):
        if self.get_hidden():
            return " "
        if self.get_has_mine() and not self.get_hidden():
            return "x"
        return f"{self.get_neighbor_mines()}"


def main():

    while True:
        n = -1
        mines = -1
        # while not 4 <= n <= 9:
        while n > 9 or n < 4:
            n = input("To start MineSweeper, choose board size (4 - 9): ")
            if not n.isdigit() or len(n) != 1:
                n = -1
                continue
            n = int(n)

        while not 1 <= mines <= 2 * n:
            mines = input(f"Choose the number of mines (1 - {n * 2}): ")
            if not mines.isdigit() or (len(mines) > 2):
                mines = -1
                continue
            mines = int(mines)

        player_name = input("Please enter your name: ")
        current_game_board = Board(n, mines)
        game = GamePlay()
        game.game_board = current_game_board
        print(game.game_board)

        while game.lose is not True and game.win is not True:
            player_move = input("Enter coordinates (n,m): ")
            if len(player_move) != 3 or not player_move[0].isdigit() or not player_move[2].isdigit() or int(
                    player_move[0]) > game.game_board.get_size() or int(player_move[2]) > game.game_board.get_size():
                continue
            row, col = player_move[0], player_move[2]
            game.player_move(row, col)
            game.check_win()
            game.expose()
            print(game.game_board)
        if game.lose:
            print(f"NICE TRY {player_name.upper()}, MAYBE NEXT TIME...\n")
        if game.win:
            print(f"CONGRATULATIONS {player_name.upper()}!!! YOU ARE THE WINNER!\n")
        another_game = "?"
        while another_game != "Y" and another_game != "N":
            another_game = input("Would you like to play again? [Y/N]: ").upper()
        if another_game == "Y":
            continue

        break

    print("Thanks for playing MineSweeper")


if __name__ == "__main__":
    main()
