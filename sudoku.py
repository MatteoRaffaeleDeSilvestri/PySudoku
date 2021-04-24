from random import choice, shuffle
from time import time
from copy import deepcopy

# VARIABLES

list_num = [x for x in range(1, 10)]
difficult_level = {'easy': [i for i in range(40, 46)], 'medium': [i for i in range(46, 57)], 'hard': [i for i in range(57, 64)]}

# SUDOKU FUNCTIONS

def grid_generator(grid):

    # Generate a valid sudoku board completely filled
    found = zero_finder(grid)
    
    if not(bool(found)):
        return True
    
    shuffle(list_num)
    
    for n in list_num:
    
        if fill(grid, found[0], found[1], n):
            grid[found[0]][found[1]] = n
    
            if grid_generator(grid):
                return True
    
            grid[found[0]][found[1]] = 0

def solve(sudoku):

    # Solve a given sudoku
    found = zero_finder(sudoku)
    
    if not(bool(found)):
        return True
    
    for n in range(1, 10):
        if fill(sudoku, found[0], found[1], n):
            sudoku[found[0]][found[1]] = n
    
            if solve(sudoku):
                return True
    
            sudoku[found[0]][found[1]] = 0
    
    return False

def zero_finder(grid):

    # Search the first zero in the sudoku grid
    for line in grid:
        if 0 in line:
            return grid.index(line), line.index(0)
    return False

def fill(sudoku, x, y, n):

    # Validate the position of the given number based on the rule of sudoku (row, column and region) 
    if n in sudoku[x]:
        return False
    
    for col in range(9):
        if sudoku[col][y] == n:
            return False
    
    for i in range(3):
        if n in sudoku[((x // 3) * 3) + i][(y // 3) * 3 : ((y // 3) * 3) + 3]:
            return False
    
    return True

def sudoku_maker(difficult):

    # Generate a valid sudoku board starting from a filled one 
    to_remove = choice(difficult_level[difficult])
    grid = [[0 for i in range(9)] for i in range(9)]
    grid_generator(grid)
    
    # Keep a copy of the solution for the final animation and for the hint function
    solution = dict()
    for i in range(81):
        solution.setdefault((i // 9, i % 9), grid[i // 9][i % 9])

    # Generate a sudoku with only one solution available
    to_check = [(i // 9, i % 9) for i in range(81)]
    removed = 0
    
    while to_check:
    
        removable = True
        
        copy_grid = deepcopy(grid)
            
        cell = choice(to_check)
        to_check.remove(cell)
        backup = copy_grid[cell[0]][cell[1]]
        
        list_num = [x for x in range(1, 10)]
        list_num.remove(backup)
        
        for num in list_num:
            copy_grid[cell[0]][cell[1]] = 0
        
            if fill(grid, cell[0], cell[1], num):
                copy_grid[cell[0]][cell[1]] = num
        
                if solve(copy_grid):
                    removable = False
                    break
        
        if removable:
            removed += 1
            grid[cell[0]][cell[1]] = 0
            if removed == to_remove:
                break
        
    # Avoid generating a grid with a number of removed pieces
    # different from the number of pieces to remove to have the 
    # selected level of difficult (restart the generation process if necessary)

    # Solve grid (for timing data purpose)
    solve_time_start = time()
    copy_grid = deepcopy(grid)
    solve(copy_grid)
    solve_time_end = time()

    # Convert the actual sudoku (matrix) in dict format
    sudoku = dict()

    for i in range(81):
        sudoku[(i // 9, i % 9)] = grid[i // 9][i % 9]

    return sudoku, solution, solve_time_end - solve_time_start

def solution_sequence(matrix, step_to_follow):

    # Generate the list of step to follow to find the solution 
    found = zero_finder(matrix)
    if not(bool(found)):
        return True
    
    for n in range(1, 10):
    
        if fill(matrix, found[0], found[1], n):
            matrix[found[0]][found[1]] = n
            step_to_follow.append(str(found[0]) + str(found[1]) + str(n))
    
            if solution_sequence(matrix, step_to_follow):
                return True
    
            matrix[found[0]][found[1]] = 0
            step_to_follow.append(str(found[0]) + str(found[1]) + str(0))
    
        else:
    
            step_to_follow.append(str(found[0]) + str(found[1]) + str(n))
    
            if n == 9:
                step_to_follow.append(str(found[0]) + str(found[1]) + str(0))
    
    return False

def animate_sol(grid):

    # Convert the given grid from dict to matrix (list of lists) 
    matrix = list(list(0 for i in range(9)) for i in range(9))
    
    for cell in grid.keys():
        matrix[cell[0]][cell[1]] = grid[cell]
    
    # Generate the step to follow for the animation
    step_to_follow = list()
    solution_sequence(matrix, step_to_follow)
    
    return step_to_follow

def static_solution(grid):
    
    # Convert the given grid from dict to matrix (list of lists)
    matrix = list(list(0 for i in range(9)) for i in range(9))
    to_check = list()
    
    for cell in grid.keys():
        matrix[cell[0]][cell[1]] = grid[cell]
        
        if grid[cell] == 0:
            to_check.append((cell[0], cell[1]))

    # Check if a solution is available (and calculate the time needed to find it)
    start_solve = time()
    
    if solve(matrix):
        end_solve = time()
        
        expected_solution = deepcopy(matrix)
        
        # Check if multiple solutions are available
        if multi_solution(matrix, to_check, expected_solution):
            return None, None, 2

        # Convert the solution from matrix (list of lists) to dict
        solution = dict()
        for i in range(81):
            solution[(i // 9, i % 9)] = matrix[i // 9][i % 9]
        
        return solution, end_solve - start_solve, 1
    
    else:
        
        return None, None, 0

def multi_solution(grid, to_check, expected_solution):

    # Generate a sudoku with only one solution available
    while to_check:
        
        removable = True
        
        copy_grid = deepcopy(grid)
        
        cell = choice(to_check)
        to_check.remove(cell)
        backup = copy_grid[cell[0]][cell[1]]

        list_num = [x for x in range(1, 10)]
        list_num.remove(backup)
        
        for num in list_num:
            copy_grid[cell[0]][cell[1]] = 0
            
            if fill(grid, cell[0], cell[1], num):
                copy_grid[cell[0]][cell[1]] = num
                solution = solve(copy_grid)
            
                if solution and copy_grid != expected_solution:
                    
                    # Another (different) solution is found
                    return True
    
    # No multiple solution avilable
    return False

# Unsolvable sudoku (for test pourpose only)
# [[2, 0, 0, 9, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 6, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0, 0]
#  [5, 0, 2, 6, 0, 0, 4, 0, 7],
#  [0, 0, 0, 0, 0, 4, 1, 0, 0],
#  [0, 0, 0, 0, 9, 8, 0, 2, 3],
#  [0, 0, 0, 0, 0, 3, 0, 8, 0],
#  [0, 0, 5, 0, 1, 0, 0, 0, 0],
#  [0, 0, 7, 0, 0, 0, 0, 0, 0]]
