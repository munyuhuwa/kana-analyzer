# -*- coding: utf-8 -*-
# 平仮名/片仮名テキストの
# # 解析
# # バリデーション
# # 制約に従ったランダム生成
# を行うライブラリ
# @munyuhuwa

import KanaInt
import GojuuonSubsets

class KanaAnalyzerValidationOptions:
	DENY_BAD_SUTEGANA_YAYUYO = True
	DENY_BAD_SUTEGANA_AIUEO = True
	DENY_BAD_HATSUON = True
	DENY_BAD_SOKUON = True
	DENY_BAD_FIRST_LETTER = True

class KanaAnalyzer:
	def __init__(self) -> None:
		pass

	KANAINT_DAN_SAFE_LIMIT = 132

	# 型変換 (検索しやすくするため)
	@classmethod
	def str_to_list(cls, s) -> list:
		if not isinstance(s, str):
			raise TypeError()
		ki_list = []
		for ch in list(s):
			try:
				ki_list.append(KanaInt.KanaInt(ch))
			except:
				pass
		return ki_list

	@classmethod
	def list_to_str(cls, ki_list) -> str:
		if not isinstance(ki_list, list):
			raise TypeError()
		s = ''
		for ki in ki_list:
			if not isinstance(ki, KanaInt):
				raise TypeError()
			s+= ki.to_str()
		return s
	
	# オプションで禁則とできる特徴の検索
	# 特定の文字+「ャュョ」の検索
	# 並びの最初の文字の位置を返す
	@classmethod
	def index_bad_sutegana_yayuyo(cls, ki_list) -> int:
		if len(ki_list) <= 1:
			return -1
		for i in range(len(ki_list)-1):
			if ki_list[i+1] in GojuuonSubsets.GojuuonSubsets.YAYUYO:
				if not(ki_list[i] in GojuuonSubsets.GojuuonSubsets.SUTEGANA_YAYUYO_GOOD_PRE):
					return i
		return -1

	# 特定の文字+「ァィゥェォ」の検索
	@classmethod
	def index_bad_sutegana_aiueo(cls, ki_list) -> int:
		if len(ki_list) <= 1:
			return -1
		for i in range(len(ki_list)-1):
			if ki_list[i+1] in GojuuonSubsets.GojuuonSubsets.AIUEO:
				if ki_list[i] in GojuuonSubsets.GojuuonSubsets.SUTEGANA_AIUEO_COMMON_GOOD_PRE:
					continue
				elif ki_list[i].dan_equal_to(ki_list[i+1]):
					continue
				else:
					return i
		return -1

	# 「ン」+特定の文字の検索
	@classmethod
	def index_bad_hatsuon(cls, ki_list)->int:
		if len(ki_list) <= 1:
			return -1
		for i in range(len(ki_list)-1):
			if ki_list[i] == GojuuonSubsets.GojuuonSubsets.HATSUON:
				if ki_list[i+1] in GojuuonSubsets.GojuuonSubsets.HATSUON_BAD_SUC:
					return i
		return -1

	# 「ッ」+特定の文字の検索
	@classmethod
	def index_bad_sokuon(cls, ki_list)->int:
		if len(ki_list) <= 1:
			return -1
		for i in range(len(ki_list)-1):
			if ki_list[i] == GojuuonSubsets.GojuuonSubsets.SOKUON:
				if ki_list[i+1] in GojuuonSubsets.GojuuonSubsets.SOKUON_BAD_SUC:
					return i
		return -1

	# 先頭文字の禁則
	@classmethod
	def is_bad_first_letter(cls, ki_list)->bool:
		if len(ki_list) == 0:
			return False
		return ki_list[0] in GojuuonSubsets.GojuuonSubsets.BAD_FIRST_LETTER

	# 指定した禁則をすべてクリアするか検証
	@classmethod
	def validate(cls, ki_list, options=KanaAnalyzerValidationOptions())->bool:
		if KanaAnalyzerValidationOptions.DENY_BAD_FIRST_LETTER:
			if KanaAnalyzer.is_bad_first_letter(ki_list):
				return False
		if KanaAnalyzerValidationOptions.DENY_BAD_HATSUON:
			if KanaAnalyzer.index_bad_hatsuon >= 0:
				return False
		if KanaAnalyzerValidationOptions.DENY_BAD_SOKUON:
			if KanaAnalyzer.index_bad_sokuon >= 0:
				return False
		if KanaAnalyzerValidationOptions.DENY_BAD_SUTEGANA_AIUEO:
			if KanaAnalyzer.index_bad_sutegana_aiueo >= 0:
				return False
		if KanaAnalyzerValidationOptions.DENY_BAD_SUTEGANA_YAYUYO:
			if KanaAnalyzer.index_bad_sutegana_yayuyo >= 0:
				return False
		return True

	# 上記の、引数に文字列を直接指定できる版
	def validate_str(cls, s, options=KanaAnalyzerValidationOptions())->bool:
		return KanaAnalyzer.validate(KanaAnalyzer.str_to_list(s), options)

	# オプションに従って正規化
	# def normalize_str(cls, s, options)->str:
	# 	pass

	# 母音を与えられた規則で差し替えた文字列を生成
	# mappings [(GojuuonDan, GojuuonDan,), ...]
	@classmethod
	def replace_vowels_str(cls, s, mappings)->str:
		ki_list = KanaAnalyzer.str_to_list(s)
		ki_list_replaced = []
		for ki in ki_list:
			if ki <= KanaAnalyzer.KANAINT_DAN_SAFE_LIMIT:
				for mapping in mappings:
					try:
						new_ki = KanaInt(ki - mapping[0] + mapping[1])
					except:
						new_ki = KanaInt(ki)
					ki_list_replaced.append(new_ki)
		return ki_list_replaced
		#小文字があるときの動作が考慮されていない問題あり

	# 子音を与えられた規則で差し替えた文字列を生成
	# @classmethod
	# def replace_consonants_str(cls, s, mappings)->str:
	# 	pass

	# オタク特有の発音に変換する
	# @classmethod
	# def meiteikei(cls, s)->str:
	# 	pass
	
	# 同じ文字が1回だけ現れるか
	@classmethod
	def is_letter_used_only_once(cls, ki_list)-> bool:
		return len(ki_list) == len(list(set(ki_list)))
