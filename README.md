# NLP
Repository for Human Language Technologies

## Overview of NLP
Document describing elements and interpretations of Natural Language Processing. [The document can be read here.](Overview_of_NLP.pdf)

## Assignment 1 - Basic Text Processing
This program takes an input file to process its information, format it correctly (or prompt proper formatting), and organize it within objects.
These objects are then placed in a dictionary, which is then compressed (using Pickle, into file dict.p) and decompressed to be printed properly. 
[The file can be found here](Homework1_hxo180002.py)

This program is run through Python, with the filepath "data/data.csv" as a system argument. If it is not found, the program will print an error message.
The program will begin to parse through the information stored on data.csv, line by line, and will prompt the user for reentry of ID or phone number when needed.
Afterwards, it will store this information in objects of the Person class, and place these Person objects in a dictionary.
This dictionary is then compressed into dict.p, and immediately opened to be read and printed.

Python has many strengths in text processing with easy string manipulation, no hard-typing of objects, ease of access to/from files, and simple syntax.
All of these properties allow for quick and efficient development of text processing software. 

In doing this assignment, I learned about Pickle, utilizing regex in Python, and using a list of keys to iterate through a dictionary. 
Opening a file, splitting text, and prompting the user were all review.

## Assignment 2 - Word Guessing Game
This program takes an input file to tokenize its information, display information about part-of-speech tagging, lexical diversity, and more.
Afterwards, it prompts the user for a guessing game of the 50 most frequent nouns in the given input file. This file must be named "anat19.txt".
The guessing game chooses a word at random and displays many empty characters to which the user must try to fill out correctly. 
There is a score system and updated output to track progress. The program can be exited with "!" as an input. 
[The file can be found here](Homework2_hxo180002.py)