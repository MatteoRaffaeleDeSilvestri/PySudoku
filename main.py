import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame, sudoku, utilities, data, pdf_gen
from time import sleep, time
from tkinter import Tk, messagebox
import webbrowser

# INITIALIZE PYGAME (and font sublibrary)

pygame.init()
pygame.font.init()

# SET WINDOW PROPRIETIES

FPS = 60
screen = pygame.display.set_mode((1000, 585))
pygame.display.set_caption('PySudoku')

# SET TEXT STYLE

field_label = pygame.font.Font('fonts/Ubuntu-Regular.ttf', 32)
animation_label = pygame.font.Font('fonts/Ubuntu-Italic.ttf', 22)
status_bar_label = pygame.font.Font('fonts/Ubuntu-Regular.ttf', 14)
ingame_stats_label = pygame.font.Font('fonts/Ubuntu-Regular.ttf', 28)
victory_label = pygame.font.Font('fonts/Ubuntu-Regular.ttf', 68)
stats_label = pygame.font.Font('fonts/Ubuntu-Regular.ttf', 23)

# DELAY VARIABLES

animation_delay = 0.1
start_end_delay = 0.5

# SET GAME VARIABLES

locked_cells = list()
free_cells = list()
grid_to_pixel = dict()
selected_cell = False
on_export = False
on_hint = False
on_quit = False
on_clear = False
on_solve = False
on_check = False
on_back = False
timer = -1
hinted = False
solved = False
checkbox_count = 0

background_color = (250, 250, 250)
black = (0, 0, 0)
selected_cell_color = (230, 230, 230)
adv_bar_color = (255, 238, 5)
winning_mark_color = ((255, 238, 5), (0, 0, 180))

# IMAGES FILE LOAD

logo = pygame.image.load('images/main_menu/logo.png')
menu = pygame.image.load('images/main_menu/menu.png')
play = pygame.image.load('images/main_menu/play.png')
play_over = pygame.image.load('images/main_menu/play_over.png')
play_msg = pygame.image.load('images/main_menu/play_msg.png')
solve = pygame.image.load('images/main_menu/solve.png')
solve_over = pygame.image.load('images/main_menu/solve_over.png')
solve_msg = pygame.image.load('images/main_menu/solve_msg.png')
stats = pygame.image.load('images/main_menu/stats.png')
stats_over = pygame.image.load('images/main_menu/stats_over.png')
stats_msg = pygame.image.load('images/main_menu/stats_msg.png')
github = pygame.image.load('images/main_menu/github.png')
github_over = pygame.image.load('images/main_menu/github_over.png')

set_difficult = pygame.image.load('images/difficult_menu/difficult.png')
easy = pygame.image.load('images/difficult_menu/easy.png')
easy_over = pygame.image.load('images/difficult_menu/easy_over.png')
medium = pygame.image.load('images/difficult_menu/medium.png')
medium_over = pygame.image.load('images/difficult_menu/medium_over.png')
hard = pygame.image.load('images/difficult_menu/hard.png')
hard_over = pygame.image.load('images/difficult_menu/hard_over.png')
back = pygame.image.load('images/difficult_menu/back.png')
back_over = pygame.image.load('images/difficult_menu/back_over.png')
generate_msg = pygame.image.load('images/difficult_menu/generating.png')

export_btn = pygame.image.load('images/game_items/export.png')
export_btn_over = pygame.image.load('images/game_items/export_over.png')
exporting_btn_over = pygame.image.load('images/game_items/exporting_over.png')
export_btn_disabled = pygame.image.load('images/game_items/export_disabled.png')
hint_btn = pygame.image.load('images/game_items/hint.png')
hint_btn_over = pygame.image.load('images/game_items/hint_over.png')
hint_btn_disabled = pygame.image.load('images/game_items/hint_disabled.png')
quit_btn = pygame.image.load('images/game_items/quit.png')
quit_btn_over = pygame.image.load('images/game_items/quit_over.png')
quit_btn_disabled = pygame.image.load('images/game_items/quit_disabled.png')
clear_btn = pygame.image.load('images/game_items/clear.png')
clear_btn_over = pygame.image.load('images/game_items/clear_over.png')
clear_btn_disabled = pygame.image.load('images/game_items/clear_disabled.png')
solve_btn = pygame.image.load('images/game_items/solve.png')
solve_btn_over = pygame.image.load('images/game_items/solve_over.png')
solve_btn_disabled = pygame.image.load('images/game_items/solve_disabled.png')
checkbox = pygame.image.load('images/game_items/checkbox.png')
checkbox_over = pygame.image.load('images/game_items/checkbox_over.png')
checkbox_checked = pygame.image.load('images/game_items/checkbox_checked.png')
checkbox_checked_over = pygame.image.load('images/game_items/checkbox_checked_over.png')
animation_msg = pygame.image.load('images/game_items/animation_msg.png')
stop = pygame.image.load('images/game_items/stop.png')
stop_over = pygame.image.load('images/game_items/stop_over.png')
note_play = pygame.image.load('images/game_items/play_note.png')

solve_text = pygame.image.load('images/game_items/solve_txt.png')
note_solve = pygame.image.load('images/game_items/solve_note.png')
solving_msg = pygame.image.load('images/game_items/solving_msg.png')
solved_msg = pygame.image.load('images/game_items/solved_msg.png')
no_solution_msg = pygame.image.load('images/game_items/no_solution_msg.png')
multiple_solution_msg = pygame.image.load('images/game_items/mulitple_solution_msg.png')

stats_background = pygame.image.load('images/stats_menu/stats_background.png')
clear_stats = pygame.image.load('images/stats_menu/clear_stats.png')
clear_stats_over = pygame.image.load('images/stats_menu/clear_stats_over.png')

locked_1 = pygame.image.load('images/numbers/locked/1.png')
locked_2 = pygame.image.load('images/numbers/locked/2.png')
locked_3 = pygame.image.load('images/numbers/locked/3.png')
locked_4 = pygame.image.load('images/numbers/locked/4.png')
locked_5 = pygame.image.load('images/numbers/locked/5.png')
locked_6 = pygame.image.load('images/numbers/locked/6.png')
locked_7 = pygame.image.load('images/numbers/locked/7.png')
locked_8 = pygame.image.load('images/numbers/locked/8.png')
locked_9 = pygame.image.load('images/numbers/locked/9.png')

free_1 = pygame.image.load('images/numbers/free/_1.png')
free_2 = pygame.image.load('images/numbers/free/_2.png')
free_3 = pygame.image.load('images/numbers/free/_3.png')
free_4 = pygame.image.load('images/numbers/free/_4.png')
free_5 = pygame.image.load('images/numbers/free/_5.png')
free_6 = pygame.image.load('images/numbers/free/_6.png')
free_7 = pygame.image.load('images/numbers/free/_7.png')
free_8 = pygame.image.load('images/numbers/free/_8.png')
free_9 = pygame.image.load('images/numbers/free/_9.png')

error_1 = pygame.image.load('images/numbers/error/e_1.png')
error_2 = pygame.image.load('images/numbers/error/e_2.png')
error_3 = pygame.image.load('images/numbers/error/e_3.png')
error_4 = pygame.image.load('images/numbers/error/e_4.png')
error_5 = pygame.image.load('images/numbers/error/e_5.png')
error_6 = pygame.image.load('images/numbers/error/e_6.png')
error_7 = pygame.image.load('images/numbers/error/e_7.png')
error_8 = pygame.image.load('images/numbers/error/e_8.png')
error_9 = pygame.image.load('images/numbers/error/e_9.png')

# UTILITY FUNCTIONS

def main_menu():
    
    # Draw main menu
    screen.fill(background_color)
    screen.blit(logo, (300, 50))
    screen.blit(menu, (415, 200))
    screen.blit(play, (150, 300))
    screen.blit(solve, (400, 300))
    screen.blit(stats, (650, 300))
    screen.blit(github, (910, 495))
    

    # Set button animation
    on_play = False
    on_solve = False
    on_stats = False
    on_github = False

    # Wait for user choice and animate buttons
    choose = False

    while not choose:

        for event in pygame.event.get():

            # Quit the game
            if event.type == pygame.QUIT:
                playing = True
                return False

            # On play
            if (pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400):
                on_play = True
                pygame.draw.rect(screen, background_color, (150, 300, 200, 100))
                screen.blit(play_over, (150, 300))
                pygame.draw.rect(screen, background_color, (300, 450, 400, 70))
                screen.blit(play_msg, (300, 450))
            else:
                on_play = False
                pygame.draw.rect(screen, background_color, (150, 300, 200, 100))
                screen.blit(play, (150, 300))
            
            # On solve
            if (pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400):
                on_solve = True
                pygame.draw.rect(screen, background_color, (400, 300, 200, 100))
                screen.blit(solve_over, (400, 300))
                pygame.draw.rect(screen, background_color, (300, 450, 400, 70))
                screen.blit(solve_msg, (300, 450))
            else:
                on_solve = False
                pygame.draw.rect(screen, background_color, (400, 300, 200, 100))
                screen.blit(solve, (400, 300))
            
            # On stats
            if (pygame.mouse.get_pos()[0] >= 650 and pygame.mouse.get_pos()[0] <= 850 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400):
                on_stats = True
                pygame.draw.rect(screen, background_color, (650, 300, 200, 100))
                screen.blit(stats_over, (650, 300))
                pygame.draw.rect(screen, background_color, (300, 450, 400, 70))
                screen.blit(stats_msg, (375, 450))
            else:
                on_stats = False
                pygame.draw.rect(screen, background_color, (650, 300, 200, 100))
                screen.blit(stats, (650, 300))

            # On github
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 985 and pygame.mouse.get_pos()[1] >= 495 and pygame.mouse.get_pos()[1] <= 570):
                on_github = True
                pygame.draw.rect(screen, background_color, (910, 495, 75, 75))
                screen.blit(github_over, (910, 495))
            else:
                on_github = False
                pygame.draw.rect(screen, background_color, (910, 495, 75, 75))
                screen.blit(github, (910, 495))
                
            # Cover button messages
            if not(on_play) and not(on_solve) and not(on_stats):
                pygame.draw.rect(screen, background_color, (300, 450, 400, 70))
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if on_play:
                    return 'Play'
                
                if on_solve:
                    return 'Solve'
                
                if on_stats:
                    return 'Stats'
                
                if on_github:

                    # Open github project repository 
                    on_github = False
                    pygame.draw.rect(screen, background_color, (910, 495, 75, 75))
                    screen.blit(github, (910, 495))           
                    webpage = webbrowser.open('https://github.com/MatteoRaffaeleDeSilvestri/PySudoku.git', new = 0, autoraise = True)
                    if webpage:
                        pygame.display.update()
        
        # Refresh the screen every 60 FPS
        pygame.time.Clock().tick(FPS)
        pygame.display.update()

