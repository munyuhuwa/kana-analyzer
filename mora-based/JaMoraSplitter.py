# -*- coding: utf-8 -*-
import re
import ReComposer

class JaMoraSplitter:
	def __loadMoraTable():
		moraTable = list()
		with open('./mora-table.csv', 'r') as f:
			for line in f:
				row = line.rstrip().split('\t')
				if len(row) < 6:
					continue
				moraTable.append(row[1:6])
				# 6番目以降は無視
		return moraTable	

	def __loadSpecialMora():
		specialMora = list()
		with open('./special-mora.csv', 'r') as f:
			for line in f:
				row = line.rstrip().split('\t')
				if row[0] == '':
					continue
				specialMora.append(row[0])
				# 最初の1列だけ
		return specialMora

	def __list2DTo1D(l2d):
		l1d = list()
		for row in l2d:
			l1d += row
		return l1d
	
	# class variables
	moraTable = __loadMoraTable()
	specialMora = __loadSpecialMora()
	moraSet = set(__list2DTo1D(moraTable)+specialMora)
	moraSplitRe = re.compile(ReComposer.composeReFromWordList(list(moraSet)))

	def __new__(cls):
		self = super().__new__(cls)
		# print( "__new__()  myId={}".format( id( self )))
		# print('にゅ' in JaMoraSplitter.moraSet)
		# print(JaMoraSplitter.moraTable)
		# print(JaMoraSplitter.moraSplitRe)
		# print(JaMoraSplitter.moraSplitRe.search('にゅ'))
		return self

	def splitTextByMora(self, text, delimitter=' '):
		if not isinstance(text, str):
			raise TypeError('text: str')
		for m in re.finditer(JaMoraSplitter.moraSplitRe, text):
			print(m)
		return text


# print(JaMoraSplitter().splitTextByMora('こんてぃにゅー'))