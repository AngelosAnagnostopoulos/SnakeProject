"""
TODO:
    Add walls on harder levels.
"""

import curses,random,pygame,os,time
from ds import Node, LinkedList

class Game():

    def __init__(self,rows: int,cols: int):
        
        self.snake = LinkedList()
        
        self.snake.push((4,8))
        self.snake.push((4,9))
        self.snake.push((4,10))
        self.food = (10,20)
        
        self.rows = rows
        self.cols = cols
        
        self.pygame_setup()
        self.graphics_setup()
        self.game_loop()
  
    def pygame_setup(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        s = "sound"
        self.food_sound = pygame.mixer.Sound(os.path.join('sounds/food.ogg'))
        self.defeat_sound = pygame.mixer.Sound(os.path.join('sounds/defeat.ogg'))

    def graphics_setup(self):
        curses.initscr()
        self.win = curses.newwin(self.rows,self.cols,0,0) # y, x
        self.win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.win.border(0)
        self.win.nodelay(1)

    def at_border(self,x,y):
        #Check if we hit the border and wrap around
        temp_x = x
        temp_y = y

        if temp_x <= 0:
            x = self.cols-2
        elif temp_x >= self.cols-1:
            x = 0
        elif temp_y >= self.rows-1:
            y = 0
        elif temp_y <= 0:
            y = self.rows-2
        self.snake.push((y,x))
        self.win.border(0)

    def game_loop(self):
        
        ESC = 27
        key = curses.KEY_RIGHT
        score = 0

        while True:
            if key == ESC:
                break
            
            self.win.addstr(0,2,"Score " + str(score) + " ")
            self.win.timeout(150 - self.snake.length // 5 + self.snake.length//10 % 120) #increase speed based on snake length
            
            prev_key = key
            event = self.win.getch()
            key = event if event != -1 else prev_key
            
            if key not in (curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC) or (prev_key == curses.KEY_LEFT and key == curses.KEY_RIGHT) or (prev_key == curses.KEY_RIGHT and key == curses.KEY_LEFT) or (prev_key == curses.KEY_UP and key == curses.KEY_DOWN) or (prev_key == curses.KEY_DOWN and key == curses.KEY_UP):
                key = prev_key

            #Calculate the next coordinates
            y,x = self.snake.head.data[0], self.snake.head.data[1]
            if key == curses.KEY_DOWN:
                y += 1
            elif key == curses.KEY_LEFT:
                x -= 1
            elif key == curses.KEY_RIGHT:
                x += 1
            elif key == curses.KEY_UP:
                y -= 1

            self.at_border(x,y)   

            if self.snake.head.data in self.snake.values():
                pygame.mixer.Sound.play(self.defeat_sound)
                time.sleep(1)
                break
            if self.snake.head.data == self.food:
                score += 1
                pygame.mixer.Sound.play(self.food_sound)
                self.food = ()
                while self.food == ():
                    self.food = (random.randint(2,self.rows-2),random.randint(2,self.cols-2))
                    if self.food in self.snake.values():
                        self.food = ()
            else:
                last = self.snake.peek_at_tail()
                self.win.addch(last.data[0],last.data[1],' ')
                self.snake.delete_tail()

            self.win.addch(y,x, '*')
            self.win.addch(self.food[0], self.food[1], '#')
        
        curses.endwin()

def main():
    game = Game(20,60)

if __name__ == "__main__":
    main()

