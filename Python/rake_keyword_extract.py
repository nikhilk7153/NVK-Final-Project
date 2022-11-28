import nltk
import string
import numpy
import sys

import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import contractions

numpy.set_printoptions(threshold=sys.maxsize)

nltk.download('punkt')


def RakeExtract(text):
    
    expanded_words = []   
    for word in text.split():
      # using contractions.fix to expand the shortened words
      expanded_words.append(contractions.fix(word))  
   
    expanded_text = ' '.join(expanded_words)
    expanded_text = expanded_text.lower()
    expanded_text = expanded_text.replace(',', '')
    
    text = expanded_text
    
    text_tokens = nltk.word_tokenize(text)
    sub_tokens = []

    for word in text_tokens:
        if word in STOP_WORDS or word in string.punctuation:
            sub_tokens.append("-")
        else:
            sub_tokens.append(word)

    spacetokens = []

    res = ""

    for i in range(0, len(sub_tokens) - 1):
        if sub_tokens[i] == "-":
            if res != "":
                spacetokens.append(res)
            spacetokens.append("-")
            res = ""
        if res == "" and sub_tokens[i] != "-":
            res = sub_tokens[i]

        if sub_tokens[i] != "-" and sub_tokens[i + 1] != "-":
            res += " " + sub_tokens[i + 1]

    if sub_tokens[-1] != "-":
        res += sub_tokens[-1]
    spacetokens.append(res)

    wrdcnt = {}
    for i in sub_tokens:
        if i != "-":
            wrdcnt[i] = wrdcnt.get(i, 0) + 1

    def getinitinfo(tokens):

        wordset = set()
        worddict = {}
        for i in tokens:
            if i != "-":
                wordset.add(i)

        cnt = 0
        for i in wordset:
            worddict[i] = cnt
            cnt += 1
        return worddict

    dic = getinitinfo(sub_tokens)
    N = len(dic)
    graph = np.zeros((N, N))

    # ["hello world space", "-", "food"]
    for i in spacetokens:
        if i != "-":
            spl = i.split()
            for i in range(len(spl)):
                for j in range(i, len(spl)):
                    graph[dic[spl[i]]][dic[spl[j]]] += 1
                    if i != j:
                        graph[dic[spl[j]]][dic[spl[i]]] += 1

    results = []

    degree = np.sum(graph, axis=0)
    for i, (k, v) in enumerate(dic.items()):
        results.append((k, degree[v] / wrdcnt[k]))

    results.sort(key=lambda x: x[1])
    results = results[::-1]

    keywords = set()
    for word in spacetokens:
        texspl = word.split()
        score = 0
        for x in results:
            for y in texspl:
                if x[0] == y:
                    score += x[1]
        keywords.add((word, score))

    keywords = list(keywords)
    keywords.sort(key=lambda x: x[1])
    keywords = keywords[::-1]
    keywords = keywords[:len(keywords) // 3]

    return keywords
