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
- Copy words from /usr/share/dict/words (need to remove proper names, non-english chars, and apostrophes as script doesn't check against these)
- Check if words in dict contain at least one of the provided letters (or easier to check for any other letters)
- Use a set to store unique words
- Reduce based on center/key letter and length
'''

import re

def word_finder(uniq, letters, words):
    uniq = uniq.lower()
    letters = letters.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    anagrams = set()

    not_letters = re.sub(f'[{uniq}{letters}]', '', alphabet)

    with open(words,'r') as wordlist:
        for word in wordlist:
            word = word.strip("\n")
            if uniq in word and len(word) >= 4:
                if not re.search(rf"[{not_letters}]+", word):
                    anagrams.add(word)

    print(f"Number of words found: {len(anagrams)}")
    return sorted(anagrams)

if __name__ == "__main__":
    uniq = input("Enter the center/required letter (1): ")
    letters = input("Enter the remaining letters as a string (6): ")
    words = "words.txt"
    print(word_finder(uniq,letters,words))
    exit(0)
