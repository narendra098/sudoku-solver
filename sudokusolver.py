# ------------sudoku solver using python ----------------

#taking an example sudoku puzzle

sudoku = [
         [0, 0, 0, 0, 0, 0, 6, 8, 8],
         [0, 0, 0, 0, 7, 3, 0, 0, 9], 
         [3, 0, 9, 0, 0, 0, 0, 4, 5],
         [4, 9, 0, 0, 0, 0, 0, 0, 0], 
         [8, 0, 3, 0, 5, 0, 9, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 3, 6],
         [9, 6, 0, 0, 0, 0, 3, 0, 8], 
         [7, 0, 0, 6, 8, 0, 0, 0, 0],
         [0, 2, 8, 0, 0, 0, 0, 0, 0]
        ]
        

# a helper function to check a right number
def is_valid_move(grid, row, col, number):
    
    #check if number is in row
    for x in range(9):
        if grid[row][x] == number:
            return False
    # check if number is in column        
    for x in range(9):
        if grid[x][col] == number:
            return False
    
    #check if number is in grid
    corner_row = row - row%3
    corner_col = col - col%3 
    
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y]==number:
                return False
    
    return True 
    
    
    
def solve(grid, row, col):
    # if col and row is at the end then True because sudoku was solved or else moving to next row and first col
    if col == 9:
        if row == 8:
            return True 
        row += 1 
        col = 0
    
    # if grid[row][col] have some value then moving to next column at that row   
    if grid[row][col]>0:
        return solve(grid, row, col+1)
     
    # check for a right value num at the row and col    
    for num in range(1,10):
        
        #if num is valid then setting num to that position
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            # calling back our solve function by shifting to next column
            if solve(grid, row, col+1): 
                return True 
        # if none of the value fits then setting num at row, col  =0      
        grid[row][col] = 0
    # if the grid can not be solved then return False
    return False
    
    
#printing our unsolved sudoku     
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end= " ")
    print()

print('------------------------------')

# printing our solved sudoku puzzle
if solve(sudoku, 0, 0):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end= " ")
        print()
        
# if solve function return False then NO SOLUTION
else:
    print("NO SOLUTION") 
    
            
            
            
            
    