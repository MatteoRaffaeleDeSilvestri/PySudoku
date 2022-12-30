from tkinter import Tk, filedialog
from os.path import join, expanduser
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import ttfonts, pdfmetrics

# VARIABLES

grid_to_pdf = {(0, 0): (60,  571),
               (0, 1): (115, 571),
               (0, 2): (170, 571),
               (0, 3): (226, 571),
               (0, 4): (281, 571),
               (0, 5): (336, 571),
               (0, 6): (392, 571),
               (0, 7): (448, 571),
               (0, 8): (503, 571),
               (1, 0): (60,  516),
               (1, 1): (115, 516),
               (1, 2): (170, 516),
               (1, 3): (226, 516),
               (1, 4): (281, 516),
               (1, 5): (336, 516),
               (1, 6): (392, 516),
               (1, 7): (448, 516),
               (1, 8): (503, 516),
               (2, 0): (60,  461),
               (2, 1): (115, 461),
               (2, 2): (170, 461),
               (2, 3): (226, 461),
               (2, 4): (281, 461),
               (2, 5): (336, 461),
               (2, 6): (392, 461),
               (2, 7): (448, 461),
               (2, 8): (503, 461),
               (3, 0): (60,  405),
               (3, 1): (115, 405),
               (3, 2): (170, 405),
               (3, 3): (226, 405),
               (3, 4): (281, 405),
               (3, 5): (336, 405),
               (3, 6): (392, 405),
               (3, 7): (448, 405),
               (3, 8): (503, 405),
               (4, 0): (60,  350),
               (4, 1): (115, 350),
               (4, 2): (170, 350),
               (4, 3): (226, 350),
               (4, 4): (281, 350),
               (4, 5): (336, 350),
               (4, 6): (392, 350),
               (4, 7): (448, 350),
               (4, 8): (503, 350),
               (5, 0): (60,  295),
               (5, 1): (115, 295),
               (5, 2): (170, 295),
               (5, 3): (226, 295),
               (5, 4): (281, 295),
               (5, 5): (336, 295),
               (5, 6): (392, 295),
               (5, 7): (448, 295),
               (5, 8): (503, 295),
               (6, 0): (60,  239),
               (6, 1): (115, 239),
               (6, 2): (170, 239),
               (6, 3): (226, 239),
               (6, 4): (281, 239),
               (6, 5): (336, 239),
               (6, 6): (392, 239),
               (6, 7): (448, 239),
               (6, 8): (503, 239),
               (7, 0): (60,  184),
               (7, 1): (115, 184),
               (7, 2): (170, 184),
               (7, 3): (226, 184),
               (7, 4): (281, 184),
               (7, 5): (336, 184),
               (7, 6): (392, 184),
               (7, 7): (448, 184),
               (7, 8): (503, 184),
               (8, 0): (60,  128),
               (8, 1): (115, 128),
               (8, 2): (170, 128),
               (8, 3): (226, 128),
               (8, 4): (281, 128),
               (8, 5): (336, 128),
               (8, 6): (392, 128),
               (8, 7): (448, 128),
               (8, 8): (503, 128)}

# CONVERT THE SUDOKU IN GAME INTO A PDF FILE

def export(grid, locked_cells):
    
    # Locate the Desktop as initial save path
    pdf_default_title = 'PySudoku.pdf'
    initial_save_path = join(expanduser('~'), 'Desktop/')
    
    try:
    
        # Hide Tkinter window
        Tk().withdraw()

        # Open dialog window from Tkinter
        pdf = filedialog.asksaveasfile(initialdir = initial_save_path, initialfile = pdf_default_title,  title = 'Export as pdf', defaultextension = '.pdf', filetypes = [('PDF file', '.pdf')])
        
        # Generate pdf
        sudoku_file = Canvas(pdf.name, pagesize = A4)
        
        # Draw logo and board
        sudoku_file.drawInlineImage('images/pdf/pdf_logo.png', 25, 715)
        sudoku_file.drawInlineImage('images/pdf/pdf_board.png', 48, 120)

        # Set custom font
        pdfmetrics.registerFont(ttfonts.TTFont('Ubuntu-Regular', 'fonts/Ubuntu-Regular.ttf'))
        sudoku_file.setFont('Ubuntu-Regular', 58)

        # Draw numbers on the board
        for cell in locked_cells:
            if cell in grid_to_pdf.keys():
                sudoku_file.drawString(grid_to_pdf[cell][0], grid_to_pdf[cell][1], str(grid[cell]))

        sudoku_file.setTitle(pdf.name[len(initial_save_path):])
        sudoku_file.save()

    except AttributeError:
        pass
