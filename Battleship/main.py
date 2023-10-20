import pygame
from Board import Board
from Game import Game

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
turn = True

class BattleShip:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.placingShips = True
        self.playing = False
        self.FPS = pygame.time.Clock()
    
    def _draw(self, board):
        board.draw(self.screen, SCREEN_WIDTH)
        pygame.display.update()
    
    def _place_ships(self, board, event):
        board.add_ships_to_board(event, turn)
    
    #main game loop (takes dim of board)
    def main(self, window_width, window_height, event, board):
        if self.placingShips:
            self._place_ships(board, event)
        #game = Game()
        self._draw(board)

if __name__ == "__main__":
    running = True
    window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    board = Board(window_size[0], window_size[1])
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Battleship")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        battleship = BattleShip(screen)
        battleship.main(window_size[0], window_size[1], event, board)
        if board.boatsPlaced1 >= 5:
            turn = False

#Quit Pygame
pygame.quit()