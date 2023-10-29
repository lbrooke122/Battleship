import pygame
import numpy as np

#player that fires shots based on the likelihood that any ship is in a given location
class Player:
    def __init__(self, hits, ships):
        self.hits = hits
        self.ships = ships
        self.ships_sizes = set([size for size in self.ships])
        self.targets = {}
        self.target_map = np.zeros([10, 10])
        self.shots_fired = np.zeroes([10, 10])
    
    #checks if a potential ship location has not already been fired at
    def not_hit(self, srow, erow, scol, ecol):
        check = 0
        for row in range(srow, erow, 1):
            for col in range(scol, ecol, 1):
                check += self.shots_fired[row][col]
                if check > 0: return False
        
        return True

    def mk_target_map(self):
        target_map = np.zeroes([10, 10])
        for ship_size in self.ships_sizes:
            current_size = ship_size - 1
            for row in range(10):
                for col in range(10):
                    ship_loc = []
                    if self.shots[row][col] != 1:
                        if row - current_size >= 0:
                            ship_loc.append((row-current_size, col), (row + 1, col + 1))
                        if row + current_size < 10:
                            ship_loc.append((row, col), (row+current_size+1, col+1))
                        if col - current_size >= 0:
                            ship_loc.append((row, col-current_size), (row + 1, col + 1))
                        if col + current_size < 10:
                            ship_loc.append((row, col), (row+1, col+current_size+1))
                    
                        for (srow, scol), (erow, ecol) in ship_loc:
                            if self.not_hit(srow, erow, scol, ecol):
                                target_map[srow:erow, scol:ecol] += 1
        return target_map
    
    #removes ship size from possible sizes if it has been sunk
    def remove_ships(self):
        for ship in self.ships:
            locations = self.ships[ship]
            count = 0
            for row, col in locations:
                count  += self.shots_fired[row][col]
            if count == ship:
                self.ships_sizes.remove(count)

    def in_range(self, board, r, c):
        return r >= 0 and r < board.COLS and c >= 0 and c < board.ROWS 
    
    #determines if current ship is horizontal
    def is_horizontal(self, board, old_row, old_col):
        row_left, row_right = old_row - 1, old_row + 1
        check = False
        if self.in_range(board, row_left, 0):
            check |= (board[old_row][old_col] == 1 & board[row_left][old_col] == 1)
        if self.in_range(board, row_right, 0):
            check |= (board[old_row][old_col] == 1 & board[row_right][old_col] == 1)
        return check
    
    #determines if current ship is vertical
    def is_vertical(self, board, old_row, old_col):
        col_up, col_down = old_col - 1, old_col + 1
        check = False
        if self.in_range(board, 0, col_up):
            check |= (board[old_row][old_col] == 1 & board[old_row][col_up] == 1)
        if self.in_range(board, 0, col_down):
            check |= (board[old_row][old_col] == 1 & board[old_row][col_down] == 1)
        return check

    #adds possible adjacent locations to targets
    def add_adj(self, board, row, col):
        dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        horizontal_check = self.is_horizontal(board, row, col)
        vertical_check = self.is_vertical(board, row, col)
        if horizontal_check: dist = [(-1, 0), (1, 0)]
        if vertical_check: dist = [(0, -1), (0, 1)]
        for d in dist:
            x, y = row + d[0], col + d[1]
            if self.in_range(board, x, y):
                self.targets.push((x, y))
                self.target_map[x][y] = 0

    #selects next likely target given that a ship has been sunk
    def select_target(self):
        self.remove_ships()
        self.target_map = self.mk_target_map()
        next_row, next_col = 0, 0
        temp_prob = -1

        for row in range(10):
            for col in range(10):
                if self.target_map[row][col] > temp_prob:
                    temp_prob = self.target_map[row][col]
                    next_row, next_col = row, col
        
        return next_row, next_col
    
    #shoots at ships
    def target_ships(self, board, game):
        if not self.targets:
            guess_row, guess_col = self.select_target(board)
        else:
            guess_row, guess_col = self.targets.pop()
        
        if board.game_board_player1[guess_row][guess_col] == 1:
            game.shots -= 1
            board.game_board_player1[guess_row][guess_col] = -1
            self.shots_fired[guess_row][guess_col] = 1
            self.add_adj(board, guess_row, guess_col)
        else:
            board.game_board_player1[guess_row][guess_col] = 2
            self.shots_fired[guess_row][guess_col] = 1

        return guess_row, guess_col
        