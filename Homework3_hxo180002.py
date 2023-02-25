import nltk
import math


def runtest():
    from nltk.corpus import wordnet as wn
    from nltk.wsd import lesk
    nltk.download('sentiwordnet')
    nltk.download('gutenberg')
    nltk.download('genesis')
    nltk.download('inaugural')
    nltk.download('nps_chat')
    nltk.download('webtext')
    nltk.download('treebank')
    from nltk.corpus import sentiwordnet as swn
    from nltk.book import text4
    print("Synsets of human: ", wn.synsets('human'))
    print("Definition of first synset: ", wn.synset('homo.n.02').definition())
    print("Example of first synset: ", wn.synset('homo.n.02').examples())
    print("Lemmas of first synset: ", wn.synset('homo.n.02').lemmas())
    print()
    print("Traversing up the hierarchy: ")
    hum = wn.synset('homo.n.02')
    hyp = hum.hypernyms()[0]
    top = wn.synset('entity.n.01')
    while hyp:
        print(hyp)
        if hyp == top:
            break
        if hyp.hypernyms():
            hyp = hyp.hypernyms()[0]
    print("Hypernyms of first synset: ", hum.hypernyms())
    print("Hyponyms of first synset: ", hum.hyponyms())
    print("Meronyms of first synset: ", hum.part_meronyms())
    print("Holonyms of first synset: ", hum.part_holonyms())
    ants = []
    for l in wn.synset('homo.n.02').lemmas():
        ants.append(l.antonyms())
    print("Antonyms of the first synset: ", ants)
    print()
    print("Synsets of living: ", wn.synsets('living'))
    print("Definition of chosen synset: ", wn.synset('live.v.02').definition())
    print("Example of chosen synset: ", wn.synset('live.v.02').examples())
    print("Lemmas of chosen synset: ", wn.synset('live.v.02').lemmas())
    print(wn.synset('live.v.02').hypernyms())
    liv = wn.synset('live.v.02')
    print("Live cannot go further up its hierarchy since it has no hypernyms.")
    print("All the forms of living: ", wn.morphy('living'))
    car = wn.synset('car.n.01')
    truck = wn.synset('truck.n.01')
    print("Comparing car and truck: ")
    print(wn.wup_similarity(car, truck))
    print(lesk('car', 'truck'))
    suffer = swn.senti_synsets('suffer')
    suflist = list(suffer)
    print("List of senti_synsets of suffer: ", suflist)
    for synst in suflist:
        print("Scores of ", synst)
        print(synst.pos_score())
        print(synst.neg_score())
        print(synst.obj_score())
    sent = 'we have suffered greatly for this immense tragedy'
    print("Sentence to evaluate is: ")
    print(sent)
    neg = 0
    pos = 0
    tokens = sent.split()
    for token in tokens:
        syn_list = list(swn.senti_synsets(token))
        if syn_list:
            syn = syn_list[0]
            print(syn)
            neg += syn.neg_score()
            pos == syn.pos_score()
    print("Negative score is ", neg, " Positive score is ", pos)
    print()
    print("Printing collocations.")
    print(text4.collocations())
    vocab = len(set(text4))
    ya = text4.count('United States') / vocab
    print("p(United States) = ", ya)
    y = text4.count('United') / vocab
    print("p(United) = ", y)
    a = text4.count('States') / vocab
    print('p(States) = ', a)
    pmi = math.log2(ya / (y * a))
    print('pmi = ', pmi)


if __name__ == '__main__':
    runtest()


