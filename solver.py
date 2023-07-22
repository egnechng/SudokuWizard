board = [ 
    [1,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
# i - row
# j - col

def validate_board(board):

    # check rows
    for row in board: 
        if not valid_set(row):
            return False
        
    # check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not valid_set(column):
            return False
        
    # check grids
    for i in range(0,9,3):
        for j in range(0,9,3):
            grid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not valid_set(grid):
                return False
            
    return True

def valid_set(nums):
    num_set = set()
    for num in nums:
        if num != 0 and num in num_set:
            return False
        num_set.add(num)
    return True

def solve(board):

    # base case
    empty = find_empty(board)
    if not empty: # solution found
        return True
    else:
        row, col = empty 
    
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            # backtrcking
            board[row][col] = 0
    
    return False
    


def is_valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] !=i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] !=i:
            return False

    # Check box
    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(y *3, y*3 + 3):
        for j in range(x *3, x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end ="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j
    
    return None
