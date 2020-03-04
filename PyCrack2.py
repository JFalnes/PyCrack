# Author:        F4lnes
# Created        04.03.2020
import hashlib

wordlist = 'sample.txt'
# hash = 'e10adc3949ba59abbe56e057f20f883e'


class FileCrack:
    def __init__(self, dictionary, hash):
        self.dictionary = dictionary
        self.hash = hash

    def crack_hash(self):
        with open(self.dictionary.strip(), encoding='latin_1') as word:
            wordL = word.readlines()
            for line in wordL:
                myhash = hashlib.md5(line.strip().encode('utf-8'))
                if myhash.hexdigest() == self.hash:
                    return line


with open('hashes.txt', 'r') as file_of_hashes:
    hashes = file_of_hashes.readlines()
    for a in hashes:
        hash = a
        b = FileCrack(wordlist, hash)
        print(str(b.crack_hash()) + ' was found for hash', a)