def select_difficult():
    
    # Draw difficult menu
    screen.fill(background_color)
    screen.blit(logo, (300, 50))
    screen.blit(set_difficult, (300, 200))
    screen.blit(easy, (150, 300))
    screen.blit(medium, (400, 300))
    screen.blit(hard, (650, 300))
    screen.blit(back, (425, 450))
    
    # Set button animation
    on_easy = False
    on_medium = False
    on_hard = False
    on_back = False

    choose = False

    # Wait for user choice and animate buttons
    while not choose:
        
        for event in pygame.event.get():

            # Quit the game
            if event.type == pygame.QUIT:
                choose = True

            # On easy
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400:
                on_easy = True
                pygame.draw.rect(screen, background_color, (150, 300, 200, 100))
                screen.blit(easy_over, (150, 300)) 
            else:
                on_easy = False
                pygame.draw.rect(screen, background_color, (150, 300, 200, 100))
                screen.blit(easy, (150, 300))

            # On medium
            if pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400:
                on_medium = True
                pygame.draw.rect(screen, background_color, (400, 300, 200, 100))
                screen.blit(medium_over, (400, 300))
            else:
                on_medium = False
                pygame.draw.rect(screen, background_color, (400, 300, 200, 100))
                screen.blit(medium, (400, 300))

            # On hard
            if pygame.mouse.get_pos()[0] >= 650 and pygame.mouse.get_pos()[0] <= 850 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 400:
                on_hard = True
                pygame.draw.rect(screen, background_color, (650, 300, 200, 100))
                screen.blit(hard_over, (650, 300))
            else:
                on_hard = False
                pygame.draw.rect(screen, background_color, (650, 300, 200, 100))
                screen.blit(hard, (650, 300))

            # On back
            if pygame.mouse.get_pos()[0] >= 425 and pygame.mouse.get_pos()[0] <= 575 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[1] <= 500:
                on_back = True
                pygame.draw.rect(screen, background_color, (425, 450, 150, 50))
                screen.blit(back_over, (425, 450)) 
            else:
                on_back = False
                pygame.draw.rect(screen, background_color, (425, 450, 150, 50))
                screen.blit(back, (425, 450))
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if on_easy:
                    pygame.draw.rect(screen, background_color, (150, 200, 850, 400))
                    screen.blit(generate_msg, (200, 300))
                    pygame.display.update()
                    gen_time_start = time()
                    grid, solution, solve_time = sudoku.sudoku_maker('easy')
                    gen_time_end = time()
                    data.management('algo', 'e', (gen_time_end - gen_time_start) - solve_time, solve_time)
                    return ('easy', grid, solution, (gen_time_end - gen_time_start) - solve_time, solve_time)
                
                if on_medium:
                    pygame.draw.rect(screen, background_color, (150, 200, 850, 400))
                    screen.blit(generate_msg, (200, 300))
                    pygame.display.update()
                    gen_time_start = time()
                    grid, solution, solve_time = sudoku.sudoku_maker('medium')
                    gen_time_end = time()
                    data.management('algo', 'm', (gen_time_end - gen_time_start) - solve_time, solve_time)
                    return ('medium', grid, solution, (gen_time_end - gen_time_start) - solve_time, solve_time)
                
                if on_hard:
                    pygame.draw.rect(screen, background_color, (150, 200, 850, 400))
                    screen.blit(generate_msg, (200, 300))
                    pygame.display.update()
                    gen_time_start = time()
                    grid, solution, solve_time = sudoku.sudoku_maker('hard')
                    gen_time_end = time()
                    data.management('algo', 'h', (gen_time_end - gen_time_start) - solve_time, solve_time)
                    return ('hard', grid, solution, (gen_time_end - gen_time_start) - solve_time, solve_time)
                
                if on_back:
                    return True
        
        # Refresh the screen every 60 FPS
        pygame.time.Clock().tick(FPS)
        pygame.display.update()

