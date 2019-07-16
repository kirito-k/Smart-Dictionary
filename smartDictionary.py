"""
    File name: smartDictionary.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: A program which determines the definitions of english words using API calls and
                 guides users if miss spelled.
"""

# difflib determines the similarity between words. It also retrieves most similar words from list
import difflib
# Type check in python
from typing import List

# nltk is used for downloading english words
import nltk
# requests used for GET requests to the API
import requests
# nested_lookup determines whether a key exists in a nested dictionary
from nested_lookup import nested_lookup

# Downloading the words
nltk.download('words')
from nltk.corpus import words


def word_meaning(word: str) -> List:
    """
    Determine meaning of the word
    :param word: word to be searched
    :return: definition of word in list form if word exists else -1
    """
    try:
        # GET request to the dictionary API end point
        r = requests.get(f'https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}&lang=en')
        # Converting the response into json object
        jsonobj = r.json()
        # Retrieve the definition key's values
        return nested_lookup('definition', jsonobj)
    except:
        # Word not found
        return []


def smart_dictionary():
    """
    Implementation of smart dictionary
    :return:
    """
    while True:
        user_word = input("Enter the word: ")
        definition = word_meaning(user_word.lower())

        if len(definition) != 0:
            # If word definition found
            print("This word means:")
            for elem in definition:
                print(elem)

            last = input("Do you want to continue? y / n")
            if last == 'y':
                break
        else:
            # Find similar words from the list of english dictionary words if any
            similar_words = difflib.get_close_matches(user_word, words.words(), n=3)

            if len(similar_words) > 0:
                # If words found
                print("Word not found!! \nDid you mean any of these?", end=': ')
                for elem in similar_words:
                    print(elem, end=' ')
                print()
            else:
                # If no words found
                print("Seems like this word does not exits :(")


def main():
    smart_dictionary()


if __name__ == '__main__':
    main()
