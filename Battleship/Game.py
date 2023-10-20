import pygame

class Game:
    def __init__(self):
        self.winner = None
    
    #checks if ships remain for both boards
    def ship_remain(self, board1, board2):
        ships1 = ships2 = 0
        for row in range(board1.board_size):
            for col in range(board1.board_size):
                tile1 = board1.get_tile_from_pos((row, col))
                tile2 = board2.get_tile_from_pos((row, col))
                
                if tile1.occupying_piece != None:
                    pass

                if tile2.occupying_piece != None:
                    pass
        
        return (ships1, ships2)
    
    #checks if the game is over and assigns winner
    def is_game_over(self, board1, board2):
        ships1, ships2 = self.ship_remain(board1, board2)

        if ships1 == 0: 
            self.winner = "player 1"
            return True
        if ships2 == 0: 
            self.winner = "player 2"
            return True
        
        return False

    def rum_game():
        revealed_tiles = 0 #contans list of tiles revealed by either user
        #list of ships which exist on board
        #list of available ships
        #add ships to board
        #tarck location of mouse
        #