def game_field(difficult, grid):

    # Draw game field (9 x 9 square)
    screen.fill(background_color)

    for i in range(10):
        if i % 3 == 0:
            width = 2
        else:
            width = 1
        pygame.draw.line(screen, black, (20, 20 + (60 * i)), (560, 20 + (60 * i)), width)
        pygame.draw.line(screen, black, (20 + (60 * i), 20), (20 + (60 * i), 560), width)

    # Draw difficult label
    difficult_level = field_label.render('Difficult: ' + difficult, True, black)
    screen.blit(difficult_level, (580, 20))
    screen.blit(export_btn, (860, 22))
    
    pygame.draw.line(screen, black, (580, 110), (980, 110), 2)

    # Draw options buttons
    screen.blit(hint_btn_disabled, (580, 140))
    screen.blit(quit_btn, (790, 140))
    screen.blit(clear_btn_disabled, (580, 250))
    screen.blit(solve_btn, (790, 250))
    animation_text = animation_label.render('Show animation', True, black)
    screen.blit(animation_text, (815, 347))
    screen.blit(checkbox, (790, 350))
    screen.blit(note_play, (580, 507))

    # Set static and free cells of sudoku
    for coord in grid.keys():
        if grid[coord[0], coord[1]] != 0:
            locked_cells.append((coord[0], coord[1]))
            if grid[coord[0], coord[1]] == 1: screen.blit(locked_1, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 2: screen.blit(locked_2, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 3: screen.blit(locked_3, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 4: screen.blit(locked_4, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 5: screen.blit(locked_5, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 6: screen.blit(locked_6, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 7: screen.blit(locked_7, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 8: screen.blit(locked_8, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
            elif grid[coord[0], coord[1]] == 9: screen.blit(locked_9, (22 + 58 * coord[1] + 2 * coord[1], 22 + 58 * coord[0] + 2 * coord[0]))
        else:
            free_cells.append((coord[0], coord[1]))

def lock_numbers(grid, selected_cell):

    # Convert all the given numbers from free to locked

    to_update = dict()
    
    for cell in grid.keys():
        if grid[cell] != 0:
            locked_cells.append(cell)
            if grid[cell] == 1: to_update[grid_to_pixel[cell]] = locked_1
            elif grid[cell] == 2: to_update[grid_to_pixel[cell]] = locked_2
            elif grid[cell] == 3: to_update[grid_to_pixel[cell]] = locked_3
            elif grid[cell] == 4: to_update[grid_to_pixel[cell]] = locked_4
            elif grid[cell] == 5: to_update[grid_to_pixel[cell]] = locked_5
            elif grid[cell] == 6: to_update[grid_to_pixel[cell]] = locked_6
            elif grid[cell] == 7: to_update[grid_to_pixel[cell]] = locked_7
            elif grid[cell] == 8: to_update[grid_to_pixel[cell]] = locked_8
            else: to_update[grid_to_pixel[cell]] = locked_9
        
    # Update the board (visual)
    for item in to_update.items():
        pygame.draw.rect(screen, background_color, (item[0][0], item[0][1], item[0][2], item[0][3]))    
        screen.blit(item[1], (item[0][0], item[0][1]))

    # Clear selected cell
    if selected_cell and ((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60) not in locked_cells:
        pygame.draw.rect(screen, background_color, selected_cell)
    selected_cell = False

def selection(selected_cell, cell):
    
    # Set offset based on the cell position on the grid
    top_shift, left_shift = utilities.shifter(cell)
    horizontal_offset, vertical_offset = utilities.offset(cell[0] * 60 + 20, cell[1] * 60 + 20)
    
    # Highlight selected cell (and clear the previous selected cell)
    if selected_cell:
        pygame.draw.rect(screen, background_color, selected_cell)

    pygame.draw.rect(screen, selected_cell_color, (cell[0] * 60 + 20 + horizontal_offset + top_shift, cell[1] * 60 + 20 + vertical_offset + left_shift, 58 + horizontal_offset, 58 + vertical_offset)) 
    selected_cell = (cell[0] * 60 + 20 + horizontal_offset + top_shift, cell[1] * 60 + 20 + vertical_offset + left_shift, 58 + horizontal_offset, 58 + vertical_offset)
    grid_to_pixel[(cell[1], cell[0])] = (selected_cell)

    return selected_cell

def hint(solution, selected_cell, btn):

    # Put a new locked number on the grid (give an hint)
    if btn == 'hint':

        if solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 1: number = locked_1;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 1
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 2: number = locked_2;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 2
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 3: number = locked_3;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 3
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 4: number = locked_4;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 4
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 5: number = locked_5;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 5
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 6: number = locked_6;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 6
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 7: number = locked_7;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 7
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 8: number = locked_8;  grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 8
        else: number = locked_9; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 9
    
    elif btn == 'solve':
    
        if solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 1: number = free_1; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 1
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 2: number = free_2; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 2
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 3: number = free_3; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 3
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 4: number = free_4; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 4
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 5: number = free_5; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 5
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 6: number = free_6; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 6
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 7: number = free_7; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 7
        elif solution[((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60)] == 8: number = free_8; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 8
        else: number = free_9; grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 9
    
    pygame.draw.rect(screen, background_color, selected_cell)
    screen.blit(number, (selected_cell[0], selected_cell[1]))
    free_cells.remove(((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60))
    locked_cells.append(((selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60))
    return False

def to_clear():

    # Check if there are cell to clean
    for cell in free_cells:
        if grid[cell] != 0:
            return True
    return False

def solution_check(grid, mode):
    
    # Keep the sudoku on the screen updated while checking if a valid solution is given
    if mode == 'Play':
        
        valid_solution = True
        to_update = dict()
        
        for cell in grid.keys():
            if grid[cell] != 0:
                if cell not in locked_cells and not utilities.validate(grid, grid[cell], cell[0], cell[1]):
                    valid_solution = False
                    if grid[cell] == 1: to_update[grid_to_pixel[cell]] = error_1
                    elif grid[cell] == 2: to_update[grid_to_pixel[cell]] = error_2
                    elif grid[cell] == 3: to_update[grid_to_pixel[cell]] = error_3
                    elif grid[cell] == 4: to_update[grid_to_pixel[cell]] = error_4
                    elif grid[cell] == 5: to_update[grid_to_pixel[cell]] = error_5
                    elif grid[cell] == 6: to_update[grid_to_pixel[cell]] = error_6
                    elif grid[cell] == 7: to_update[grid_to_pixel[cell]] = error_7
                    elif grid[cell] == 8: to_update[grid_to_pixel[cell]] = error_8
                    else: to_update[grid_to_pixel[cell]] = error_9
                elif cell not in locked_cells:
                    if grid[cell] == 1: to_update[grid_to_pixel[cell]] = free_1
                    elif grid[cell] == 2: to_update[grid_to_pixel[cell]] = free_2
                    elif grid[cell] == 3: to_update[grid_to_pixel[cell]] = free_3
                    elif grid[cell] == 4: to_update[grid_to_pixel[cell]] = free_4
                    elif grid[cell] == 5: to_update[grid_to_pixel[cell]] = free_5
                    elif grid[cell] == 6: to_update[grid_to_pixel[cell]] = free_6
                    elif grid[cell] == 7: to_update[grid_to_pixel[cell]] = free_7
                    elif grid[cell] == 8: to_update[grid_to_pixel[cell]] = free_8
                    else: to_update[grid_to_pixel[cell]] = free_9
            else:
                valid_solution = False
        
        # Keep the grid updated (visual feedback for each input number)
        for item in to_update.items():
            if type(selected_cell) != bool and (selected_cell[0], selected_cell[1]) == (item[0][0], item[0][1]):
                color = selected_cell_color
            else:
                color = background_color
            if item[1] == 0:
                pygame.draw.rect(screen, color, (item[0][0], item[0][1], item[0][2], item[0][3]))
            else:
                pygame.draw.rect(screen, color, (item[0][0], item[0][1], item[0][2], item[0][3]))    
                screen.blit(item[1], (item[0][0], item[0][1]))
        return valid_solution

    # Keep the sudoku on the screen updated while checking if a solvable sudoku is given
    elif mode == 'Solve':

        valid_solution = True
        to_update = dict()
        
        for cell in grid.keys():
            if grid[cell] != 0 and cell not in locked_cells:
                if not utilities.validate(grid, grid[cell], cell[0], cell[1]):
                    valid_solution = False
                    if grid[cell] == 1: to_update[grid_to_pixel[cell]] = error_1
                    elif grid[cell] == 2: to_update[grid_to_pixel[cell]] = error_2
                    elif grid[cell] == 3: to_update[grid_to_pixel[cell]] = error_3
                    elif grid[cell] == 4: to_update[grid_to_pixel[cell]] = error_4
                    elif grid[cell] == 5: to_update[grid_to_pixel[cell]] = error_5
                    elif grid[cell] == 6: to_update[grid_to_pixel[cell]] = error_6
                    elif grid[cell] == 7: to_update[grid_to_pixel[cell]] = error_7
                    elif grid[cell] == 8: to_update[grid_to_pixel[cell]] = error_8
                    else: to_update[grid_to_pixel[cell]] = error_9
                else:
                    if grid[cell] == 1: to_update[grid_to_pixel[cell]] = free_1
                    elif grid[cell] == 2: to_update[grid_to_pixel[cell]] = free_2
                    elif grid[cell] == 3: to_update[grid_to_pixel[cell]] = free_3
                    elif grid[cell] == 4: to_update[grid_to_pixel[cell]] = free_4
                    elif grid[cell] == 5: to_update[grid_to_pixel[cell]] = free_5
                    elif grid[cell] == 6: to_update[grid_to_pixel[cell]] = free_6
                    elif grid[cell] == 7: to_update[grid_to_pixel[cell]] = free_7
                    elif grid[cell] == 8: to_update[grid_to_pixel[cell]] = free_8
                    else: to_update[grid_to_pixel[cell]] = free_9
        
        # Keep the grid updated (visual feedback for each input number)
        for item in to_update.items():
            if type(selected_cell) != bool and (selected_cell[0], selected_cell[1]) == (item[0][0], item[0][1]):
                color = selected_cell_color
            else:
                color = background_color
            if item[1] == 0:
                pygame.draw.rect(screen, color, (item[0][0], item[0][1], item[0][2], item[0][3]))
            else:
                pygame.draw.rect(screen, color, (item[0][0], item[0][1], item[0][2], item[0][3]))    
                screen.blit(item[1], (item[0][0], item[0][1]))
        return valid_solution

def status_bar_animation(progress, mode):

    # Animate status bar during solving process

    if mode == 'Play':
        pygame.draw.rect(screen, background_color, (735, 412, 90, 35))
        pygame.draw.rect(screen, adv_bar_color, (585, 414, (393 * progress) // 100, 32))
        adv_label = field_label.render(str(progress) + '%', True, black)
        if progress <= 9:
            screen.blit(adv_label, (760, 411))
        elif progress <= 99:
            screen.blit(adv_label, (751, 411))
        else:
            screen.blit(adv_label, (741, 411))
    
    elif mode == 'Solve':
        pygame.draw.rect(screen, background_color, (735, 402, 90, 35))
        pygame.draw.rect(screen, adv_bar_color, (585, 404, (393 * progress) // 100, 32))
        adv_label = field_label.render(str(progress) + '%', True, black)
        if progress <= 9:
            screen.blit(adv_label, (760, 401))
        elif progress <= 99:
            screen.blit(adv_label, (751, 401))
        else:
            screen.blit(adv_label, (741, 401))

def game_field_empty():

    # Draw game field (9 x 9 square)
    screen.fill(background_color)

    for i in range(10):
        if i % 3 == 0:
            width = 2
        else:
            width = 1
        pygame.draw.line(screen, black, (20, 20 + (60 * i)), (560, 20 + (60 * i)), width)
        pygame.draw.line(screen, black, (20 + (60 * i), 20), (20 + (60 * i), 560), width)

    # Draw text and options buttons
    screen.blit(solve_text, (580, 20))
    screen.blit(note_solve, (580, 259))
    pygame.draw.line(screen, black, (580, 320), (980, 320), 2)
    screen.blit(clear_btn_disabled, (580, 340))
    screen.blit(solve_btn_disabled, (790, 340))
    animation_text = animation_label.render('Show animation', True, black)
    screen.blit(animation_text, (815, 437))
    screen.blit(checkbox, (790, 440))
    screen.blit(back, (830, 512))
    
    # Set free cells of sudoku and generate the grid
    grid = dict()
    for i in range(81):
        free_cells.append((i // 9, i % 9))
        grid[(i // 9, i % 9)] = 0
    
    return grid

def requirements():

    # Check if the requirements for a valid sudoku are meet
    if list(grid.values()).count(0) <= 64:
        return True
    else:
        return False

def stats_section():

    # Display the statistics background and buttons
    screen.blit(stats_background, (0, 0))
    screen.blit(back, (830, 512))

    # Set buttons animation
    on_clear = False
    on_back = False
    
    # Fill the stats fields
    clearable = draw_stats()

    # If there are stats to clear than show clear button
    if clearable:
        screen.blit(clear_stats, (665, 512))

    pygame.display.update()

    done = False
    
    while not done:

        for event in pygame.event.get():

            # Quit the game
            if event.type == pygame.QUIT:
                return False
             
            # Animate back button
            if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                on_back = True
                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                screen.blit(back_over, (830, 512))
                pygame.display.update()
            else:
                on_back = False
                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                screen.blit(back, (830, 512))
                pygame.display.update()

            # Animate clear button
            if clearable:
                if pygame.mouse.get_pos()[0] >= 665 and pygame.mouse.get_pos()[0] <= 815 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                    on_clear = True
                    pygame.draw.rect(screen, background_color, (665, 512, 150, 50))
                    screen.blit(clear_stats_over, (665, 512))
                    pygame.display.update()
                else:
                    on_clear = False
                    pygame.draw.rect(screen, background_color, (665, 512, 150, 50))
                    screen.blit(clear_stats, (665, 512))
                    pygame.display.update()

            # Go back to main menu
            if event.type == pygame.MOUSEBUTTONDOWN and on_clear:
                
                # Hide Tkinter window
                Tk().withdraw()

                answer = messagebox.askyesno(title = 'Clear statistics', message = 'Are you sure you want to delete the statistics?')
                if answer:

                    # Reset data (and update the screen)
                    stats = data.reset()
                    on_clear = False
                    clearable = False
                    screen.blit(stats_background, (0, 0))
                    pygame.draw.rect(screen, background_color, (665, 512, 150, 50))
                    draw_stats()
                    pygame.display.update()
            
            # Go back to main menu
            if event.type == pygame.MOUSEBUTTONDOWN and on_back:
                done = True
                
        # Refresh the screen every 60 FPS
        pygame.time.Clock().tick(FPS)
        pygame.display.update()
    
    return True

def draw_stats():
    
    # Collect data
    stats = data.read()

    # EASY
    if stats['pg']['e'] != 0:

        clearable_easy = True

        pygame.draw.rect(screen, background_color, (380, 190, 120, 315))

        # Display played game (easy)
        pge = stats_label.render(str(stats['pg']['e']), True, black)
        if stats['pg']['e'] < 10:
            screen.blit(pge, (435, 163))
        elif stats['pg']['e'] < 100:
            screen.blit(pge, (428, 163))
        elif stats['pg']['e'] < 1000:
            screen.blit(pge, (421, 163))
        else:
            pge = stats_label.render('> 999', True, black)
            screen.blit(pge, (414, 163))
        
        # Display longest game time (easy) 
        lge = stats_label.render(stats['lg']['e'], True, black)
        screen.blit(lge, (396, 190))

        # Display shortest game time (easy) 
        sge = stats_label.render(stats['sg']['e'], True, black)
        screen.blit(sge, (396, 217))

        # Display won game (easy)
        gwe = stats_label.render(str(stats['gw']['e']), True, black)
        if stats['gw']['e'] < 10:
            screen.blit(gwe, (435, 244))
        elif stats['gw']['e'] < 100:
            screen.blit(gwe, (429, 244))
        elif stats['gw']['e'] < 1000:
            screen.blit(gwe, (422, 244))
        else:
            gwe = stats_label.render('> 999', True, black)
            screen.blit(gwe, (414, 244))

        # Display winning ratio % (easy)
        wre = stats_label.render(str(int(stats['gw']['e'] / stats['pg']['e'] * 100)) + '%', True, black)
        if int(stats['gw']['e'] / stats['pg']['e'] * 100) < 10:
            screen.blit(wre, (428, 271))
        elif int(stats['gw']['e'] / stats['pg']['e'] * 100) < 100:
            screen.blit(wre, (423, 271))
        else:
            screen.blit(wre, (414, 271))

        # Display average generating time (easy)
        if int(sum(stats['agt']['e']) / len(stats['agt']['e'])) > 60:
            agte = stats_label.render('> 1 min' ,True, black)
            screen.blit(agte, (403, 338))
        else:
            if sum(stats['agt']['e']) / len(stats['agt']['e']) < 0.001:
                agte = stats_label.render('< 0.001ms', True, black)
            else:
                agte = stats_label.render(utilities.data_format(str(sum(stats['agt']['e']) / len(stats['agt']['e']))), True, black)
            screen.blit(agte, (389, 338))

        # Display best generating time (easy)
        if int(min(stats['agt']['e'])) > 60:
            bgte = stats_label.render('> 1 min', True, black)
            screen.blit(bgte, (403, 392))
        else:
            if min(stats['agt']['e']) < 0.001:
                bgte = stats_label.render('< 0.001ms', True, black)
            else:
                bgte = stats_label.render(utilities.data_format(str(min(stats['agt']['e']))), True, black)
            screen.blit(bgte, (389, 392))

        # Display worst generating time (easy)
        if int(max(stats['agt']['e'])) > 60:
            wgte = stats_label.render('> 1 min', True, black)
            screen.blit(wgte, (403, 419))
        else:
            if max(stats['agt']['e']) < 0.001:
                wgte = stats_label.render('< 0.001ms', True, black)
            else:
                wgte = stats_label.render(utilities.data_format(str(max(stats['agt']['e']))), True, black)
            screen.blit(wgte, (389, 419))
            
        # Display average solving time (easy)
        if sum(stats['ast']['e']) / len(stats['ast']['e']) > 60:
            aste = stats_label.render('> 1 min' ,True, black)
            screen.blit(aste, (403, 365))
        else:
            if sum(stats['ast']['e']) / len(stats['ast']['e']) < 0.001:
                aste = stats_label.render('< 0.001ms', True, black)
            else:
                aste = stats_label.render(utilities.data_format(str(sum(stats['ast']['e']) / len(stats['ast']['e']))), True, black)
            screen.blit(aste, (389, 365))

        # Display best solving time (easy)
        if int(min(stats['ast']['e'])) > 60:
            bste = stats_label.render('> 1 min', True, black)
            screen.blit(bste, (403, 446))
        else:
            if min(stats['ast']['e']) < 0.001:
                bste = stats_label.render('< 0.001ms', True, black)
            else:
                bste = stats_label.render(utilities.data_format(str(min(stats['ast']['e']))), True, black)
            screen.blit(bste, (389, 446))

        # Display worst solving time (easy)
        if int(max(stats['ast']['e'])) > 60:
            wste = stats_label.render('> 1 min', True, black)
            screen.blit(wste, (403, 473))
        else:
            if max(stats['ast']['e']) < 0.001:
                wste = stats_label.render('< 0.001ms', True, black)
            else:            
                wste = stats_label.render(utilities.data_format(str(max(stats['ast']['e']))), True, black)
            screen.blit(wste, (389, 473))

    else:
        pge = stats_label.render(str(stats['pg']['e']), True, black)
        screen.blit(pge, (435, 163))
        clearable_easy = False
      
    # MEDIUM
    if stats['pg']['m'] != 0:

        clearable_medium = True

        pygame.draw.rect(screen, background_color, (595, 190, 120, 315)) 

        # Display played game (medium)
        pgm = stats_label.render(str(stats['pg']['m']), True, black)
        if stats['pg']['m'] < 10:
            screen.blit(pgm, (650, 163))
        elif stats['pg']['m'] < 100:
            screen.blit(pgm, (644, 163))
        elif stats['pg']['m'] < 1000:
            screen.blit(pgm, (638, 163))
        else:
            pgm = stats_label.render('> 999', True, black)
            screen.blit(pgm, (631, 163))
    
        # Display longest game time (medium) 
        lgm = stats_label.render(stats['lg']['m'], True, black)
        screen.blit(lgm, (612, 190))

        # Display shortest game time (medium)
        sgm = stats_label.render(stats['sg']['m'], True, black)
        screen.blit(sgm, (612, 217))

        # Display won game (medium)
        gwm = stats_label.render(str(stats['gw']['m']), True, black)
        if stats['gw']['m'] < 10:
            screen.blit(gwm, (651, 244))
        elif stats['gw']['m'] < 100:
            screen.blit(gwm, (645, 244))
        elif stats['gw']['m'] < 1000:
            screen.blit(gwm, (638, 244))
        else:
            gwm = stats_label.render('> 999', True, black)
            screen.blit(gwm, (631, 244))
        
        # Display winning ratio % (medium)
        wrm = stats_label.render(str(int(stats['gw']['m'] / stats['pg']['m'] * 100)) + '%', True, black)
        if int(stats['gw']['m'] / stats['pg']['m'] * 100) < 10:
            screen.blit(wrm, (644, 271))
        elif int(stats['gw']['m'] / stats['pg']['m'] * 100) < 100:
            screen.blit(wrm, (639, 271))
        else:
            screen.blit(wrm, (630, 271))
        
        # Display average generating time (medium)
        if sum(stats['agt']['m']) / len(stats['agt']['m']) > 60:
            agtm = stats_label.render('> 1 min' ,True, black)
            screen.blit(agtm, (619, 338))
        else:
            if sum(stats['agt']['m']) / len(stats['agt']['m']) < 0.001:
                agtm = stats_label.render('< 0.001ms', True, black)
            else:
                agtm = stats_label.render(utilities.data_format(str(sum(stats['agt']['m']) / len(stats['agt']['m']))), True, black)
            screen.blit(agtm, (605, 338))

        # Display best generating time (medium)
        if int(min(stats['agt']['m'])) > 60:
            bgtm = stats_label.render('> 1 min', True, black)
            screen.blit(bgtm, (619, 392))
        else:
            if min(stats['agt']['m']) < 0.001:
                bgtm = stats_label.render('< 0.001ms', True, black)
            else:
                bgtm = stats_label.render(utilities.data_format(str(min(stats['agt']['m']))), True, black)
            screen.blit(bgtm, (605, 392))

        # Display worst generating time (medium)
        if int(max(stats['agt']['m'])) > 60:
            wgtm = stats_label.render('> 1 min', True, black)
            screen.blit(wgtm, (619, 419))
        else:
            if max(stats['agt']['m']) < 0.001:
                wgtm = stats_label.render('< 0.001ms', True, black)
            else:
                wgtm = stats_label.render(utilities.data_format(str(max(stats['agt']['m']))), True, black)
            screen.blit(wgtm, (605, 419))
        
        # Display average solving time (medium)
        if sum(stats['ast']['m']) / len(stats['ast']['m']) > 60:
            astm = stats_label.render('> 1 min' ,True, black)
            screen.blit(astm, (619, 365))
        else:
            if sum(stats['ast']['m']) / len(stats['ast']['m']) < 0.001:
                astm = stats_label.render('< 0.001ms', True, black)
            else:
                astm = stats_label.render(utilities.data_format(str(sum(stats['ast']['m']) / len(stats['ast']['m']))), True, black)
            screen.blit(astm, (605, 365))

        # Display best solving time (medium)
        if int(min(stats['ast']['m'])) > 60:
            bstm = stats_label.render('> 1 min', True, black)
            screen.blit(bstm, (619, 446))
        else:
            if min(stats['ast']['m']) < 0.001:
                bstm = stats_label.render('< 0.001ms', True, black)
            else:
                bstm = stats_label.render(utilities.data_format(str(min(stats['ast']['m']))), True, black)
            screen.blit(bstm, (605, 446))

        # Display worst solving time (medium)
        if int(max(stats['ast']['m'])) > 60:
            wstm = stats_label.render('> 1 min', True, black)
            screen.blit(wstm, (619, 473))
        else:
            if max(stats['ast']['m']) < 0.001:
                wstm = stats_label.render('< 0.001ms', True, black)
            else:
                wstm = stats_label.render(utilities.data_format(str(max(stats['ast']['m']))), True, black)
            screen.blit(wstm, (605, 473))

    else:
        pgm = stats_label.render(str(stats['pg']['m']), True, black)
        screen.blit(pgm, (650, 163))
        clearable_medium = False
      
    # HARD
    if stats['pg']['h'] != 0:

        clearable_hard = True

        pygame.draw.rect(screen, background_color, (815, 190, 120, 315)) 

        # Display played game (hard)
        pgh = stats_label.render(str(stats['pg']['h']), True, black)
        if stats['pg']['h'] < 10:
            screen.blit(pgh, (868, 163))
        elif stats['pg']['h'] < 100:
            screen.blit(pgh, (862, 163))
        elif stats['pg']['h'] < 1000:
            screen.blit(pgh, (855, 163))
        else:
            pgh = stats_label.render('> 999', True, black)
            screen.blit(pgh, (848, 163))
        
        # Display longest game time (hard)
        lgh = stats_label.render(stats['lg']['h'], True, black)
        screen.blit(lgh, (830, 190))

        # Display shortest game time (hard)
        sgh = stats_label.render(stats['sg']['h'], True, black)
        screen.blit(sgh, (830, 217))

        # Display won game (hard)
        gwh = stats_label.render(str(stats['gw']['h']), True, black)
        if stats['gw']['h'] < 10:
            screen.blit(gwh, (869, 244))
        elif stats['gw']['h'] < 100:
            screen.blit(gwh, (863, 244))
        elif stats['gw']['h'] < 1000:
            screen.blit(gwh, (856, 244))
        else:
            gwh = stats_label.render('> 999', True, black)
            screen.blit(gwh, (848, 244))

        # Display winning ratio % (hard)
        wrh = stats_label.render(str(int(stats['gw']['h'] / stats['pg']['h'] * 100)) + '%', True, black)
        if int(stats['gw']['h'] / stats['pg']['h'] * 100) < 10:
            screen.blit(wrh, (862, 271))
        elif int(stats['gw']['h'] / stats['pg']['h'] * 100) < 100:
            screen.blit(wrh, (857, 271))
        else:
            screen.blit(wrh, (848, 271))
    
        # Display average generating time (hard)
        if sum(stats['agt']['h']) / len(stats['agt']['h']) > 60:
            agth = stats_label.render('> 1 min' ,True, black)
            screen.blit(agth, (837, 338))
        else:
            if sum(stats['agt']['h']) / len(stats['agt']['h']) < 0.001:
                agth = stats_label.render('< 0.001ms', True, black)
            else:
                agth = stats_label.render(utilities.data_format(str(sum(stats['agt']['h']) / len(stats['agt']['h']))), True, black)
            screen.blit(agth, (823, 338))

        # Display best generating time (hard)
        if int(min(stats['agt']['h'])) > 60:
            bgth = stats_label.render('> 1 min', True, black)
            screen.blit(bgth, (837, 392))
        else:
            if min(stats['agt']['h']) < 0.001:
                bgth = stats_label.render('< 0.001ms', True, black)
            else:
                bgth = stats_label.render(utilities.data_format(str(min(stats['agt']['h']))), True, black)
            screen.blit(bgth, (823, 392))

        # Display worst generating time (hard)
        if int(max(stats['agt']['h'])) > 60:
            wgth = stats_label.render('+1 min', True, black)
            screen.blit(wgth, (837, 419))
        else:
            if max(stats['agt']['h']) < 0.001:
                wgth = stats_label.render('< 0.001ms', True, black)
            else:
                wgth = stats_label.render(utilities.data_format(str(max(stats['agt']['h']))), True, black)
            screen.blit(wgth, (823, 419))

        # Display average solving time (medium)
        if sum(stats['ast']['h']) / len(stats['ast']['h']) > 60:
            asth = stats_label.render('+1 min' ,True, black)
            screen.blit(asth, (837, 365))
        else:
            if sum(stats['ast']['h']) / len(stats['ast']['h']) < 0.001:
                asth = stats_label.render('< 0.001ms', True, black)
            else:
                asth = stats_label.render(utilities.data_format(str(sum(stats['ast']['h']) / len(stats['ast']['h']))), True, black)
            screen.blit(asth, (823, 365))

        # Display best solving time (hard)
        if int(min(stats['ast']['h'])) > 60:
            bsth = stats_label.render('+1 min', True, black)
            screen.blit(bsth, (837, 446))
        else:
            if min(stats['ast']['h']) < 0.001:
                bsth = stats_label.render('< 0.001ms', True, black) 
            else:
                bsth = stats_label.render(utilities.data_format(str(min(stats['ast']['h']))), True, black)
            screen.blit(bsth, (823, 446))

        # Display worst solving time (hard)
        if int(max(stats['ast']['h'])) > 60:
            wsth = stats_label.render('+1 min', True, black)
            screen.blit(wsth, (837, 473))
        else:
            if max(stats['ast']['h']) < 0.001:
                wsth = stats_label.render('< 0.001ms', True, black)
            else:
                wsth = stats_label.render(utilities.data_format(str(max(stats['ast']['h']))), True, black)
            screen.blit(wsth, (823, 473))
  
    else:
        pgh = stats_label.render(str(stats['pg']['h']), True, black)
        screen.blit(pgh, (868, 163))
        clearable_hard = False
    
    return clearable_easy or clearable_medium or clearable_hard

if __name__ == "__main__":

    # Open main menu at startup
    mode = main_menu()
    
    # MAIN LOOP
    while mode:

        # Play the game
        if mode == 'Play':

            # Choose the difficult of the board to generate
            try:
                action = select_difficult()
                
                if type(action) == bool:
                    playing = False
                    mode = action
                
                else:

                    # Generate and draw the grid
                    difficult, grid, solution, generation_time, solving_time = action[0], action[1], action[2], action[3], action[4]
                    game_field(difficult, grid)
                    playing = True

            # Avoid TypeError if user decide to exit game in the select difficult menu
            except TypeError:
                playing = False
                mode = False
                    
            # Play loop
            while playing:

                # Update game timer               
                timer += 1
                if timer % FPS == 0:
                    pygame.draw.rect(screen, background_color, (580, 64, 230, 35))
                    clock = field_label.render('Time: ' + utilities.time_format(timer // 60), True, black)
                    screen.blit(clock, (580, 62))

                for event in pygame.event.get():

                    # Quit the game
                    if event.type == pygame.QUIT:
                        playing = False
                        mode = False
                    
                    # Animate export button
                    if pygame.mouse.get_pos()[0] >= 860 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 22 and pygame.mouse.get_pos()[1] <= 92:
                        on_export = True
                        pygame.draw.rect(screen, background_color, (860, 22, 120, 70))
                        screen.blit(export_btn_over, (860, 22))
                    else:
                        on_export = False
                        pygame.draw.rect(screen, background_color, (860, 22, 120, 70))
                        screen.blit(export_btn, (860, 22))

                    # Animate hint button
                    if selected_cell:
                        if pygame.mouse.get_pos()[0] >= 580 and pygame.mouse.get_pos()[0] <= 770 and pygame.mouse.get_pos()[1] >= 140 and pygame.mouse.get_pos()[1] <= 230:
                            on_hint = True
                            pygame.draw.rect(screen, background_color, (580, 140, 190, 90))
                            screen.blit(hint_btn_over, (580, 140))
                        else:
                            on_hint = False
                            pygame.draw.rect(screen, background_color, (580, 140, 190, 90))
                            screen.blit(hint_btn, (580, 140))
                    
                    # Animate quit button
                    if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 140 and pygame.mouse.get_pos()[1] <= 230:
                        on_quit = True
                        pygame.draw.rect(screen, background_color, (790, 140, 190, 90))
                        screen.blit(quit_btn_over, (790, 140))
                    else:
                        on_quit = False
                        pygame.draw.rect(screen, background_color, (790, 140, 190, 90))
                        screen.blit(quit_btn, (790, 140))
                    
                    # Animate clear button
                    if not(to_clear()):
                        pygame.draw.rect(screen, background_color, (580, 250, 190, 90))
                        screen.blit(clear_btn_disabled, (580, 250))
                        pygame.display.update()
                    else:
                        if pygame.mouse.get_pos()[0] >= 580 and pygame.mouse.get_pos()[0] <= 770 and pygame.mouse.get_pos()[1] >= 250 and pygame.mouse.get_pos()[1] <= 340:
                            on_clear = True
                            pygame.draw.rect(screen, background_color, (580, 250, 190, 90))
                            screen.blit(clear_btn_over, (580, 250))
                        else:
                            on_clear = False
                            pygame.draw.rect(screen, background_color, (580, 250, 190, 90))
                            screen.blit(clear_btn, (580, 250))
                        pygame.display.update()

                    # Animate solve button
                    if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 250 and pygame.mouse.get_pos()[1] <= 340:
                        on_solve = True
                        pygame.draw.rect(screen, background_color, (790, 250, 190, 90))
                        screen.blit(solve_btn_over, (790, 250))
                    else:
                        on_solve = False
                        pygame.draw.rect(screen, background_color, (790, 250, 190, 90))
                        screen.blit(solve_btn, (790, 250))
                    
                    # Animate checkbox
                    if checkbox_count % 2 == 0:
                        if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] >= 350 and pygame.mouse.get_pos()[1] <= 370:
                            on_check = True
                            pygame.draw.rect(screen, background_color, (790, 350, 20, 20))
                            screen.blit(checkbox_over, (790, 350))
                        else:
                            on_check = False
                            pygame.draw.rect(screen, background_color, (790, 350, 20, 20))
                            screen.blit(checkbox, (790, 350))
                    else:
                        if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] >= 350 and pygame.mouse.get_pos()[1] <= 370:
                            on_check = True
                            pygame.draw.rect(screen, background_color, (790, 350, 20, 20))
                            screen.blit(checkbox_checked_over, (790, 350))
                        else:
                            on_check = False
                            pygame.draw.rect(screen, background_color, (790, 350, 20, 20))
                            screen.blit(checkbox_checked, (790, 350))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        # Generate and export pdf
                        if on_export:
                            screen.blit(exporting_btn_over, (860, 22))
                            pygame.display.update()
                            pdf_gen.export(grid, locked_cells)
                            screen.blit(export_btn, (860, 22))
                            pygame.display.update()
                            
                        # Get an hint
                        if on_hint:
                            selected_cell = hint(solution, selected_cell, 'hint')
                            pygame.draw.rect(screen, background_color, (580, 140, 190, 90))
                            screen.blit(hint_btn_disabled, (580, 140))
                            on_hint = False
                            hinted = True

                            # Update difficult label
                            pygame.draw.rect(screen, background_color, (580, 20, 250, 40))
                            difficult_level = field_label.render('Difficult: - ', True, black)
                            screen.blit(difficult_level, (580, 20)) 
                        
                        # Go back to main menu
                        if on_quit:
                            playing = False
                            mode = True

                        # Clear the grid
                        if on_clear:
                            for cell in free_cells:
                                grid[cell[0], cell[1]] = 0
                                selected_cell = selection(selected_cell, (cell[1], cell[0]))
                                pygame.draw.rect(screen, background_color, selected_cell)
                            selected_cell = False
                                
                        # Solve sudoku
                        if on_solve:

                            on_check = False     
                            stopped = False
                            
                            # Disable buttons
                            screen.blit(export_btn_disabled, (860, 22))
                            screen.blit(hint_btn_disabled, (580, 140))
                            screen.blit(quit_btn_disabled, (790, 140))
                            screen.blit(clear_btn_disabled, (580, 250))
                            pygame.draw.rect(screen, background_color, (790, 250, 190, 90))
                            screen.blit(solve_btn_disabled, (790, 250))
                            pygame.draw.rect(screen, background_color, (580, 507, 397, 50))
                            
                            # Clear the grid
                            for cell in free_cells:
                                selected_cell = selection(selected_cell, (cell[1], cell[0]))
                                grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 0
                            
                            pygame.draw.rect(screen, background_color, selected_cell)
                            selected_cell = False
                            
                            # Display solving message
                            screen.blit(solving_msg, (580, 390, 400, 100))
                            pygame.display.update()
                        
                            # Fill empty cells
                            if checkbox_count % 2 == 0:
                                
                                # Apply (and compensate) the delay
                                if start_end_delay - solving_time > 0:
                                    sleep(start_end_delay - solving_time)

                                for cell in free_cells[:]:
                                    selected_cell = selection(selected_cell, (cell[1], cell[0]))
                                    selected_cell = hint(solution, selected_cell, 'solve')
                                
                            else:

                                # Generate the solution (and compensate delay)
                                start_gen = time()
                                solution_animation = sudoku.animate_sol(grid)
                                end_gen = time()
                                
                                # Apply (and compensate) the delay
                                if start_end_delay - (end_gen - start_gen) > 0:
                                    sleep(start_end_delay - (end_gen - start_gen))
                                
                                # Wait for user input to stop the animation
                                pygame.draw.rect(screen, background_color, (580, 390, 400, 100))
                                
                                quitted = False
                                
                                # Initialise status bar and timer 
                                adv = 0
                                pygame.draw.rect(screen, black, (580, 410, 400, 40), 2)
                                iteractions = len(solution_animation)
                                tmr = (len(solution_animation) - adv) // 10 
                                time_label = status_bar_label.render('Time remaining: ' + utilities.time_format(tmr), True, black)
                                screen.blit(time_label, (580, 452))
                                
                                for command in solution_animation:

                                    adv += 1
                                    actual_timer = (len(solution_animation) - adv) // 10

                                    # Update the status bar
                                    actual_adv = int(adv / len(solution_animation) * 100)
                                    status_bar_animation(actual_adv, mode)

                                    # Update timer        
                                    if actual_timer != tmr:
                                        pygame.draw.rect(screen, background_color, (580, 452, 401, 20))
                                        tmr = actual_timer
                                        time_label = status_bar_label.render('Time remaining: ' + utilities.time_format(tmr), True, black)
                                        screen.blit(time_label, (580, 452))
                                        
                                    for event in pygame.event.get():
                                        
                                        # Quit the game
                                        if event.type == pygame.QUIT:
                                            quitted = True 
                                            mode = False
                                           
                                        # Animate stop button
                                        if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                            on_stop = True
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(stop_over, (830, 512))
                                            pygame.display.update()
                                        else:
                                            on_stop = False
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(stop, (830, 512))
                                            pygame.display.update()
                                        
                                        # Stop the animation
                                        if event.type == pygame.MOUSEBUTTONDOWN and on_stop:
                                            solution_animation.clear()
                                            stopped = True
                                    
                                    # Animate
                                    if not quitted and not stopped:       
                                        selected_cell = selection(selected_cell, (int(command[1]), int(command[0])))
                                        grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = int(command[2])
                                        solution_check(grid, mode)
                                        sleep(animation_delay)
                                        pygame.display.update()
                                    else:
                                        break
                            
                            if mode:
                                
                                # Reset selected cell and stop button
                                pygame.draw.rect(screen, background_color, (580, 400, 401, 100))
                                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                screen.blit(back, (830, 512))
                                selected_cell = False
                                solution_check(grid, mode)

                                if checkbox_count % 2 == 0 or not stopped:
                                    sleep(start_end_delay)
                                    
                                # Display solve stats
                                if not stopped:
                                    if checkbox_count % 2 == 0:
                                        gen_label = ingame_stats_label.render('Generation time: ' + utilities.gen_solve_time_format(generation_time), True, black)
                                        solve_label = ingame_stats_label.render('Solving time: ' + utilities.gen_solve_time_format(solving_time), True, black)
                                        screen.blit(gen_label, (580, 405))
                                        screen.blit(solve_label, (580, 435))
                                    else:
                                        gen_label = ingame_stats_label.render('Generation time: ' + utilities.gen_solve_time_format(generation_time), True, black)
                                        solve_label = ingame_stats_label.render('Solving time: ' + utilities.gen_solve_time_format(solving_time), True, black)
                                        iteraction_label = ingame_stats_label.render('Iteractions: ' + str(adv), True, black)
                                        screen.blit(gen_label, (580, 398))
                                        screen.blit(solve_label, (580, 428))
                                        screen.blit(iteraction_label, (580, 458))
                                
                                pygame.display.update()
                                
                                # Wait for user input to get back to main menu
                                done = False

                                while not done:

                                    for event in pygame.event.get():

                                        # Quit the game
                                        if event.type == pygame.QUIT:
                                            done = True
                                            mode = False

                                        # Animate back button
                                        if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                            on_back = True
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(back_over, (830, 512))
                                            pygame.display.update()
                                        else:
                                            on_back = False
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(back, (830, 512))
                                            pygame.display.update()

                                        # Go back to main menu
                                        if event.type == pygame.MOUSEBUTTONDOWN and on_back:
                                            done = True

                            solved = True
                            playing = False

                        # Animate checkbox
                        if on_check:
                            checkbox_count += 1
                            pygame.draw.rect(screen, background_color, (790, 350, 20, 20))
                            if checkbox_count % 2 != 0:
                                screen.blit(checkbox_checked, (790, 350))
                            else:
                                screen.blit(checkbox, (790, 350))
                        
                        # Select cell on the grid
                        if pygame.mouse.get_pos()[0] >= 22 and pygame.mouse.get_pos()[0] <= 558 and pygame.mouse.get_pos()[1] >= 22 and pygame.mouse.get_pos()[1] <= 558 and ((pygame.mouse.get_pos()[1] - 20) // 60, (pygame.mouse.get_pos()[0] - 20) // 60) not in locked_cells:
                            selected_cell = selection(selected_cell,((pygame.mouse.get_pos()[0] - 20) // 60, (pygame.mouse.get_pos()[1] - 20) // 60))
                            screen.blit(hint_btn, (580, 140))
                        else:
                            if selected_cell:
                                pygame.draw.rect(screen, background_color, selected_cell)
                                selected_cell = False
                                screen.blit(hint_btn_disabled, (580, 140))
 
                    # Manage the number in input
                    if event.type == pygame.KEYDOWN and selected_cell:
                            
                        # Add number to selected cell and update the grid to keep track of board change 
                        if pygame.key.name(event.key) in ['1', '[1]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 1
                        elif pygame.key.name(event.key) in ['2', '[2]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 2
                        elif pygame.key.name(event.key) in ['3', '[3]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 3
                        elif pygame.key.name(event.key) in ['4', '[4]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 4
                        elif pygame.key.name(event.key) in ['5', '[5]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 5
                        elif pygame.key.name(event.key) in ['6', '[6]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 6
                        elif pygame.key.name(event.key) in ['7', '[7]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 7
                        elif pygame.key.name(event.key) in ['8', '[8]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 8
                        elif pygame.key.name(event.key) in ['9', '[9]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 9
                            
                        # Clear selected cell
                        elif pygame.key.name(event.key) in ['backspace', 'delete']:
                            grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 0
                            pygame.draw.rect(screen, selected_cell_color, selected_cell)
                        
                # Keep the sudoku updated (give visual feedback for every input on the board) and check if a solution is foud
                if solution_check(grid, mode) and not solved:
                    
                    # Disable buttons
                    screen.blit(export_btn_disabled, (860, 22))
                    screen.blit(hint_btn_disabled, (580, 140))
                    screen.blit(quit_btn_disabled, (790, 140))
                    screen.blit(clear_btn_disabled, (580, 250))
                    pygame.draw.rect(screen, background_color, (790, 250, 190, 90))
                    screen.blit(solve_btn_disabled, (790, 250))
                    
                    # Load data if the player win without help (hint or solve)
                    if not hinted:
                        data.management('player', difficult[0], str(utilities.time_format(timer // 60)), None)
                        
                    # Display message 'You win!'
                    pygame.draw.circle(screen, winning_mark_color[0], (int((22 / 2) + (560 / 2)), int((22 / 2) + (560 / 2))), int(230% (560 / 2)))
                    win = victory_label.render('You win!', True, winning_mark_color[1])
                    screen.blit(win, (160, 250))
                    pygame.draw.rect(screen, background_color, (580, 507, 397, 56))
                    screen.blit(back, (830, 512))

                    # Wait for user input to go back to menu
                    go_back = False

                    while not(go_back):

                        for event in pygame.event.get():

                            # Quit the game
                            if event.type == pygame.QUIT:
                                go_back = True
                                mode = False

                            # Animate back button
                            if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                on_back = True
                                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                screen.blit(back_over, (830, 512))
                                pygame.display.update()
                            else:
                                on_back = False
                                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                screen.blit(back, (830, 512))
                                pygame.display.update()

                            # Go back to main menu
                            if event.type == pygame.MOUSEBUTTONDOWN and on_back:
                                go_back = True

                    playing = False

                # Refresh the screen every 60 FPS
                pygame.time.Clock().tick(FPS)
                pygame.display.update()
        
            # Reset game variables
            locked_cells = list()
            free_cells = list()
            grid_to_pixel = dict()
            selected_cell = False
            on_hint = False
            on_quit = False
            on_clear = False
            on_solve = False
            on_check = False
            on_back = False
            timer = -1
            hinted = False
            solved = False
            checkbox_count = 0

            # Go back to main menu (if player don't want to quit the game)
            if mode:
                mode = main_menu()
            
        # Validate and solve a given sudoku
        elif mode == 'Solve':
                        
            # Draw the empty board 
            grid = game_field_empty()
            solved = False
            
            # Solve loop
            while not solved:
                
                for event in pygame.event.get():
                        
                    # Quit the game
                    if event.type == pygame.QUIT:
                        solved = True
                        mode = False

                    # Animate clear button
                    if not(to_clear()):
                        pygame.draw.rect(screen, background_color, (580, 340, 190, 90))
                        screen.blit(clear_btn_disabled, (580, 340))
                        pygame.display.update()
                    else:
                        if pygame.mouse.get_pos()[0] >= 580 and pygame.mouse.get_pos()[0] <= 770 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[1] <= 430:
                            on_clear = True
                            pygame.draw.rect(screen, background_color, (580, 340, 190, 90))
                            screen.blit(clear_btn_over, (580, 340))
                        else:
                            on_clear = False
                            pygame.draw.rect(screen, background_color, (580, 340, 190, 90))
                            screen.blit(clear_btn, (580, 340))
                        pygame.display.update()

                    # Animate solve button
                    if requirements() and solution_check(grid, mode):
                        if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[1] <= 430:
                            on_solve = True
                            pygame.draw.rect(screen, background_color, (790, 340, 190, 90))
                            screen.blit(solve_btn_over, (790, 340))
                        else:
                            on_solve = False
                            pygame.draw.rect(screen, background_color, (790, 340, 190, 90))
                            screen.blit(solve_btn, (790, 340))
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen, background_color, (790, 340, 190, 90))
                        screen.blit(solve_btn_disabled, (790, 340))
                        pygame.display.update()

                    # Animate checkbox
                    if checkbox_count % 2 == 0:
                        if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[1] <= 460:
                            on_check = True
                            pygame.draw.rect(screen, background_color, (790, 440, 20, 20))
                            screen.blit(checkbox_over, (790, 440))
                        else:
                            on_check = False
                            pygame.draw.rect(screen, background_color, (790, 440, 20, 20))
                            screen.blit(checkbox, (790, 440))
                    else:
                        if pygame.mouse.get_pos()[0] >= 790 and pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[1] <= 460:
                            on_check = True
                            pygame.draw.rect(screen, background_color, (790, 440, 20, 20))
                            screen.blit(checkbox_checked_over, (790, 440))
                        else:
                            on_check = False
                            pygame.draw.rect(screen, background_color, (790, 440, 20, 20))
                            screen.blit(checkbox_checked, (790, 440))

                    # Animate back button
                    if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                        on_back = True
                        pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                        screen.blit(back_over, (830, 512))
                    else:
                        on_back = False
                        pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                        screen.blit(back, (830, 512))

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # Clear the grid
                        if on_clear:
                            for cell in free_cells:
                                grid[cell[0], cell[1]] = 0
                                selected_cell = selection(selected_cell, (cell[1], cell[0]))
                                pygame.draw.rect(screen, background_color, selected_cell)
    
                        # Solve sudoku
                        if on_solve:

                            on_check = False
                            stopped = False

                            # Convert all the given number as fixed cell (locked numbers)
                            lock_numbers(grid, selected_cell)
                            selected_cell = False
                            
                            # Check if the sudoku is already solved
                            if list(grid.values()).count(0) == 0:
                                
                                # Convert all the given number as fixed cell (locked numbers)
                                pygame.draw.rect(screen, background_color, (580, 340, 400, 200))
                                screen.blit(solved_msg, (580, 385, 400, 100))
                                
                                # Wait for user input to go back to menu
                                go_back = False

                                while not(go_back):

                                    for event in pygame.event.get():

                                        # Quit the game
                                        if event.type == pygame.QUIT:
                                            go_back = True
                                            mode = False

                                        # Animate back button
                                        if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                            on_back = True
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(back_over, (830, 512))
                                            pygame.display.update()
                                        else:
                                            on_back = False
                                            pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                            screen.blit(back, (830, 512))
                                            pygame.display.update()
                                    
                                        # Go back to main menu
                                        if event.type == pygame.MOUSEBUTTONDOWN and on_back:
                                            go_back = True
                            
                            else:

                                no_solution = False
                                multi_solution = False

                                # Display the solving message
                                pygame.draw.rect(screen, background_color, (580, 340, 400, 225))
                                screen.blit(solving_msg, (580, 385))  
                                pygame.display.update()

                                # Fill empty cells
                                if checkbox_count % 2 == 0:

                                    # Generate the solution (and compensate delay)
                                    start_gen = time()
                                    solution, solving_time, error_code = sudoku.static_solution(grid)
                                    end_gen = time()
                                    
                                    # Apply (and compensate) the delay
                                    if start_end_delay - (end_gen - start_gen) > 0:
                                        sleep(start_end_delay - (end_gen - start_gen))

                                    # Check if a solution is available 
                                    if error_code:
                                        for cell in list(set((i // 9, i % 9) for i in range(81)) - set(locked_cells)):
                                            selected_cell = selection(selected_cell, (cell[1], cell[0]))
                                            selected_cell = hint(solution, selected_cell, 'solve')
                                    else:

                                        # Identify the error occurred
                                        if error_code == 0:
                                            no_solution = True
                                        else:
                                            multi_solution = True

                                else:

                                    # Calculate solving time and generate the actual solution separately
                                    start_gen = time()
                                    solution, solving_time, error_code = sudoku.static_solution(grid)
                                    end_gen = time()

                                    # Apply (and compensate) the delay
                                    if start_end_delay - (end_gen - start_gen) > 0:
                                        sleep(start_end_delay - (end_gen - start_gen))
            
                                    # Check if a solution is available 
                                    if error_code:

                                        # Display the animation message
                                        pygame.draw.rect(screen, background_color, (580, 340, 400, 225))
                                        screen.blit(animation_msg, (580, 385))  
                                        pygame.display.update()

                                        # Generate the solution (and compensate delay)
                                        solution_animation = sudoku.animate_sol(grid)
                                        
                                        # Wait for user input to stop the animation
                                        pygame.draw.rect(screen, background_color, (580, 390, 400, 100))
                                        
                                        quitted = False
                                        
                                        # Initialise status bar and timer 
                                        adv = 0
                                        pygame.draw.rect(screen, black, (580, 400, 400, 40), 2)
                                        iteractions = len(solution_animation)
                                        tmr = (len(solution_animation) - adv) // 10 
                                        time_label = status_bar_label.render('Time remaining: ' + utilities.time_format(tmr), True, black)
                                        screen.blit(time_label, (580, 442))

                                        for command in solution_animation:

                                            adv += 1
                                            actual_timer = (len(solution_animation) - adv) // 10

                                            # Update the status bar
                                            actual_adv = int(adv / len(solution_animation) * 100)
                                            status_bar_animation(actual_adv, mode)

                                            # Update timer        
                                            if actual_timer != tmr:
                                                pygame.draw.rect(screen, background_color, (580, 442, 401, 20))
                                                tmr = actual_timer
                                                time_label = status_bar_label.render('Time remaining: ' + utilities.time_format(tmr), True, black)
                                                screen.blit(time_label, (580, 442))
                                                
                                            for event in pygame.event.get():
                                                
                                                # Quit the game
                                                if event.type == pygame.QUIT:
                                                    quitted = True 
                                                    mode = False
                                                
                                                # Animate stop button
                                                if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                                    on_stop = True
                                                    pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                                    screen.blit(stop_over, (830, 512))
                                                    pygame.display.update()
                                                else:
                                                    on_stop = False
                                                    pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                                    screen.blit(stop, (830, 512))
                                                    pygame.display.update()
                                                
                                                # Stop the animation
                                                if event.type == pygame.MOUSEBUTTONDOWN and on_stop:
                                                    solution_animation.clear()
                                                    stopped = True
                                            
                                            # Animate
                                            if not quitted and not stopped:       
                                                selected_cell = selection(selected_cell, (int(command[1]), int(command[0])))
                                                grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = int(command[2])
                                                solution_check(grid, mode)
                                                sleep(animation_delay)
                                                pygame.display.update()
                                            else:
                                                break
                                    
                                    else:

                                        # Identify the error occurred
                                        if error_code == 0:
                                            no_solution = True
                                        else:
                                            multi_solution = True

                                if mode:

                                    # Reset selected cell and stop button
                                    pygame.draw.rect(screen, background_color, (580, 400, 401, 100))
                                    pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                    screen.blit(back, (830, 512))
                                    selected_cell = False
                                    solution_check(grid, mode)
                                    
                                    # Dispaly 'no solution' or 'multiple solutions' message
                                    if no_solution:
                                        screen.blit(no_solution_msg, (580, 385))
                                    elif multi_solution:
                                        screen.blit(multiple_solution_msg, (580, 385))
                                    else:

                                        # Display solve stats
                                        if not stopped:
                                            if checkbox_count % 2 == 0:
                                                solve_label = ingame_stats_label.render('Solving time: ' + utilities.gen_solve_time_format(solving_time), True, black)
                                                screen.blit(solve_label, (580, 327))
                                            else:
                                                solve_label = ingame_stats_label.render('Solving time: ' + utilities.gen_solve_time_format(solving_time), True, black)
                                                iteraction_label = ingame_stats_label.render('Iteractions: ' + str(adv), True, black)
                                                screen.blit(solve_label, (580, 327))
                                                screen.blit(iteraction_label, (580, 357))

                                    pygame.display.update()

                                    if checkbox_count % 2 == 0 or not stopped:
                                        sleep(start_end_delay)

                                    # Wait for user input to get back to main menu
                                    done = False

                                    while not done:

                                        for event in pygame.event.get():

                                            # Quit the game
                                            if event.type == pygame.QUIT:
                                                done = True
                                                mode = False

                                            # Animate back button
                                            if pygame.mouse.get_pos()[0] >= 830 and pygame.mouse.get_pos()[0] <= 980 and pygame.mouse.get_pos()[1] >= 512 and pygame.mouse.get_pos()[1] <= 562:
                                                on_back = True
                                                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                                screen.blit(back_over, (830, 512))
                                                pygame.display.update()
                                            else:
                                                on_back = False
                                                pygame.draw.rect(screen, background_color, (830, 512, 150, 50))
                                                screen.blit(back, (830, 512))
                                                pygame.display.update()

                                            # Go back to main menu
                                            if event.type == pygame.MOUSEBUTTONDOWN and on_back:
                                                done = True

                            solved = True

                        # Animate checkbox
                        if on_check:
                            checkbox_count += 1
                            pygame.draw.rect(screen, background_color, (790, 440, 20, 20))
                            if checkbox_count % 2 != 0:
                                screen.blit(checkbox_checked, (790, 440))
                            else:
                                screen.blit(checkbox, (790, 440))
                        
                        # Go back to main menu
                        if on_back:
                            solved = True
                            
                        # Select cell on the grid
                        if pygame.mouse.get_pos()[0] >= 22 and pygame.mouse.get_pos()[0] <= 558 and pygame.mouse.get_pos()[1] >= 22 and pygame.mouse.get_pos()[1] <= 558 and ((pygame.mouse.get_pos()[1] - 20) // 60, (pygame.mouse.get_pos()[0] - 20) // 60) not in locked_cells:
                            selected_cell = selection(selected_cell,((pygame.mouse.get_pos()[0] - 20) // 60, (pygame.mouse.get_pos()[1] - 20) // 60))
                        else:
                            if selected_cell:
                                pygame.draw.rect(screen, background_color, selected_cell)
                                selected_cell = False
                        
                    # Manage the number in input
                    if event.type == pygame.KEYDOWN and selected_cell:
                        
                        # Add number to selected cell and update the grid to keep track of board change 
                        if pygame.key.name(event.key) in ['1', '[1]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 1
                        elif pygame.key.name(event.key) in ['2', '[2]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 2
                        elif pygame.key.name(event.key) in ['3', '[3]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 3
                        elif pygame.key.name(event.key) in ['4', '[4]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 4
                        elif pygame.key.name(event.key) in ['5', '[5]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 5
                        elif pygame.key.name(event.key) in ['6', '[6]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 6
                        elif pygame.key.name(event.key) in ['7', '[7]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 7
                        elif pygame.key.name(event.key) in ['8', '[8]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 8
                        elif pygame.key.name(event.key) in ['9', '[9]']: grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 9
                            
                        # Clear selected cell
                        elif pygame.key.name(event.key) in ['backspace', 'delete']:
                            grid[(selected_cell[1] - 20) // 60, (selected_cell[0] - 20) // 60] = 0
                            pygame.draw.rect(screen, selected_cell_color, selected_cell)
                
                # Keep the sudoku updated (give visual feedback for every input on the board)
                solution_check(grid, mode)

                # Refresh the screen every 60 FPS
                pygame.time.Clock().tick(FPS)
                pygame.display.update()
        
            # Reset game variables
            locked_cells = list()
            free_cells = list()
            grid_to_pixel = dict()
            selected_cell = False
            on_clear = False
            on_solve = False
            on_check = False
            on_back = False
            checkbox_count = 0
            
            # Go back to main menu (if player don't want to quit the game)
            if mode:
                mode = main_menu()

        # See game stats
        elif mode == 'Stats':
            mode = stats_section()
            if mode:
                mode = main_menu()
    
        # Go back to main menu 
        elif mode:
            mode = main_menu()       
