# -*- coding:utf-8 -*-

import os
import csv
import aiueoTrie

trie = aiueoTrie.AiueoTrie()

dict_file_path = "./assets/dict.csv"
dict_file_path = os.path.join(os.path.dirname(__file__), dict_file_path)
with open(dict_file_path, "r") as f:
    r = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in r:
        trie.append(row[0], row[1])
