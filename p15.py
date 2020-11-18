#!/bin/env python3


from key_manager import controler
from pnum import prmat
import push_numbers as p
import random , os , platform , time

class Game:
    """This is class For PlayGround"""
    def __init__(self):
        self.mat = [[],[],[],[]]
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                choice = random.choice(numbers)
                self.mat[i].append(choice)
                numbers.remove(choice)

        self.time_start = time.time()
        #self.time_now = int(time.time()-self.time_start())

    def game_manager(self):
        while p.matrix_is_alive(self.mat):
            self.draw()
            controler(self.mat)
        self.draw()

    def draw(self):
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == 'Windows':
            os.system('cls')
        prmat(self.mat)

    def not_finished(self):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if self.mat[i][j] > self.mat[i][j+1]:
                    return True
        return False

if __name__ == "__main__":
    game = Game()
    game.game_manager()
