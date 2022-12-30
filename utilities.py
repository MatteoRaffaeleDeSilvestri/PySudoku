# UTILITY FUNCTIONS

def offset(x, y):

    # Calculate the offset based on the position of the cell selected
    h_o = 1
    v_o = 1
    if x // 60 == 0 or (x // 60) % 3 == 0:
        h_o = 0
    if y // 60 == 0 or (y // 60) % 3 == 0:
        v_o = 0
    return h_o, v_o

def shifter(coord):

    # Round the offset calcutaled 
    top_shift = 0
    left_shift = 0
    if coord[0] % 3 == 0:
        top_shift = 2
    if coord[1] % 3 == 0:
        left_shift = 2
    return top_shift, left_shift

def validate(grid, number, x, y):

    # Validate the position of given number based on the rule of sudoku (row, column and region) 
    to_check = set()
    for i in range(9):
        to_check.add((x, i))
        to_check.add((i, y))
        to_check.add(((3 * (x // 3)) + i // 3, (3 * (y // 3)) + i % 3))
    for coord in to_check.difference({(x, y)}):
        if grid[coord] == number:
            return False
    return True

def time_format(value):
    
    # Format the input value into hh:mm:ss format
    if ((value // 60) // 60) % 60 > 99:
        return '--:--:--'
    sec = str(value % 60)
    if int(sec) <= 9:
        sec = '0' + str(sec)
    mnt = str((value // 60) % 60)
    if int(mnt) <= 9:
        mnt = '0' + str(mnt)
    hr = str(((value // 60) // 60) % 60)
    if int(hr) <= 9:
        hr = '0' + str(hr)
    return hr + ':' + mnt + ':' + sec

def data_format(data):

    # Convert data into an appropriate format
    if len(data[data.index('.') + 1 : ]) > 3:
        data = data[ : data.index('.') + 1] + data[data.index('.') + 1 : data.index('.') + 4]
    if len(data) < 6:
        if data[1] == '.':
            data = '0' + data
        while len(data) < 6:
            data = data + '0'
    return data + 'sec'

def gen_solve_time_format(time_data):
    if int(time_data) > 60:
        return '> 1 min'
    else:
        if time_data < 0.001:
            return '< 0.001ms'
        else:
            if int(time_data) < 10:
                return str(time_data)[:5] + 'sec'
            else:
                return str(time_data)[:6] + 'sec'

def longest_game(stored_time, new_time):

    # Compare time and select the longest one
    if stored_time == new_time or stored_time == '--:--:--':
        return stored_time

    st_h, st_m, st_s = stored_time.split(':')
    nt_h, nt_m, nt_s = new_time.split(':')
    
    if int(st_h) > int(nt_h):
        return stored_time
    elif int(st_h) < int(nt_h):
        return new_time
    else:
        if int(st_m) > int(nt_m):
            return stored_time
        elif int(st_m) < int(nt_m):
            return new_time
        else:
            if int(st_s) > int(nt_s):
                return stored_time
            elif int(st_s) < int(nt_s):
                return new_time

def shortest_game(stored_time, new_time):

    # Compare time and select the shortest one
    if stored_time == new_time or stored_time == '00:00:00':
        return stored_time

    st_h, st_m, st_s = stored_time.split(':')
    nt_h, nt_m, nt_s = new_time.split(':')
    
    if int(st_h) < int(nt_h):
        return stored_time
    elif int(st_h) > int(nt_h):
        return new_time
    else:
        if int(st_m) < int(nt_m):
            return stored_time
        elif int(st_m) > int(nt_m):
            return new_time
        else:
            if int(st_s) < int(nt_s):
                return stored_time
            elif int(st_s) > int(nt_s):
                return new_time

'''
KEEP THIS INFO FOR FUTURE REFERENCES

Relation between sudoku cells and screen pixels:

grid_pixel_relation = {(0, 0): (22, 22, 58, 58), 
                 (0, 1): (81, 22, 59, 58),
                 (0, 2): (141, 22, 59, 58),
                 (0, 3): (202, 22, 58, 58),
                 (0, 4): (261, 22, 59, 58),
                 (0, 5): (321, 22, 59, 58),
                 (0, 6): (382, 22, 58, 58),
                 (0, 7): (441, 22, 59, 58),
                 (0, 8): (501, 22, 59, 58),
                 (1, 0): (22, 81, 58, 59),
                 (1, 1): (81, 81, 59, 59),
                 (1, 2): (141, 81, 59, 59),
                 (1, 3): (202, 81, 58, 59),
                 (1, 4): (261, 81, 59, 59),
                 (1, 5): (321, 81, 59, 59),
                 (1, 6): (382, 81, 58, 59),
                 (1, 7): (441, 81, 59, 59),
                 (1, 8): (501, 81, 59, 59),
                 (2, 0): (22, 141, 58, 59),
                 (2, 1): (81, 141, 59, 59),
                 (2, 2): (141, 141, 59, 59),
                 (2, 3): (202, 141, 58, 59),
                 (2, 4): (261, 141, 59, 59),
                 (2, 5): (321, 141, 59, 59),
                 (2, 6): (382, 141, 58, 59),
                 (2, 7): (441, 141, 59, 59),
                 (2, 8): (501, 141, 59, 59),
                 (3, 0): (22, 202, 58, 58),
                 (3, 1): (81, 202, 59, 58),
                 (3, 2): (141, 202, 59, 58),
                 (3, 3): (202, 202, 58, 58),
                 (3, 4): (261, 202, 59, 58),
                 (3, 5): (321, 202, 59, 58),
                 (3, 6): (382, 202, 58, 58),
                 (3, 7): (441, 202, 59, 58),
                 (3, 8): (501, 202, 59, 58),
                 (4, 0): (22, 261, 58, 59),
                 (4, 1): (81, 261, 59, 59),
                 (4, 2): (141, 261, 59, 59),
                 (4, 3): (202, 261, 58, 59),
                 (4, 4): (261, 261, 59, 59),
                 (4, 5): (321, 261, 59, 59),
                 (4, 6): (382, 261, 58, 59),
                 (4, 7): (441, 261, 59, 59),
                 (4, 8): (501, 261, 59, 59),
                 (5, 0): (22, 321, 58, 59),
                 (5, 1): (81, 321, 59, 59),
                 (5, 2): (141, 321, 59, 59),
                 (5, 3): (202, 321, 58, 59),
                 (5, 4): (261, 321, 59, 59),
                 (5, 5): (321, 321, 59, 59),
                 (5, 6): (382, 321, 58, 59),
                 (5, 7): (441, 321, 59, 59),
                 (5, 8): (501, 321, 59, 59),
                 (6, 0): (22, 382, 58, 58),
                 (6, 1): (81, 382, 59, 58),
                 (6, 2): (141, 382, 59, 58),
                 (6, 3): (202, 382, 58, 58),
                 (6, 4): (261, 382, 59, 58),
                 (6, 5): (321, 382, 59, 58),
                 (6, 6): (382, 382, 58, 58),
                 (6, 7): (441, 382, 59, 58),
                 (6, 8): (501, 382, 59, 58),
                 (7, 0): (22, 441, 58, 59),
                 (7, 1): (81, 441, 59, 59),
                 (7, 2): (141, 441, 59, 59),
                 (7, 3): (202, 441, 58, 59),
                 (7, 4): (261, 441, 59, 59),
                 (7, 5): (321, 441, 59, 59),
                 (7, 6): (382, 441, 58, 59),
                 (7, 7): (441, 441, 59, 59),
                 (7, 8): (501, 441, 59, 59),
                 (8, 0): (22, 501, 58, 59),
                 (8, 1): (81, 501, 59, 59),
                 (8, 2): (141, 501, 59, 59),
                 (8, 3): (202, 501, 58, 59),
                 (8, 4): (261, 501, 59, 59),
                 (8, 5): (321, 501, 59, 59),
                 (8, 6): (382, 501, 58, 59),
                 (8, 7): (441, 501, 59, 59),
                 (8, 8): (501, 501, 59, 59)}

Formula for coordinate of each square:

(22 - utilities.offset(pygame.mouse.get_pos()[0] - 20, pygame.mouse.get_pos()[1] - 20)[0] + ((pygame.mouse.get_pos()[0] - 20) // 60) + 58 * ((pygame.mouse.get_pos()[0] - 20) // 60) + ((pygame.mouse.get_pos()[0] - 20) // 60), 22 - utilities.offset(pygame.mouse.get_pos()[0] - 20, pygame.mouse.get_pos()[1] - 20)[1] + ((pygame.mouse.get_pos()[1] - 20) // 60) + 58 * ((pygame.mouse.get_pos()[1] - 20) // 60) + ((pygame.mouse.get_pos()[1] - 20) // 60), 58 + utilities.offset(pygame.mouse.get_pos()[0] - 20, pygame.mouse.get_pos()[1] - 20)[0], 58 + utilities.offset(pygame.mouse.get_pos()[0] - 20, pygame.mouse.get_pos()[1] - 20)[1])
'''
