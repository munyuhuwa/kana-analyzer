# -*- coding:utf-8 -*-

import MeCab
import random

import phonetics
import customDictReader

def soramimi(text):
    tagger = MeCab.Tagger("-r/etc/mecabrc")
    parse_result = tagger.parseToNode(text)

    out_text = ""
    while parse_result:
        arr = parse_result.feature.split(",")
        out_word = parse_result.surface
        if (arr[0] == "名詞"):
            vstr = phonetics.getVowelString(arr[8])
            alternative_words = customDictReader.trie.find(vstr)
            if len(alternative_words) > 0:
                out_word = random.choice(alternative_words)
        parse_result = parse_result.next
        out_text += out_word
    return out_text