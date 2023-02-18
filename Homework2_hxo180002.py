import sys
import os
import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint

seed(1234)


def checklen():  # This method checks for input filepath "anat19.txt" as a system argument.
    if len(sys.argv) > 1:
        if sys.argv[1] == "anat19.txt" and len(sys.argv) == 2:  # Verifying that path is correct
            readfile(sys.argv[1])  # Send filepath over to the function that actually parses the file.
        else:
            print("File path is not specified to anat19.txt. Please try again.")
    else:
        print("File path is not specified to anat19.txt. Please try again.")


def readfile(filepath):  # Function that parses through input file at specific location and preprocesses info.
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:  # Opening file
        text_in = f.read()
    tokens = word_tokenize(text_in)  # Tokenizing information.
    uniquetokens = set(tokens)  # Creating a set for only the unique tokens, later used for lexical diversity.
    lexdiv = len(uniquetokens) / len(tokens)  # Calculating lexical diversity.
    print("The lexical diversity of the input text is: ", "%.2f" % lexdiv)
    ptokens = [t.lower() for t in tokens if t.isalpha() and len(t) > 5 and t not in stopwords.words('english')]
    # The above line is processing text by checking for alphabet, removing stopwords, and keeping words of len > 5
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in ptokens]  # Lemmatization of processed tokens
    ulemmas = set(lemmas)  # Set of lemmas created for part-of-speech tagging
    tags = nltk.pos_tag(ulemmas)  # Tagging of lemmas
    print("Printing first 20 lemmas tagged:")
    print(tags[:20])
    nouns = []
    for x in range(len(tags)):
        if tags[x][1] == "NNP" or tags[x][1] == "NN" or tags[x][1] == "NNS":  # This checks for multiple noun types
            nouns.append(tags[x][0])
    print("Number of tokens after preprocessing (Step a) is ", len(ptokens))
    print("Number of nouns after tagging (Step d) is ", len(nouns))
    guessgame(tokens, nouns)  # Passing over to guessing game.


def guessgame(tokens, nouns):
    dictn = {}  # Initializing dictionary, used for pairing and sorting nouns by their frequency.
    for y in range(len(nouns)):
        dictn[y] = (nouns[y], tokens.count(nouns[y]))  # Filling out dictionary
    sorted_nouns = sorted(dictn.values(), key=lambda x: x[1], reverse=True)  # Sorting dict by frequency.
    wordlist = []
    for z in range(50):
        wordlist.append(sorted_nouns[z][0])  # Translating into list data structure, only taking the 50 most frequent.
    print(wordlist)
    score = 5  # Initialization of game conditions, with both score and exit condition set to default.
    exitcon = bool(False)
    while exitcon is not bool(True):
        score = 5
        gword = wordlist[randint(0, len(wordlist))]  # Random selection of word from list of 50.
        outstring = ""  # String shown to player that also indicates game progress.
        for i in range(len(gword)):
            outstring = outstring + "_"  # Initial setup of new word, with only blank spaces.
        print(outstring)
        while score > 0:
            if "_" not in outstring:  # Victory condition check happens first.
                print("Congratulations, you guessed the word!")
                score = 5
                break
            print("Guess a letter for this word.")
            letter = input()  # Read user input, and respond accordingly.
            if letter is "!":  # Exit command handling
                print("Thank you for playing. Now exiting")
                exitcon = bool(True)
                break
            if len(letter) is not 1 or letter.isalpha() is bool(False):  # Checking for letter input only
                print("ERROR. Please enter a letter. Try again")
                continue
            if letter in outstring:  # Checking for already input letter, skips over rest
                print("You already correctly guessed this letter. Try again.")
                continue
            if letter in gword:  # If user guesses letter correctly, add point and letter to outstring
                score = score + 1
                locs = [r.start() for r in re.finditer(letter, gword)]
                for f in range(len(locs)):
                    outstring = outstring[:locs[f]] + letter + outstring[locs[f] + 1:]  # Displaying newly added letter
                print("Good job, your letter was in the word! Your score is now ", score)
                print(outstring)
            else:  # Guessed letter is incorrect, subtract point
                score = score - 1
                print("Uh oh, your guess was incorrect. Your score is now ", score)
                print(outstring)
        if outstring is gword:  # End of inner while loop win condition, replays with reset score
            print("You won! Here's another word.")
        if score is 0:  # End of inner while loop lose condition, displays answer and replays with reset score
            print("Sorry, you lost. The word was " + gword + ". Here's another word.")


if __name__ == '__main__': # Initial start of the program, sends over to check argument.
    checklen()

