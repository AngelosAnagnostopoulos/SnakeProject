#The menu redrawing implementation with states is hideous but at least it works

import curses,os,time,pygame.mixer
import audio
from snake import Game
from abc import ABC, abstractmethod

class Menu(ABC):
    """
    A menu to control difficulty via levels and snake speed.
    Added option to turn on/off music and SFX.l
    """
    main_menu = ["Play","Walls off","Audio","Exit"]
    music_menu = ["Music off", "SFX on","Back"]
 
    def __init__(self):
        self.current_row = 0 
        self.menu = []
        pygame.mixer.init()

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

    @abstractmethod
    def minimain(self,stdscr):
        pass


class MainMenu(Menu):
    
    def __init__(self):
        super().__init__()
        self.menu = Menu.main_menu
        self.walls_state = "off"

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
                elif self.current_row == 1 and self.walls_state == "off":
                #Implement walls logic in game
                    self.walls_state = "on"
                    Menu.main_menu[1] = "Walls On"
                elif self.current_row == 1 and self.walls_state == "on":
                    self.walls_state = "off"
                    Menu.main_menu[1] = "Walls Off"
                elif self.current_row == 2:
                    audio = AudioMenu()
                    audio.minimain(stdscr)     
            
            self._print_menu(stdscr)
 
class AudioMenu(Menu):

    def __init__(self):
        super().__init__()
        self.menu = Menu.music_menu
        self.music_state = "off"
        self.sfx_state = "on"
        self.window = curses.newwin(10,10,10,50)

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
                elif self.current_row == 0 and self.music_state == "off":
                    self.music_state = "on"
                    Menu.music_menu[0] = "Music On"
                    pygame.mixer.music.play(-1)

                elif self.current_row == 0 and self.music_state == "on":
                    self.music_state = "off"
                    Menu.music_menu[0] = "Music Off"
                    pygame.mixer.music.stop()
                
                elif self.current_row == 1 and self.sfx_state == "off":
                    self.sfx_state = "on"
                    Menu.music_menu[1] = "SFX On"
                    audio.food_sound_ptr = audio.food_sound
                    audio.defeat_sound_ptr = audio.defeat_sound

                elif self.current_row == 1 and self.sfx_state == "on":
                    self.sfx_state = "off"
                    Menu.music_menu[1] = "SFX Off"
                    audio.food_sound_ptr = None 
                    audio.defeat_sound_ptr = None 

            self._print_menu(stdscr)



def main(stdscr):
    m = MainMenu()
    m.minimain(stdscr)

curses.wrapper(main)
