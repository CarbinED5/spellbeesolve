#!/usr/bin/python3

'''
This program was inspired to solve (for fun) the Spelling Bee mini game found on the NYT crossword app.

Objective: Create as many words as possible from the provided letters

Rules:
- 7 unique letters are provided
- Words must utilize the center/key letter
- Words must be 4 letters long at a minimum
- Letters can be used more than once
- No proper nouns

Notes:
- Use words from /usr/share/dict/words (removed proper names, non-english chars, and apostrophes)
'''

import re

def word_finder(uniq, letters, words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    anagrams = set()

    not_letters = re.sub(f'[{uniq.lower()}{letters.lower()}]', '', alphabet)

    with open(words,'r') as word_list:
        for word in word_list:
            word = word.strip("\n")
            if uniq in word and len(word) >= 4:
                if not re.search(rf"[{not_letters}]+", word):
                    anagrams.add(word)

    return sorted(anagrams)

if __name__ == "__main__":
    uniq = input("Enter the center/required letter (1): ")
    letters = input("Enter the remaining letters as a string (6): ")
    words = "words.txt"
    anagrams = word_finder(uniq,letters,words)

    print(f"Number of words found: {len(anagrams)}")
    print("Anagrams: ", anagrams)
