# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from asyncio.base_futures import _FINISHED
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR

def wordle():
    word = random.choice(FIVE_LETTER_WORDS)

    def enter_action(s):
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Please enter a valid English word.")
        else:
            s = s.lower()
            curRow = gw.get_current_row()
            fin = True
            for i in range(0, len(word)):
                if s[i] == word[i]:
                    gw.set_square_color(curRow, i, CORRECT_COLOR)
                    gw.set_key_color(s[i].upper(), CORRECT_COLOR)
                elif s[i] in word:
                    fin = False
                    gw.set_square_color(curRow, i, PRESENT_COLOR)
                    gw.set_key_color(s[i].upper(), PRESENT_COLOR)
                else:
                    fin = False
            
            if fin:
                gw.show_message("You guessed correctly")
            else:
                gw.set_current_row(curRow + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup code

if __name__ == "__main__":
    wordle()
