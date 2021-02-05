# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 07:57:16 2021

@author: dgary
"""
import random
def play():
    winStatus = ''
    win = 'You won!'
    while winStatus != win:
        user = input("Rock [r], Paper [p], or Scissors [s]?\n").lower()
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            winStatus = 'Tie. try again.'
            return winStatus
        elif user == ('r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            winStatus = win
            return winStatus
        else:
            winStatus = 'You lost!'
            return winStatus
        return winStatus

print(play())