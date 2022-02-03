# -*- coding: utf-8 -*-
import re
import ReComposer

class JaMoraSplitter:
	# class variables
	moraTable = list()
	specialMora = list()
	moraSet = set() # 重複なし
	moraSplitRe = None

	@classmethod
	def loadMoraList(cls):
		with open('./mora-table.csv', 'r') as f:
			for line in f:
				row = line.rstrip().split('\t')
				if len(row) < 6:
					continue
				JaMoraSplitter.moraTable.append(row[1:6])
				for item in row[1:6]:
					cls.moraSet.add(item)
				# 6番目以降は無視
		with open('./special-mora.csv', 'r') as f:
			for line in f:
				row = line.rstrip().split('\t')
				if row[0] == '':
					continue
				JaMoraSplitter.specialMora.append(row[0])
				JaMoraSplitter.moraSet.add(row[0])
				# 最初の1列だけ
		# print('にゅ' in JaMoraSplitter.moraSet)
		# print('|'.join(list(JaMoraSplitter.moraSet)))
		re_text = ReComposer.composeReFromWordList(list(cls.moraSet))
		JaMoraSplitter.moraSplitRe = re.compile(re_text)
		# print(JaMoraSplitter.moraSplitRe)
		# print(JaMoraSplitter.moraSplitRe.search('にゅ'))

	def __new__(cls):
		self = super().__new__(cls)
		# print( "__new__()  myId={}".format( id( self )))
		self.loadMoraList()
		return self

	def splitTextByMora(self, text, delimitter=' '):
		if not isinstance(text, str):
			raise TypeError('text: str')
		for m in re.finditer(JaMoraSplitter.moraSplitRe, text):
			print(m)
		return text


# print(JaMoraSplitter().splitTextByMora('こんてぃにゅー'))