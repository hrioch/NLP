import urllib
import re
from urllib.request import Request, urlopen
import math
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
import pickle


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
vocab = set()


def readsite():
    url = 'https://en.wikipedia.org/wiki/Nintendo'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(html)
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            if ('Nintendo' in link_str or 'nintendo' in link_str) and ('wiki' not in link_str) and ('archive' not in link_str) and ('jp' not in link_str) and ('edn' not in link_str):
                if link_str.startswith('/url?q='):
                        link_str = link_str[7:]
                        print('MOD:', link_str)
                if '&' in link_str:
                        i = link_str.find('&')
                        link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                        f.write(link_str + '\n')
    with open('urls.txt', 'r') as r:
        urls = r.read().splitlines()
    urls = urls[:15]
    print(urls)
    for u in range(len(urls)):
        outc = u+1
        outf = "output" + str(outc) + ".txt"
        print("Reading site ", urls[u])
        req = Request(urls[u], headers={'User-Agent': 'Mozilla/5.0'})
        read = urlopen(req).read()
        soupr = BeautifulSoup(read)
        for script in soupr(["script", "style"]):
            script.extract()
        text = soupr.get_text()
        text_chunks = [chunk for chunk in text.splitlines() if not re.match(r'^\s*$', chunk)]
        print("Printing to " + outf)
        with open(outf, 'w', encoding="utf-8") as o:
            for t in text_chunks:
                #print(t)
                o.write(t)
    tf_dicts = []
    for k in range(len(urls)):
        num = k + 1
        readf = "output" + str(num) + ".txt"
        print("Reading " + readf)
        tf_dicts.append(tf(readf))
    vocab = set(tf_dicts[0].keys())
    for y in range(1, len(urls)):
        vocab = vocab.union(set(tf_dicts[y].keys()))
    print("Number of unique words: ", len(vocab))
    idf_dict = {}
    vocab_by_topic = []
    for z in range(len(tf_dicts)):
        vocab_by_topic.append(tf_dicts[z].keys())

    for term in vocab:
        temp = ['x' for voc in vocab_by_topic if term in voc]
        idf_dict[term] = math.log((1 + len(tf_dicts)) / (1 + len(temp)))
    tf_idfs = []
    for i in range(len(tf_dicts)):
        tf_idfs.append(tfidf(tf_dicts[i], idf_dict))
    for j in range(len(tf_idfs)):
        doc_term_weights = sorted(tf_idfs[j].items(), key=lambda x: x[1], reverse=True)
        print("doc " + str(j+1) + " ", doc_term_weights[:25])
    doc1most = ["nintendo", "price", "regular", "mario", "dlc", "hollywood", "metroid", "studios", "universal", "switch"]
    doc2most = ["wii", "released", "launched", "players", "u", "super", "advance", "titles", "ds", "pokémon"]
    doc3most = ["fortune", "luck", "heaven", "yamazaki", "connection", "nin", "gorges", "kanji", "ten", "plausible"]
    doc4most = ["beauty", "deck", "hanafuda", "cards", "photo", "seasons", "continues", "natural", "blossoms", "traditional"]
    doc5most = ["cameo", "earn", "commission", "york", "nintendo", "links", "creator", "encourages", "playable", "extensive"]
    doc6most = ["hiroshi", "sekiryo", "feature", "deal", "atari", "conservative", "haskell", "yamauchi", "yokoi", "cartridges"]
    doc7most = ["insider", "user", "warioware", "love", "score", "produces", "club", "device", "shape", "person"]
    doc8most = ["oldest", "collection", "box", "harrah", "earliest", "items", "mistake", "bill", "closing", "marufuku"]
    doc9most = ["calender", "item", "promotional", "shame", "bad", "torn", "national", "great", "kanji", "days"]
    doc10most = ["kimishima", "wii", "iwata", "president", "global", "device", "health", "benefits", "politics", "yamauchi"]
    doc11most = ["pokémon", "movie", "eshop", "download", "iwata", "kimishima", "furukawa", "switch", "yamauchi", "president"]
    doc12most = ["princess", "sold", "bowser", "worldwide", "super", "insider", "system", "video", "million", "zelda"]
    doc13most = ["yokoi", "yamauchi", "source", "portable", "firm", "salaryman", "popeye", "sharp", "gunpei", "adventure"]
    doc14most = ["laughs", "asks", "development", "research", "iwata", "watch", "color", "design", "system", "block"]
    doc15most = ["laughs", "watch", "display", "ball", "title", "asks", "calculator", "iwata", "idea", "research"]
    docwords = []
    docwords.append(doc1most)
    docwords.append(doc2most)
    docwords.append(doc3most)
    docwords.append(doc4most)
    docwords.append(doc5most)
    docwords.append(doc6most)
    docwords.append(doc7most)
    docwords.append(doc8most)
    docwords.append(doc9most)
    docwords.append(doc10most)
    docwords.append(doc11most)
    docwords.append(doc12most)
    docwords.append(doc13most)
    docwords.append(doc14most)
    docwords.append(doc15most)
    pickle.dump(docwords, open('list.p', 'wb'))  # write binary
    # end of program
    print("end of crawler")


def tf(file):
    with open(file, 'r', encoding="utf-8") as f:
        doc = f.read().lower()
        doc = doc.replace('\n', ' ')
    tf_dict = {}
    tokens = word_tokenize(doc)
    tokens = [w for w in tokens if w.isalpha() and w not in stopwords]
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)
    return tf_dict


def tfidf(tf_dict, idf_dict):
    tf_idf = {}
    for t in tf_dict.keys():
        tf_idf[t] = tf_dict[t] * idf_dict[t]

    return tf_idf


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readsite()


