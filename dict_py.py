import csv
import random

class VocabularyBook:
    def __init__(self):
        self.vocab = {}
        self.incorrect_vocab = {}
        self.load_vocab()


    def load_vocab(self):
        try:
            with open('./words.csv', mode='r', newline='', encoding='cp949') as file:
                reader = csv.reader(file)
                self.vocab = {rows[0]:[rows[1], int(rows[2])] for rows in reader if rows[0] != "words"}

            with open('./incorrect_words.csv', mode='r', newline='', encoding='cp949') as file:
                reader = csv.reader(file)
                self.incorrect_vocab = {rows[0]:[rows[1], int(rows[2]), int(rows[3])] for rows in reader if rows[0] != "words"}
                print(self.vocab)
                print(self.incorrect_vocab)
                print("=== Data Upload Success ====")

        except FileNotFoundError:
            with open('./words.csv', mode='r', newline='', encoding='cp949') as file:
                pass


    def save_vocab(self):
        with open('./words.csv', mode='w', newline='', encoding='cp949') as file:
            writer = csv.writer(file)
            writer.writerow(['words', 'meaning', 'fail_cnt'])
            for key, value in self.vocab.items():
                writer.writerow([key, value[0], value[1]])

        with open('./incorrect_words.csv', mode='w', newline='', encoding='cp949') as file:
            writer = csv.writer(file)
            writer.writerow(['words', 'meaning', 'fail_cnt', 'ans_cnt'])
            for key, value in self.incorrect_vocab.items():
                writer.writerow([key, value[0], value[1], value[2]])

    def add_word(self, memname, word, meaning):
        if memname == "vocab":
            self.vocab[word] = [meaning, 0]
        elif memname == "incorrect_vocab":
            self.incorrect_vocab[word] = [meaning, self.vocab[word][1], 0]

    def check_meaning(self, word):
        answer = input(f"{word} : ")
        if word in self.vocab:
            print(self.vocab[word][0], answer)
            if self.vocab[word][0] == answer:
                return True
            else:
                self.vocab[word][1] += 1
                if self.vocab[word][1] > 2:
                    self.add_word("incorrect_vocab", word, self.vocab[word][0])
                    self.delete_word("vocab", word)
                return True
        elif word in self.incorrect_vocab:
            if self.incorrect_vocab[word][0] == answer:
                self.incorrect_vocab[word][2] += 1
                if self.incorrect_vocab[word][2] > self.incorrect_vocab[word][1] or self.incorrect_vocab[word][2] == 3:
                    self.add_word("vocab", word, self.vocab[word][0])
                    self.delete_word("incorrect_vocab", word)
                return True
            else:
                self.incorrect_vocab[word][1] += 1
                return True
        else:
            return False

    
    def delete_word(self, memname, word):
        if memname == "vocab":
            try:
                del self.vocab[word]
            except KeyError:
                pass

        elif memname == "incorrect_vocab":
            try:
                del self.incorrect_vocab[word]
            except KeyError:
                pass

    def select_word(self, vocab_num, incorrect_num):
        vocab_keys = list(self.vocab.keys())
        incorrect_keys = list(self.incorrect_vocab.keys())
        if vocab_num > len(vocab_keys):
            vocab_num = len(vocab_keys)
        if incorrect_num > len(incorrect_keys):
            incorrect_num = len(incorrect_keys)

        vocabs = random.sample(vocab_keys, vocab_num)
        incorrect = random.sample(incorrect_keys, incorrect_num)
        return vocabs+incorrect
