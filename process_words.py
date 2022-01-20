"""Processes all 5 letter words to get a better idea of a starting word for
wordle"""
import numpy as np
import string
from collections import namedtuple
from itertools import combinations, combinations_with_replacement

Word = namedtuple("Word", "word green yellow weighted")

# alphabet = list(string.ascii_lowercase)
# letters_in_word = 5
# unique_letters = 4
# real_word_list = ["hello", "world"]
#
# letter_pools = list(combinations(alphabet, unique_letters))
# for letter_pool in letter_pools:
#     possible_words = list(combinations_with_replacement(letter_pool,
#                                                         letters_in_word))
#     for possible_word in possible_words:
#         possible_word_str = "".join(possible_word)
#         if possible_word_str in real_word_list:
#             print(possible_word_str)


class WordleSolver:

    def __init__(self):
        # Set up word list and letter frequency table
        self.alphabet = list(string.ascii_lowercase)
        # Load word list
        with open('5_letter_words.txt') as f:
            self.lines = f.read().splitlines()

        # Populate letter frequency table
        self.letter_frequency_table = np.zeros((26, 5))
        for line in self.lines:
            for i in range(5):
                letter = ord(line[i]) - 97
                position = i
                self.letter_frequency_table[letter, position] += 1

        self.word_list = [Word(word,
                               self.word_score_green([word]),
                               self.word_score_yellow([word]),
                               self.word_score_weighted([word]))
                          for word in self.lines]

        max_index = [0, 0, 0]
        max_scores = [0, 0, 0]
        for i in range(len(self.word_list)):
            word = self.word_list[i]
            if word.green > max_scores[0]:
                max_scores[0] = word.green
                max_index[0] = i
            if word.yellow > max_scores[1]:
                max_scores[1] = word.yellow
                max_index[1] = i
            if word.weighted >= max_scores[2]:
                max_scores[2] = word.weighted
                max_index[2] = i
        print("Max green word:", self.word_list[max_index[0]].word, self.word_list[max_index[0]].green)
        print("Max yellow word:", self.word_list[max_index[1]].word, self.word_list[max_index[1]].yellow)
        print("Max weighted word:", self.word_list[max_index[2]].word, self.word_list[max_index[2]].weighted)

        # for word in self.word_list:
        #     print(word.word, word.score)
        # letter_frequency = np.sum(self.letter_frequency_table, 1)

        # max_word_appreances = np.max(letter_frequency)
        # most_used_letter_overall = alphabet[int(np.argmax(letter_frequency))]
        #
        # max_letter_in_a_single_position = np.max(letter_frequency_table)
        # print(max_letter_in_a_single_position)
        # most_letter_in_a_single_position = np.argmax(letter_frequency_table)
        # print(np.floor(most_letter_in_a_single_position/5))
        # q = most_letter_in_a_single_position // 5
        # r = most_letter_in_a_single_position % 5
        # print(q, r, alphabet[q])
        #
        # word_scores = np.zeros(len(lines))
        # for i in range(len(lines)):
        #     word = lines[i][0:5]
        #     for j in range(5):
        #         letter = ord(word[j]) - 97
        #         position = j
        #         word_scores[i] += letter_frequency_table[letter, position]
        #     # print(word, word_scores[i])
        #
        # max_word_score = np.max(word_scores)
        # max_word = lines[int(np.argmax(word_scores))][0:5]
        # print(max_word, max_word_score)
        # # for a, b in zip(np.sum(letter_frequency_table, 1), ):
        # #     print(a, b)
        #
        #

    def word_score_green(self, words):
        score = 0
        letters_used = np.zeros((26, 5))
        for word in words:
            for i in range(5):
                letter = ord(word[i]) - 97
                position = i
                green_points = self.letter_frequency_table[letter, position]
                if letters_used[letter, position] == 0:
                    score += green_points
                    letters_used[letter, position] = 1
        return score

    def word_score_yellow(self, words):
        score = 0
        letter_pool = []
        for word in words:
            for i in range(5):
                letter = ord(word[i]) - 97
                yellow_points = self.letter_frequency_table.sum(1)[letter]
                if letter not in letter_pool:
                    score += yellow_points
                    letter_pool.append(letter)
        return score

    def word_score_weighted(self, words):
        score = 0
        letter_pool = []
        letters_used = np.zeros((26, 5))
        for word in words:
            for i in range(5):
                letter = ord(word[i]) - 97
                position = i
                if letter not in letter_pool:
                    yellow_points = self.letter_frequency_table.sum(1)[
                                        letter] * 2
                    score += yellow_points
                    letter_pool.append(letter)
                if letters_used[letter, position] == 0:
                    green_points = self.letter_frequency_table[letter, position] * 3
                    score += green_points
                    letters_used[letter, position] = 1
        return score

    def highest_score(self, unique_letters):
        # total_score = 0

        # a = self.highest_score_helper()
        pass

    def highest_score_helper(self):
        pass

    def highest_score_2(self, unique_words):
        max_total_score = [0] * 3
        max_indexes = [None] * 3
        max_words = [None] * 3
        # a = self.highest_score_helper()
        for index_tuple in combinations(range(len(self.word_list)), unique_words):
            words = []
            for i in index_tuple:
                words.append(self.lines[i])
            total_green_score = self.word_score_green(words)
            if total_green_score > max_total_score[0]:
                max_total_score[0] = total_green_score
                max_indexes[0] = index_tuple
                max_words[0] = words
            total_yellow_score = self.word_score_yellow(words)
            if total_yellow_score > max_total_score[1]:
                max_total_score[1] = total_yellow_score
                max_indexes[1] = index_tuple
                max_words[1] = words
            total_weighted_score = self.word_score_weighted(words)
            if total_weighted_score > max_total_score[2]:
                max_total_score[2] = total_weighted_score
                max_indexes[2] = index_tuple
                max_words[2] = words
        print(max_total_score)
        print(max_indexes)
        print(max_words)

    def highest_score_2_helper(self):
        pass


def main():
    a = WordleSolver()
    score_1 = a.word_score_green(["cores"])
    # print(score_1)
    score_2 = a.word_score_yellow(["cores"])
    # print(score_2)
    # print((3*score_1+2*score_2))
    score_3 = a.word_score_weighted(["cores"])
    # print(score_3)
    a.highest_score_2(1)
    # a.highest_score(1)


if __name__ == "__main__":
    main()
