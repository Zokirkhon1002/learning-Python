# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 23:06:19 2021

@author: Zokirkhon
Theme: finding a word.
"""

from uzwords import words;
import random



def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()





def display(user_letters,word):
    display_letter = ''
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter;


def start():
    word = get_word();
    # letters of word and do not repeat each letter
    word_letters = set(word);
    # letter from user input
    user_letters = ''
    print(f"I thought {len(word)} digits, Can you find it?")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"The letters you have entered so far: {user_letters}")
        
        letter_from_input = input("Add a letter: ").upper()
        if letter_from_input in user_letters:
            print("You have already entered this letter. Please enter another letter")
            continue
        elif letter_from_input in word:
            word_letters.remove(letter_from_input)
            print(f"The letter {letter_from_input} is correct")
        else:
            print("We don’t have such kind of letter.")
        user_letters += letter_from_input
    print(f"\nCongratulation! You have found the {word} word. In {len(user_letters)} attempts.")

