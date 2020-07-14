
import sys 

from collections import Counter

path = sys.argv[1]

def count_dict_word(filename):

    textfile = open(filename)
    words_2 = []

    for line in textfile:

        words = line.strip().split(" ")

        for word in words:

            if word == "":

                continue

            for char in word:

                if not char.isalpha():

                    word = word.replace(char, "")

            words_2.append(word.lower())

    word_count = Counter(words_2)
    
    print(word_count)

    # word_count = {}

    #     for word in words:
    #         word_count[word] = word_count.get(word, 0) + 1

    # print(word_count)