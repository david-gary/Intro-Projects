# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:26:40 2021

@author: dgary
"""

import random

def guess(x):
    randNum = random.randint(1, x)
    guess = 0
    while guess != randNum:
        guess = int(input(f"Guess a number between 1 and {x}: \n\ "))
        if guess < randNum:
            print('Nope, too low. Try again.')
        elif guess > randNum:
            print('Sorry, guess again. Too high, bruh')
    print("Finally, you got it. Did it take you ore than 3 guess?")

def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} \ntoo high [H]    too low [L]\nor correct [C]\n".lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed it! {guess}")
    
comp_guess(50)