import curses, time
from snake import Game

class Menu():
    """
    DOCSTRING!:
    A menu to control difficulty via levels and snake speed.
    Added option to turn on/off music and SFX.l
    """
    main_menu = ["Play","Difficulty","Music","Exit"]
    difficulty_menu = ["Medium","Hard","Walls","Back"]
    music_menu = ["Music", "SFX","Back"]
 
    def __init__(self):
        self.current_row = 0 
        self.menu = []

    def _print_menu(self, stdscr):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        for i,row in enumerate(self.menu):
            x = width // 2 - len(row) // 2
            y = height // 2 - len(self.menu) // 2 + i

            if i == self.current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y,x,row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y,x,row)

        stdscr.refresh()

    def minimain(self,stdscr):
        pass


class MainMenu(Menu):
    
    def __init__(self):
        super().__init__()
        self.menu = Menu.main_menu

    def minimain(self,stdscr):
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
       
        self._print_menu(stdscr)

        while True:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.menu) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                #Functions for changing the menu here:
                if self.current_row == len(self.menu) - 1:
                    break
                elif self.current_row == 0:
                    game = Game(20,60) 
                elif self.current_row == 1:
                    diff = DifficultyMenu()
                elif self.current_row == 2:
                    music = MusicMenu()

            self._print_menu(stdscr)
 

class MusicMenu(Menu):

    def __init__(self):
        super().__init__()
        self.menu = Menu.music_menu

    def minimain(self,stdscr):
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
       
        self._print_menu(stdscr)

        while True:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.menu) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                #Functions for changing the menu here:
                if self.current_row == len(self.menu) - 1:
                    back = MainMenu(self.main_menu)
                elif self.current_row == 0:
                    #Music on/off
                    pass 
                elif self.current_row == 1:
                    #SFX on/off
                    pass
            self._print_menu(stdscr)
            stdscr.refresh()


class DifficultyMenu(Menu):

    def __init__(self):
        super().__init__()
        self.menu = Menu.difficulty_menu

    def minimain(self,stdscr):
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
       
        self._print_menu(stdscr)

        while True:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.menu) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                #Functions for changing the menu here:
                if self.current_row == len(self.menu) - 1:
                    back = MainMenu(self.main_menu)
                elif self.current_row == 0:
                    #medium difficulty
                    pass 
                elif self.current_row == 1:
                    #hard difficulty
                    pass
                elif self.current_row == 2:
                    #walls on/off
                    pass

            self._print_menu(stdscr)
            stdscr.refresh()


def main(stdscr):
    m = MainMenu()
    m.minimain(stdscr)

curses.wrapper(main)
