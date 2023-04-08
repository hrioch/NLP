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

## Assignment 3 - WordNet
This program shows examples and output of WordNet processing. It uses given sample words, such as human for nouns and living for verbs, to analyze.
For more in-depth analysis on WordNet and its utility, [check out this short document.](WordNet.pdf)
For the sample program, [see here.](Homework3_hxo180002.py)

## Assignment 4 - Ngrams
Language can be split into smaller sliding windows known as N-grams, which are used for language model creation. There are sample programs that take input,
use it to create a basis of language, and try to guess the language of incoming text from a test file. 
The packaging file [can be found here.](Homework4p1_hxo180002.py)
The analysis and comparison file [can be found here.](Homework4p2_hxo180002.py)
A more detailed write-up can be [found here.](Ngrams.pdf)

## Assignment 5 - Sentence Parsing
There are multiple ways to parse a sentence of language. This exercise has examples of three different parsing methods. There are diagrams, definitions,
classifications, and more. Parsing methods include constituency parsing, dependency parsing, and sample role labelling. 
[The document and analysis of this exercise can be found here.](Sentence_Parsing.pdf)

## Assignment 6 - Finding or Building a Corpus
This project creates a web crawler and parser that scans through an initial website, finds 15 relevant websites, prints their text onto output files,
computes word frequency, and prints it. Then, 10 relevant words were chosen from each document and stored into a knowledge base.
[The program can be found here.](Homework6_hxo180002.py)
[Explanation of knowledge base and a sample ChatBot conversation can be found here.](Finding_or_Building_a_Corpus.pdf)

## Assignment 7 - Text Classification
Multiple text classification algorithms were used on a sample dataset and compared in accuracy.
The notebook pdf [can be found here.](Text_Classification_NB.pdf)
The discussion of results [can be found here.](Text_Classification.pdf)
[This is the sample dataset.](best_selling_switch_games.csv)

## Assignment 8 - ACL Paper Summary
A study was conducted on the inaccuracies of table-to-text linearization when rows and/or columns change positions.
A solution, known as TableFormer, was presented and tested.
You can read a summary on this paper [here.](ACLPaperSummary.pdf)