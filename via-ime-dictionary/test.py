import sys
import phonetics
import customDictReader

word = input('input a word\n')
vstr = phonetics.getVowelString(word)
# print(vstr)
# print(customDictReader.trie)
# print(customDictReader.trie.tree.values)
print(customDictReader.trie.find(vstr))