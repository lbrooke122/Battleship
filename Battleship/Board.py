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
        self.boatsPlaced1 = 0
        self.game_board_player2 = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.boatsPlaced2 = 0

    
    def draw(self, gameDisplay, screenWidth = 0):
        gameDisplay.fill(white)
        #create player 1 board
        print(self.turn)
        if self.turn:
            for row in range(self.ROWS):
                x_pos = row * self.GRID_SIZE
                for col in range(self.COLS):
                    y_pos = col * self.GRID_SIZE
                    if self.game_board_player1[row][col] == 1:
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
        #create player 2 board
        else:
            for row in range(self.ROWS):
                x_pos = row * self.GRID_SIZE
                for col in range(self.COLS):
                    y_pos = col * self.GRID_SIZE
                    if self.game_board_player2[row][col] == 1:
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
    
    def add_ships_to_board(self, event, wTurn):
        self.turn = wTurn
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                row, col = x // self.GRID_SIZE, y // self.GRID_SIZE
                if self.turn:
                    self.game_board_player1[row][col] = 1
                    self.boatsPlaced1 += 1
                else:
                    self.game_board_player2[row][col] = 1
                    self.boatsPlaced2 += 1