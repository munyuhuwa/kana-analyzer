# -*- coding:utf-8 -*-

AIUEO = ["a", "i", "u", "e", "o", "_"]

class AiueoTrieNode:
    def __init__(self):
        self.values = []
        self.children = [None, None, None, None, None, None,]

    def append(self, vowel_indexes, value):
        if len(vowel_indexes) == 0:
            self.values.append(value)
            return
        current_vowel_index = vowel_indexes.pop(0)
        if self.children[current_vowel_index] is None:
            self.children[current_vowel_index] = AiueoTrieNode()
        self.children[current_vowel_index].append(vowel_indexes, value)
    
    def find(self, vowel_indexes):
        if len(vowel_indexes) == 0:
            return self.values
        current_vowel_index = vowel_indexes.pop(0)
        if self.children[current_vowel_index] is None:
            return []
        return self.children[current_vowel_index].find(vowel_indexes)

class AiueoTrie:
    def __init__(self):
        self.tree = AiueoTrieNode()
    
    def __getVowelIndexes(self, vstr):
        vowels = list(vstr)
        vowel_indexes = []
        for vowel in vowels:
            try:
                vowel_indexes.append(AIUEO.index(vowel))
            except ValueError as e:
                return None
        return vowel_indexes

    def append(self, vstr, value):
        vowel_indexes = self.__getVowelIndexes(vstr)
        if vowel_indexes is None:
            return
        self.tree.append(vowel_indexes, value)
    
    def find(self, vstr):
        vowel_indexes = self.__getVowelIndexes(vstr)
        if vowel_indexes is None:
            return []
        return self.tree.find(vowel_indexes)       
