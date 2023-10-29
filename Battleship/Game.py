import pygame
import copy

white,black,red = (255,255,255),(0,0,0),(255,0,0)

class Game:
    def __init__(self):
        self.winner = None
        self.shots = 30
        self.ship_locations = {}
    
    def ship_remain(self, board):
        ships = 0
        for row in range(board.ROWS):
            for col in range(board.COLS):
                if board.game_board_player1[row][col] == 1:
                    ships += 1
        return ships
    
    def count_ships(self, board):
        board_temp = copy.deepcopy(board)
        def dfs(row, col, width = board.GRID_SIZE, height = board.GRID_SIZE):
            if 0 <= row < height and 0 <= col < width and board_temp[row][col] == 1:
                board_temp[row][col] = 0 #since we have seen this part of the ship already, change it to not ship
                temp_ship.append((row, col))
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        for row in range(board.GRID_SIZE):
            for col in range(board.GRID_SIZE):
                temp_ship = []
                dfs(row, col)
                self.ship_locations[len(temp_ship)] = temp_ship

    def is_game_over(self, board, placingShips):
        ships = self.ship_remain(board)

        if ships == 0 and not placingShips: 
            self.winner = "player 2"
            return True
        if self.shots == 0: 
            self.winner = "player 1"
            return True
        
        return False

    def shoot_at_ship(self, event, do, board):
        if do:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    row, col = x // board.GRID_SIZE, y // board.GRID_SIZE
                    check = board.game_board_player1[row][col]
                    if check == 1:
                        board.game_board_player1[row][col] = -1
                        self.shots -= 1
                    elif check == 2 or check == -1: check = check
                    else: 
                        board.game_board_player1[row][col] = 2
                        self.shots -= 1
    
    def draw(self, gameDisplay, displayShots, board, screenWidth = 0):
        for row in range(board.ROWS):
            x_pos = row * board.GRID_SIZE
            for col in range(board.COLS):
                y_pos = col * board.GRID_SIZE
                if board.game_board_player1[row][col] == -1 and displayShots:
                    pygame.draw.rect(gameDisplay, black, 
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE),
                                        board.BORDER_WIDTH)
                elif board.game_board_player1[row][col] == 2 and displayShots:
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE),
                                        board.BORDER_WIDTH)
                else:
                    pygame.draw.rect(gameDisplay, white,
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, board.GRID_SIZE, board.GRID_SIZE),
                                        board.BORDER_WIDTH)
        pygame.display.update()
    
    def message(self):
        print(f"{self.winner} wins!")