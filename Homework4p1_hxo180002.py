import sys
from nltk import word_tokenize
from nltk.util import ngrams
import pickle


def preptext(filearg):  # This method checks for input filepath "anat19.txt" as a system argument.
    raw_text = open(filearg, errors="ignore").read()
    print("Opened ", filearg)
    unigrams = word_tokenize(raw_text)
    bigrams = list(ngrams(unigrams, 2))

    print(len(unigrams))
    print(len(set(unigrams)))
    print(len(set(bigrams)))

    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

    print("Completed ", filearg)

    return unigram_dict, bigram_dict


if __name__ == '__main__':
    print("Preparing text of English training model.")
    unieng, bieng = preptext("data/LangId.train.English")
    print("Preparing text of French training model.")
    unifrn, bifrn = preptext("data/LangId.train.French")
    print("Preparing text of Italian training model.")
    uniita, biita = preptext("data/LangId.train.Italian")

    pickle.dump(unieng, open("Unigrams.English.p", "wb"))
    pickle.dump(bieng, open("Bigrams.English.p", "wb"))
    pickle.dump(unifrn, open("Unigrams.French.p", "wb"))
    pickle.dump(bifrn, open("Bigrams.French.p", "wb"))
    pickle.dump(uniita, open("Unigrams.Italian.p", "wb"))
    pickle.dump(biita, open("Bigrams.Italian.p", "wb"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
