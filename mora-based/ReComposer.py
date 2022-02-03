# -*- coding: utf-8 -*-
#
# 単語リストから正規表現を作るとき、
# (ab|a|abc|ac)
# のようにすると、
# "ac"という文字列があっても、"ac"で最長一致せず、"a"にマッチしてしまう動作が起こるため、
# 枝分かれ状の正規表現
# a(b(c)?|c)?
# を確実に作成する。
#

import re


class Trie:
	def __init__(self, keySegment) -> None:
		self.keySegment = keySegment
		self.children = dict()
		self.value = None

	def addWord(self, key, value):
		if not isinstance(key, str):
			raise TypeError('')
		keySegments = list(key)
		self.addWordByKeySegments(keySegments, value)

	def addWordByKeySegments(self, keySegments, value):
		if len(keySegments) == 0:
			self.value = value
			return
		if not (keySegments[0] in self.children):
			child = Trie(keySegments[0])
			self.children[keySegments[0]] = child
		self.children[keySegments[0]].addWordByKeySegments(keySegments[1:], value)
		return

	# def iter(self, keySegments):
	# 	appendedKeySegments = keySegments + [self.value,]
	# 	if not(self.value is None):
	# 		key = ''.join(appendedKeySegments)
	# 		yield key
	# 	for _, child in self.children:
	# 		child.iter(appendedKeySegments)
	
	def makeRe(self):
		if not (self.keySegment is None):
			re_text = '' + self.keySegment
		if len(self.children) == 0:
			return re_text
		child_re_texts = [child.makeRe() for child in self.children.values()]
		re_text += '(' + '|'.join(child_re_texts) + ')'
		if not (self.value is None):
			re_text += '?'
		return re_text

def composeReFromWordList(wordList):
	if not isinstance(wordList, list):
		raise TypeError('')
	if not all([isinstance(word, str) for word in wordList]):
		raise TypeError('')
	tree = Trie('')
	for word in wordList:
		tree.addWord(word, True)
	return tree.makeRe()
