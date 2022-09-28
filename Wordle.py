# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    def enter_action(s):

        gw.show_message(s)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    word = random.choice(FIVE_LETTER_WORDS)
    for i in range(0,len(word)):
        gw.set_square_letter(0, i, word[i])


# Startup code

if __name__ == "__main__":
    wordle()
