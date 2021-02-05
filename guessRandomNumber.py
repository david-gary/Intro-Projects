# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:02:01 2021

@author: dgary
"""

import random

def guess(x):
    randNum = random.randint(1, x)
    guess = 0
    while guess != randNum:
        guess = int(input(f"Guess a number between 1 and {x}:\n"))
        if guess < randNum:
            print('Nope, too low. Try again.')
        elif guess > randNum:
            print('Sorry, guess again. Too high, bruh')
    print("Finally, you got it. Did it take you ore than 3 guess?")

guess(50)