import sys
import pickle
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.util import ngrams
import math


def calculate():
    uniengdict = pickle.load(open("Unigrams.English.p", "rb"))
    biengdict = pickle.load(open("Bigrams.English.p", "rb"))
    print("English pickles opened.")
    unifrndict = pickle.load(open("Unigrams.French.p", "rb"))
    bifrndict = pickle.load(open("Bigrams.French.p", "rb"))
    print("French pickles opened.")
    uniitadict = pickle.load(open("Unigrams.Italian.p", "rb"))
    biitadict = pickle.load(open("Bigrams.Italian.p", "rb"))
    print("Italian pickles opened.")
    openfile = open("data/LangId.test", errors="ignore").read()
    sentlist = openfile.splitlines()
    print()
    open("output.txt", "w").close()
    outf = open("output.txt", "a")

    engsize = len((uniengdict.keys()))
    frnsize = len((unifrndict.keys()))
    itasize = len((uniitadict.keys()))
    outlist = []
    lineno = 0
    for sent in sentlist:
        plapeng = 1
        plapfrn = 1
        plapita = 1
        lineno += 1
        print("This is line", lineno)
        unigrams_test = word_tokenize(sent)
        bigrams_test = list(ngrams(unigrams_test, 2))
        for bigram in bigrams_test:
            n1 = biengdict[bigram] if bigram in biengdict else 0
            d1 = uniengdict[bigram[0]] if bigram[0] in biengdict else 0
            n2 = bifrndict[bigram] if bigram in bifrndict else 0
            d2 = unifrndict[bigram[0]] if bigram[0] in bifrndict else 0
            n3 = biitadict[bigram] if bigram in biitadict else 0
            d3 = uniitadict[bigram[0]] if bigram[0] in biitadict else 0
            plapeng = plapeng * ((n1 + 1) / (d1 + engsize))
            plapfrn = plapfrn * ((n2 + 1) / (d2 + frnsize))
            plapita = plapita * ((n3 + 1) / (d3 + itasize))
        if plapeng > plapfrn and plapeng > plapita:
            outf.write(str(lineno) + " English\n")
            outlist.append(str(lineno) + " English")
            print("This line is likely English.\n")
        else:
            if plapfrn > plapeng and plapfrn > plapita:
                outf.write(str(lineno) + " French\n")
                outlist.append(str(lineno) + " French")
                print("This line is likely French.\n")
            else:
                if plapita > plapeng and plapita > plapfrn:
                    outf.write(str(lineno) + " Italian\n")
                    outlist.append(str(lineno) + " Italian")
                    print("This line is likely Italian.\n")
                else:
                    outf.write(str(lineno) + " English\n")
                    outlist.append(str(lineno) + " English")
                    print("This line is likely English.\n")
    checksol = open("data/LangId.sol").read()
    solsents = checksol.splitlines()
    acc = 0
    wronglines = []
    for x in range(300):
        if str(solsents[x]) == str(outlist[x]):
            acc += 1
        else:
            wronglines.append(x+1)
    propacc = acc/300
    print("Accuracy is ", propacc, "%")
    for y in range(len(wronglines)):
        print(wronglines[y], " was an incorrect line.")

if __name__ == '__main__':
    calculate()
