#!/usr/bin/env python3
# Author:    Johannes R. Falnes
# Date:      2019
# Last Edit: 26/12/2019
'''
TODO:
1. Add more hashtypes, hash recognizer?
'''
import hashlib

# Define Username, password hash, hashtype and wordlist

username = input("What is the username? ")
passHash = input("What is your hash? ")
hashType = input("What type of hash is this?\n1. MD5\n2. SHA-256\n3. SHA-512")
wordlist = input("What wordlist do you want to use? \n1. Rockyou.txt\n2. Top12KPasswords.txt \n3. Custom")
# printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)

# Choose which hashing algorithm to use
if (hashType == "1"):
    hashPass = hashlib.md5
if (hashType == "2"):
    hashPass = hashlib.sha256
if (hashType == "3"):
    hashPass = hashlib.sha512
# Choose which dictionary to use
if (wordlist == "1"):
    wordlist = ("rockyou.txt")
if (wordlist == "2"):
    wordlist = ("Top12KPasswords.txt")

# Possibility for custom wordlists
if (wordlist == "3"):
    customWordlist = input("What wordlist do you want to use? ")
    wordlist = customWordlist


# Function for comparing hash to passwords in dictionary
def hashCrack(wordlist, passHash):
    with open(wordlist, encoding='latin_1') as wordL:
        word = wordL.readlines()
    for a in word:
        Var01 = hashPass(a.strip().encode('utf-8'))
        if Var01.hexdigest() == passHash:
            return (a)


cracked = hashCrack(wordlist, passHash)
# If cracked returns something other than 0, print the unhashed password.
if cracked is not None:
    print("Found " + passHash + ":" + cracked.strip() + " in " + wordlist)
else:
    print("Your hash is not in " + wordlist)
