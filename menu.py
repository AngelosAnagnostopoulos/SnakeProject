import curses, time
from snake import Game


class Menu():

    def __init__(self,stdscr,menu):
        
        stdscr.clear()
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
        current_row = 0
   
    def menu_functionality(self,stdscr):
        pass

    def _print_menu(self,stdscr, current_row, menu):

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


class Main_Menu(Menu):
    
    def __init__(self,stdscr,menu):
        super().__init__(stdscr,menu)
        self.menu = menu
        self.menu_functionality(stdscr)
    
    def menu_functionality(self, stdscr):
      
        current_row = 0
        self._print_menu(stdscr,self.menu,current_row)
      
        while True:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
            
                stdscr.clear()
                stdscr.refresh()
                
                if current_row == len(menu) - 1:
                    break
                elif current_row == 0:
                    game = Game(20,60) 
                """
                elif current_row == 1:
                    difficulty_menu()
                elif current_row == 2:
                    music_menu()
                """
            
            self._print_menu(stdscr, self.menu, current_row)       
            stdscr.refresh()
    

main_menu = ["Play","Difficulty","Music","Exit"]
difficulty_menu = ["Easy", "Medium", "Hard", "Custom"]
custom_difficulty = ["Speed +","Speed -","Walls"]
music_menu = ["Music"]

def main(stdscr):
    m = Main_Menu(stdscr,main_menu)

curses.wrapper(main)


