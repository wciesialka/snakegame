#!/usr/bin/env python3

from SnakeGame import Game, Point
from time import sleep
from os import system
from random import choice
import termios, fcntl, sys, os
from typing import List
import threading
from enum import Enum

FRAMERATE:int = 5 # Frames per second

class ConsoleFormat(Enum):
    '''Console text formatting commands.'''

    RESET = '\033[1;0m'
    FG_BLACK = '\033[1;30m' 
    FG_RED = '\033[1;31m'
    FG_GREEN = '\033[1;32m'
    FG_YELLOW = '\033[1;33m'
    FG_BLUE = '\033[1;34m'
    FG_MAGENTA = '\033[1;35m'
    FG_CYAN = '\033[1;36m'
    FG_WHITE = '\033[1;37m'

    BG_BLACK = '\033[1;40m' 
    BG_RED = '\033[1;41m'
    BG_GREEN = '\033[1;42m'
    BG_YELLOW = '\033[1;43m'
    BG_BLUE = '\033[1;44m'
    BG_MAGENTA = '\033[1;45m'
    BG_CYAN = '\033[1;46m'
    BG_WHITE = '\033[1;47m'

    def __str__(self):
        return self.value

class RunningFlag:

    '''Basic boolean wrapper class for determining if game is running.'''

    def __init__(self):
        self.__value:bool = True

    @property
    def value(self) -> bool:
        return self.__value

    def __bool__(self):
        return self.__value

    def false(self):
        '''Set flag to false.'''
        self.__value = False

    def true(self):
        '''Set flag to true.'''
        self.__value = True

    

def print_game_screen(game:Game.SnakeGame):
    '''Prints the game screen.

    :param game: Game object to print.
    :type game: SnakeGame
    '''
    block = f'{ConsoleFormat.FG_BLACK}\u2588'
    
    for y in range(-1,game.size[1]+2):

        for x in range(-1,game.size[0]+2):
            print(ConsoleFormat.BG_WHITE,end='')

            if x == -1 or x == game.size[0] + 1 or y == -1 or y == game.size[1]+1:
                print(block,end='')
            else:
                pt = Point.Point(x,y)

                tile = game.tile_type(pt)

                if tile is Game.TileType.EMPTY:
                    print(' ',end='')
                elif tile is Game.TileType.APPLE:
                    print(f'{ConsoleFormat.FG_RED}@',end='')
                elif tile is Game.TileType.HEAD:
                    print(f'{ConsoleFormat.FG_GREEN}O',end='')
                else:
                    print(f'{ConsoleFormat.FG_GREEN}*',end='')
                print(ConsoleFormat.RESET,end='')
        print(ConsoleFormat.RESET)

def movement_queue_handler(sentry:RunningFlag, queue:List[str] = []):
    '''Function for handling the movement queue without blocking.

    :param sentry: If this flag is false, stop running the thread on the next iteration.
    :type sentry: RunningFlag
    :param queue: Movement queue to append to.
    :type queue: list[str]
    '''

    valid_keys = ('w','a','s','d')

    while sentry:
        try:
            c = sys.stdin.read(1)
            if c:
                if c.lower() in valid_keys:
                    queue.append(c.lower())

        except IOError: pass

def main():
    '''Handle terminal settings game_running allow for control of the game, then start the game.
    After game is done, reset the terminal.'''


    # Set terminal settings
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)

    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    game_running = RunningFlag()
    
    # Start the key collecting thread.
    keys = []
    t = threading.Thread(name="key-collection",target=movement_queue_handler,args=[game_running,keys])
    t.start()

    # Start the game. This will block main() until the game is done.
    try:
        start(keys)
    finally:
        # End and join the thread.
        game_running.false()
        t.join()

        # Reset the terminal
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def start(key_queue:List[str]):
    '''Start the game.
    
    :param key_queue: Queue of keys that the user inputs.
    :type key_queue: list[str]'''

    pt = Point.Point(1.5,2.3)
    game = Game.SnakeGame((20,10),3)
    while True:
        system("clear")
        print_game_screen(game)

        if len(key_queue) > 0:
            c = key_queue.pop(0)
            if c == 'w':
                game.face_north()
            elif c == 'a':
                game.face_west()
            elif c == 's':
                game.face_south()
            elif c == 'd':
                game.face_east()
        try:
            game.update()
        except:
            break
        

        sleep(1 / FRAMERATE)
    system("clear")
    print(f"Game Over! Your score: {game.score}")
    


if __name__ == "__main__":
    main()