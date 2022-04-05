DIRECTIONS = ['left', 'right', 'up', 'down']
import time
import collections
import DisplayHelpers

class Snake_Game:
    def __init__(self):
        self.board = {(Pos(x, y)) for x in range(self.WIDTH) for y in range(self.HEIGHT)}
        #We need a board to matrix function to display with
        
    def tickGame():

        DisplayHelpers.DisplayColorMatrix()
        time.sleep(.3)
class snake:
    def __init__(self):
        self.length = 4 #Default length = 4
        self.direction = 'right' 
        self.x_pos = 0
        self.y_pos = 0
        self.head_pos = [self.x_pos, self.y_pos]
        self.tail_positions = collections.deque()

