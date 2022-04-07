from DisplayHelpers.DisplayColorMatrix import DisplayColorMatrix
import numpy as np
import AlphabetToGrid
import sys
import time

board = np.zeros((12,12), np.int8)

toPrint = "hi"
toPrint = toPrint.upper()

for x in toPrint:
    print(x)
    
#%%



nextGrid = []
for x in toPrint:
    nextGrid.append(np.array(AlphabetToGrid.getLetterGrid(x)))

#%%
for x in nextGrid:
    print(x)
    
    for y in x.transpose():
        time.sleep(.2)
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
        print(board)

#%%
board[10][11] = 1
board[:,6] = board[:,7]
board[:,7] = board[:,8]
board[:,8] = board[:,9]
board[:,9] = board[:,10]
board[:,10] = board[:,11]
DisplayColorMatrix(board)
