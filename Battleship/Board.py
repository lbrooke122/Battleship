import pygame
#set color with rgb
white,black,red = (255,255,255),(0,0,0),(255,0,0)

class Board:
    def __init__(self, width, height):
        self.GRID_SIZE = width//10
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.ROWS, self.COLS = width//self.GRID_SIZE, height//self.GRID_SIZE
        self.BORDER_WIDTH, self.GRID_BORDER = 2, 20
        
        self.turn = True
        
        self.game_board_player1 = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
    
    def draw(self, gameDisplay, displayShips, screenWidth = 0):
        gameDisplay.fill(white)
        #create player 1 board
        for row in range(self.ROWS):
            x_pos = row * self.GRID_SIZE
            for col in range(self.COLS):
                y_pos = col * self.GRID_SIZE
                if self.game_board_player1[row][col] == 1 and displayShips:
                    pygame.draw.rect(gameDisplay, black, 
                                        (x_pos, y_pos, self.GRID_SIZE, self.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, self.GRID_SIZE, self.GRID_SIZE),
                                        self.BORDER_WIDTH)
                else:
                    pygame.draw.rect(gameDisplay, white,
                                        (x_pos, y_pos, self.GRID_SIZE, self.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                        (x_pos, y_pos, self.GRID_SIZE, self.GRID_SIZE),
                                        self.BORDER_WIDTH)

        pygame.display.update()
    
    def add_ships_to_board(self):
        x, y = pygame.mouse.get_pos()
        row, col = x // self.GRID_SIZE, y // self.GRID_SIZE
        self.game_board_player1[row][col] = 1
    
    def get_ship_num(self):
        temp = 0
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.game_board_player1[row][col] == 1:
                    temp += 1

        return temp