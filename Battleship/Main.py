import pygame
from Board import Board
from Game import Game
from Player import Player

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
white,black,red = (255,255,255),(0,0,0),(255,0,0)

class BattleShip:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
        self.rectAI = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 10, 10)
        self.rectGame = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+20, 10, 10)
        self.font = pygame.font.Font(None, 36)
        self.aiText = font.render("Play Computer", True, white)
        self.gameText = font.render("Play Opponent", True, white)
    
    def drawStart(self):
        text_AIrect = self.aiText.get_rect()
        text_Grect = self.gameText.get_rect()
        text_AIrect.center = self.rectAI.center
        text_Grect.center = self.rectGame.center
        pygame.draw.rect(self.screen, black, text_AIrect)
        pygame.draw.rect(self.screen, black, text_Grect)

    def _draw(self, board, playingGame, placingShips, game):
        if start:
            pass
        elif placingShips:
            board.draw(self.screen, placingShips, SCREEN_WIDTH)
        else:
            game.draw(self.screen, playingGame, board)
        
        pygame.display.update()
    
    def _place_ships(self, board):
        board.add_ships_to_board()
    
    #main game loop
    def main(self, ws0, ws1):
        board = Board(ws0, ws1)
        game = Game()
        playerAI = Player(30, {})
        start = False
        placingShips = True
        playingGame = False
        countingShips = False
        playingComputer = False

        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                
                if not start:
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        if self.event.button == 1:
                            x, y = pygame.mouse.get_pos()
                            if self.rectAI.collidepoint(x, y):
                                playingComputer, start = True, True
                            if self.rectGame.collidepoint(x, y):
                                playingGame = True, start = True

                elif not game.is_game_over(board, placingShips):
                    if placingShips:
                        if self.event.type == pygame.MOUSEBUTTONDOWN:
                            if self.event.button == 1:
                                self._place_ships(board)

                    if board.get_ship_num() == 20 and not playingGame and not playingComputer: 
                        placingShips, playingGame, countingShips = False, True, True
                    elif board.get_ship_num() == 20 and not playingGame and playingComputer:
                        placingShips, countingShips = False, True

                    if countingShips:
                        game.count_ships(board)
                        playerAI = Player(30, game.ship_locations)
                        countingShips = False
                    
                    if playingComputer:
                        playerAI.target_ships(board, game)

                    if playingGame:
                        game.shoot_at_ship(self.event, playingGame, board)
                    
                else:
                    game.message()
                    self.running = False
        
            self._draw(board, playingGame, placingShips, game)
            self.FPS.tick(60)

if __name__ == "__main__":
    window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Battleship")

    battleship = BattleShip(screen)
    battleship.main(window_size[0], window_size[1])

#Quit Pygame
pygame.quit()