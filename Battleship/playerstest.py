import pygame

pygame.init()

#set color with rgb
white,black,red = (255,255,255),(0,0,0),(255,0,0)

class Board:
    def __init__(self, ships_num):
        self.WIDTH, self.HEIGHT, self.GRID_SIZE = 800, 600, 20
        self.ROWS, self.COLS = self.WIDTH // self.GRID_SIZE, self.HEIGHT // self.GRID_SIZE
        self.BORDER_WIDTH = 5

        self.ships_num = ships_num
        
        self.turn = "player 1"
        
        self.game_board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

        #self._setup() #sets starting position 
    
    def draw(self, gameDisplay):
        gameDisplay.fill(white)
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.game_board[row][col] == 1:
                    pygame.draw.rect(gameDisplay, black, 
                                     (row * self.GRID_SIZE, col * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
                    pygame.draw.rect(gameDisplay, red, 
                                     (row * self.GRID_SIZE, col * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
                else:
                    pygame.draw.rect(gameDisplay, white,
                                     (row * self.GRID_SIZE, col * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE),
                                     self.BORDER_WIDTH)
                    pygame.draw.rect(gameDisplay, red, 
                                     (row * self.GRID_SIZE, col * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE),
                                     self.BORDER_WIDTH)
        pygame.display.update()

pygame.init()

class BattleShip:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
    
    def _draw(self, board):
        board.draw(self.screen)
        pygame.display.update()
    
    #main game loop (takes dim of board)
    def main(self, window_width, window_height):
        board = Board(5)
        #game = Game()
        self._draw(board)

if __name__ == "__main__":
    window_size = (640, 640)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Battleship")
    battleship = BattleShip(screen)
    battleship.main(window_size[0], window_size[1])
