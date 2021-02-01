#!/bin/env python3

"""
This code is puzzle 15 of Game!
I wrote this code (EmadDeve20 in Github)
email address: emaddeve20@gmail.com
this is source have GPL LICENSE
if you see a bug plz report it to me or pl I so happy about this :D
or you have an idea plz send PL
"""


import os
import platform
import time
import random
from key_manager import controler
from pnum import prmat
import push_numbers as p

class Game:
    """This is class For PlayGround and Handle for win time"""
    def __init__(self):
        self.mat = [[], [], [], []]

        #numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        numbers = []
        for i in range(16):
            numbers.append(i+1)

        for i in range(len(self.mat)):
            for _j in range(len(self.mat)):
                choice = random.choice(numbers)
                self.mat[i].append(choice)
                numbers.remove(choice)

        self.time_start = time.time()
        #self.time_now = int(time.time()-self.time_start())

    def game_manager(self):
        """this function sees the playground. The game is finished or Not!"""
        while p.matrix_is_alive(self.mat):
            self.draw()
            controler(self.mat)
        self.draw()

    def draw(self):
        """this is function can draw a playground for player :D"""
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == 'Windows':
            os.system('cls')
        prmat(self.mat)


if __name__ == "__main__":
    GAME = Game()
    GAME.game_manager()
