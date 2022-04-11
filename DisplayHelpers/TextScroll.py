from DisplayColorMatrix import DisplayColorMatrix
import numpy as np
import AlphabetToGrid
import sys
import time
from rpi_ws281x import Color, PixelStrip, ws


board = np.zeros((12,12), int)

toPrint = "hello world  "
toPrint = toPrint.upper()

nextGrid = []
for x in toPrint:
    nextGrid.append(np.array(AlphabetToGrid.getLetterGrid(x)))

#%%
blue = Color(0,0,255)
blank = Color(0,0,0)
colorBoard =  [[0 for j in range(12)] for i in range(12)]
while(True):
    time.sleep(1)
    for x in nextGrid:    
        for y in x.transpose():
            time.sleep(.1)
            #So sloppy but I dont feel like automating
            board[:,0] = board[:,1]
            board[:,1] = board[:,2]
            board[:,2] = board[:,3]
            board[:,3] = board[:,4]
            board[:,4] = board[:,5]
            board[:,5] = board[:,6]
            board[:,6] = board[:,7]
            board[:,7] = board[:,8]
            board[:,8] = board[:,9]
            board[:,9] = board[:,10]
            board[:,10] = board[:,11] 
            board[:,11] = y
            
            
            
            for i in range(12):
                for j in range(12):
                    if board[i][j].any() == 1:
                        colorBoard[i][j] = blue
                    else:
                        colorBoard[i][j] = blank
                    
            display_color_matrix(colorBoard)


