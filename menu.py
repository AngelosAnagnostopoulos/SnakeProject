import curses
import time 

class Menu():
    """
    DOCSTRING!:
    A menu to control difficulty via levels and snake speed.
    Added option to turn on/off music and SFX.l
    """
    def __init__(self):
        pass


menu = ["Play","Difficulty","Music","Exit"]

def print_menu(stdscr, current_row):

    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    for i,row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + i

        if i == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)

    stdscr.refresh()

def main(stdscr):

    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
   
    current_row = 0

    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()
        
        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            #Functions for changing the menu here:
            stdscr.clear()
            stdscr.addstr(0,0,"Test string")
            stdscr.refresh()
            if current_row == len(menu) - 1:
                break

        print_menu(stdscr,current_row)
               
        stdscr.refresh()

curses.wrapper(main)


