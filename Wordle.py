# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from asyncio.base_futures import _FINISHED
import random
from tkinter import W

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from tkinter import messagebox

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

            for i in range(0, len(word)):
                if s[i] in word and s[i] != word[i]: 
                    fin = False
                    if s.count(s[i]) > word.count(s[i]):
                        indices = [j for j, ch in enumerate(s) if ch == s[i]]
                        changeCol = True
                        for j in range(len(indices)):
                            if gw.get_square_color(curRow, indices[j]) == CORRECT_COLOR:
                                changeCol = False
                        if changeCol:
                            for j in range(len(indices)):
                                if j == 0:
                                    if gw.get_key_color(s[indices[j]].upper()) == CORRECT_COLOR:
                                        gw.set_square_color(curRow, indices[j], PRESENT_COLOR)
                                    else:
                                        gw.set_square_color(curRow, indices[j], PRESENT_COLOR)
                                        gw.set_key_color(s[indices[j]].upper(), PRESENT_COLOR)
                                else:
                                    gw.set_square_color(curRow, indices[j], MISSING_COLOR)
                        else:
                            gw.set_square_color(curRow, indices[j], MISSING_COLOR)
                        

                    elif gw.get_key_color(s[i].upper()) == CORRECT_COLOR:
                        gw.set_square_color(curRow, i, PRESENT_COLOR)
                    else:
                        gw.set_square_color(curRow, i, PRESENT_COLOR)
                        gw.set_key_color(s[i].upper(), PRESENT_COLOR)
            
            for i in range(0, len(word)):
                if s[i] not in word:
                    fin = False
                    gw.set_square_color(curRow, i, MISSING_COLOR)
                    gw.set_key_color(s[i].upper(), MISSING_COLOR)
            if curRow == 5:
                finish(s.lower())
                gw.show_message("The correct word is " + word.upper())
                return
            if fin:
                gw.show_message("You guessed correctly" + word.upper())
                finish(s.lower())
            else:
                gw.set_current_row(curRow + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    def finish(s):
        if s == word:
            messagebox.showinfo('information', 'Congratulations, you guessed the word correctly!')
        else:
            messagebox.showinfo('information', 'Sorry, you did not guess the word. The word is ' + word.upper())

# Startup code

if __name__ == "__main__":
    wordle()
