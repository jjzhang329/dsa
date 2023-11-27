# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Approach: 4 directions, left->right, top->down, right->left, down->up
# keep track of loop, for example, if it is 4 X 4 matrix, it will be 2 loop to fill all 
# if it is 3 X 3 matrix, it only needs 1 loop, so loop = n // 2


def generateMatrix(n):
    
    startx, starty = 0, 0 #initialize row and col
    loop, mid = n//2, n//2 #keep track of loop, and center point if n is odd number
    matrix = [[0] * n for _ in range(n)] #initialize matrix
    val = 1 #number
    for offset in range(1, loop+1): 
        # fill in left->right
        for i in range(starty, n-offset):
            matrix[startx][i] = val
            val += 1
        #fill in top->down
        for i in range(startx, n-offset):
            matrix[i][n-offset] = val 
            val += 1
        #fill in right->left
        for i in range(n-offset, starty, -1):
            matrix[n-offset][i] = val 
            val += 1
        #fill in bottom->top
        for i in range(n-offset, startx, -1):
            matrix[i][starty] = val 
            val += 1

        startx += 1
        starty += 1
    
    if n % 2 != 0:
        matrix[mid][mid] = n*n 

    return matrix

print(generateMatrix(4))
