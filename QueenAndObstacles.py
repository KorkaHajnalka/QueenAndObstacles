import numpy as np


def AttackablePlaces(SizeOfChessboard, QueenPosition, ObstaclesPositions):

    # This function calculates a matrix (called CBMatrix) which shows attackable places. 
    # An element of CBMatrix is 0 if a place that this element represents is not attackable, and 1 if it is attackable.

    # Initialize CBMatrix:
    CBMatrix = np.zeros((SizeOfChessboard, SizeOfChessboard))

    # Get coordinates of Queen's position:
    rq = QueenPosition[0]
    cq = QueenPosition[1]

    # Attackable fields can be identified with help of four conditions, which determines CBMatrix without any obstacles.
    for i in range(SizeOfChessboard):
        for j in range(SizeOfChessboard):
            
            if(i == rq or j == cq or i+j == rq+cq or i-j == rq-cq):
                CBMatrix[i,j] = 1
            else:
                CBMatrix[i,j] = 0

    # CBMatrix is modified in the second step when obstacles are taken into account.
    # Iterate over obstacles
    for k in range(len(ObstaclesPositions)):
        ro = ObstaclesPositions[k][0]
        co = ObstaclesPositions[k][1]
        
        # Case of vertical obstacles 
        if(ro == rq):
            if(co < cq):
                for i in range(co + 1): CBMatrix[ro,i] = 0
            else: 
                for i in range(co, SizeOfChessboard,1): CBMatrix[ro,i] = 0

        # Case of horizontal obstacles
        if(co == cq):
            if(ro < rq):
                for i in range(rq + 1): CBMatrix[i,co] = 0
            else: 
                for i in range(ro, SizeOfChessboard,1): CBMatrix[i,co] = 0 

        # Case of diagonal obstacles in direction up or down right
        if(ro + co == rq + cq):
           i = ro
           j = co
           if(ro < rq):
               while(i >= 0 and j < SizeOfChessboard):
                   CBMatrix[i][j] = 0
                   i= i-1
                   j= j+1
           else:
                while(i < SizeOfChessboard and j >=0):
                   CBMatrix[i][j] = 0
                   i=i+1
                   j=j-1

        # Case of diagonal obstacles in direction up or down left
        if(ro - co == rq - cq):
           i = ro
           j = co
           if(ro < rq):
               while(i >= 0 and j>=0 ):
                   CBMatrix[i][j] = 0
                   i=i-1
                   j=j-1
           else:
                while(i < SizeOfChessboard and j < SizeOfChessboard):
                   CBMatrix[i][j] = 0
                   i=i+1
                   j=j+1

    # Number of attackable fields is the sum of nonzero elements of CBMatrix
    # Queen's position was treated as attackable position, so it is needed to subtrack 1
    NumberOfAttackableFields = np.count_nonzero(CBMatrix)-1      

    return NumberOfAttackableFields


SizeOfChessboard = 8
QueenPosition = [4,3]
ObstaclesPositions = [[5,4]]

AttackablePlaces(SizeOfChessboard, QueenPosition, ObstaclesPositions)