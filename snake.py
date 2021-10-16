"""
TODO:
    Appending is done at O(1) time but there is a problem.
    A lot of functions care about the tail and in order to access it parse the entire list at O(n).
    Make a tail pointer at the linked list in order to have direct access to the last element.

    Add a class list in order to get around calling values() so much so that we save up on the O(n) operations.
    
    Add sound effects on eating food and background music.

    Add a menu with a difficulty option and set the game's speed (easy, medium, hard) at the beggining

    Add walls on harder levels.
"""

import curses,random


class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    
    #values = []

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
            
     #   if len(LinkedList.values) > 0:
     #       LinkedList.values.pop()
     #   if new_node.next != None:
     #       LinkedList.values.append(new_node.next.data)
        
        """ROBUST CODE 3000"""
        #except AttributeError as e:
        #    pass
        #except IndexError as e2:
        #    pass

    # Function to delete a node given it's position
    def deleteNode(self, position):
 
        if self.head == None:
            return

        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            self.tail = self.head
            return
        
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None or temp.next is None:
            return       
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    def find_length(self):
        
        if self.head == None:
            return 0

        length = 0
        temp = self.head
        while temp.next:
            length +=1
            temp = temp.next
        return length

    def peek_at_tail(self):
        if self.head == None:
            return 0

        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    """LinkedList.values took its place but leaving it here for future purposes"""
    def values(self):
        temp = self.head.next
        vals = []
        while(temp):
            vals.append(temp.data)
            temp = temp.next
        return vals

class Game():

    def __init__(self,rows: int,cols: int):
        
        self.snake = LinkedList()
        
        self.snake.push((4,8))
        self.snake.push((4,9))
        self.snake.push((4,10))
        self.food = (10,20)
        
        self.rows = rows
        self.cols = cols
        
        self.graphics_setup()
        self.game_loop()

    def graphics_setup(self):
        curses.initscr()
        self.win = curses.newwin(self.rows,self.cols,0,0) # y, x
        self.win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.win.border(0)
        self.win.nodelay(1)

    def game_loop(self):
        
        ESC = 27
        key = curses.KEY_RIGHT
        score = 0

        while True:
            if key == ESC:
                break
            
            self.win.addstr(0,2,"Score " + str(score) + " ")
            self.win.timeout(150 - self.snake.find_length() // 5 + self.snake.find_length()//10 % 120) #increase speed based on snake length
            
            prev_key = key
            event = self.win.getch()
            key = event if event != -1 else prev_key

            #Check for arrow keys
            if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC] or (prev_key == curses.KEY_LEFT and key == curses.KEY_RIGHT) or (prev_key == curses.KEY_RIGHT and key == curses.KEY_LEFT) or (prev_key == curses.KEY_UP and key == curses.KEY_DOWN) or (prev_key == curses.KEY_DOWN and key == curses.KEY_UP):
                key = prev_key
            
            #Calculate the next coordinates
            y,x = self.snake.head.data[0], self.snake.head.data[1]
            if key == curses.KEY_DOWN:
                y += 1
            if key == curses.KEY_LEFT:
                x -= 1
            if key == curses.KEY_RIGHT:
                x += 1
            if key == curses.KEY_UP:
                y -= 1

            #Check if we hit the border and wrap around
            if x < 0:
                x = self.cols-1
            elif x >= self.cols-1:
                x = 0
            elif y >= self.rows-1:
                y = 0
            elif y < 0:
                y = self.rows-1
            
            self.snake.push((y,x))
            self.win.border(0)

            if self.snake.head.data in self.snake.values():
                break
            if self.snake.head.data == self.food:
                score += 1
                self.food = ()
                while self.food == ():
                    self.food = (random.randint(1,self.rows-1),random.randint(1,self.cols-1))
                    if self.food in self.snake.values():
                        self.food = ()
            else:
                last = self.snake.peek_at_tail()
                self.win.addch(last.data[0],last.data[1],' ')
                self.snake.deleteNode(self.snake.find_length())

            self.win.addch(y,x, '*')
            self.win.addch(self.food[0], self.food[1], '#')
        
        curses.endwin()
        print(f"Final score = {score}")

def main():
    game = Game(20,60)

if __name__ == "__main__":
    main()

