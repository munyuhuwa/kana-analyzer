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
	danList = moraTable[0] # あいうえお
	gyouList = [row[0] for row in moraTable] # あかさたな...
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

	# ホワイトリストにあるモーラにのみコールバックを適用
	def splitWithCallbackForValidMora(self, text, func=None):
		parts = []
		tmpIdx = 0
		for m in re.finditer(JaMoraSplitter.moraSplitRe, text):
			if m.start() > tmpIdx:
				parts.append(text[tmpIdx:m.start()])
			if func is None:
				parts.append(text[m.start():m.end()])
			else:
				parts.append(func(text[m.start():m.end()]))# ここに適用
			tmpIdx = m.end()
		return parts

	def insertSeparatorIntoText(self, text, delimitter=','):
		if not isinstance(text, str):
			raise TypeError('text: str')
		parts = self.splitWithCallbackForValidMora(text, None)
		return delimitter.join(parts)

	# 引数は2次元形式の表にあるモーラのみ可
	def tableIndice(self, query):
		for i in range(len(JaMoraSplitter.moraTable)):
			row = JaMoraSplitter.moraTable[i]
			for j in range(len(row)):
				if row[j] == query:
					return (i, j,)
		raise ValueError('')

	# 引数はあいうえおのみ可
	def danIndex(self, query):
		return JaMoraSplitter.danList.index(query)

	# 引数はあかさたな...のみ可 
	def gyouIndex(self, query):
		return JaMoraSplitter.gyouList.index(query)

	def __moveDan(self, srcIdx, dstIdx, mora):
		try:
			idc = self.tableIndice(mora)
		except:
			return mora
		if idc[1] == srcIdx:
			return JaMoraSplitter.moraTable[idc[0]][dstIdx]
		else:
			return mora

	def __moveGyou(self, srcIdx, dstIdx, mora):
		try:
			idc = self.tableIndice(mora)
		except:
			return mora
		if idc[0] == srcIdx:
			return JaMoraSplitter.moraTable[dstIdx][idc[1]]
		else:
			return mora 

	def moveDanText(self, src, dst, text):
		try:
			srcIdx = self.danIndex(src)
			dstIdx = self.danIndex(dst)
		except:
			return text
		return ''.join(self.splitWithCallbackForValidMora(text, lambda x: self.__moveDan(srcIdx, dstIdx, x)))

	def moveGyouText(self, src, dst, text):
		try:
			srcIdx = self.gyouIndex(src)
			dstIdx = self.gyouIndex(dst)
		except:
			return text
		return ''.join(self.splitWithCallbackForValidMora(text, lambda x: self.__moveGyou(srcIdx, dstIdx, x)))

	def isVowelCommon(self, text1, text2):
		mList1 = [t[0] for t in re.findall(JaMoraSplitter.moraSplitRe, text1)]
		mList2 = [t[0] for t in re.findall(JaMoraSplitter.moraSplitRe, text2)]
		if len(mList1) != len(mList2):
			return False
		flg = True
		for i in range(len(mList1)):
			try:
				idc1 = self.tableIndice(mList1[i])
				idc2 = self.tableIndice(mList2[i])
				# print('%d %d' % idc1)
				# print('%d %d' % idc2)
				if idc1[1] != idc2[1]:
					flg = False
					break
			except:
				# 五十音表にないときは完全一致が必要
				if mList1[i] != mList2[i]:
					flg = False
					break
		return flg

# print(JaMoraSplitter().insertSeparatorIntoText('こんてぃにゅー'))
# print(JaMoraSplitter().tableIndice('ふぁ'))
# print(JaMoraSplitter().danIndex('う'))
# print(JaMoraSplitter().gyouIndex('にゃ'))
# print(JaMoraSplitter().moveGyouText('さ', 'しゃ', 'すごいのぉ'))
# print(JaMoraSplitter().isVowelCommon('らーめん', 'かーてん'))
# print(JaMoraSplitter().isVowelCommon('らーめん', 'かんてん'))
# print(JaMoraSplitter().isVowelCommon('ぐうぜん', 'りゅうねん'))
# print(JaMoraSplitter().isVowelCommon('あけちみつひで', 'だけにみついで'))