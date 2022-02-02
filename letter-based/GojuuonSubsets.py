# -*- coding: utf-8 -*-
# 五十音の部分集合を定義するクラス

from enum import IntEnum

import KanaInt
class GojuuonSubsets:
	@classmethod
	def kanaint_list_convert(cls, ch_list):
		return [KanaInt.KanaInt(ch) for ch in ch_list]

	DUMMY_LETTER = KanaInt('＊')
	SOKUON = KanaInt('ッ')
	HATSUON = KanaInt('ン')
	CHOUON = KanaInt('ー')
	YAYUYO = kanaint_list_convert(['ヤ','ユ','ヨ',])
	SUTEGANA_YAYUYO = kanaint_list_convert(['ャ','ュ','ョ',])
	AIUEO = kanaint_list_convert(['ア','イ','ウ','エ','オ',])
	SUTEGANA_AIUEO = kanaint_list_convert(['ァ','ィ','ゥ','ェ','ォ',])
	GOJUUON_TABLE_BY_DAN = [
		kanaint_list_convert(['ア', 'カ', 'サ', 'タ', 'ナ', 'ハ', 'マ', 'ヤ', 'ラ', 'ワ', 'ガ', 'ザ', 'ダ', 'バ', 'パ',]),
		kanaint_list_convert(['イ', 'キ', 'シ', 'チ', 'ニ', 'ヒ', 'ミ', 'ヰ', 'リ', 'ギ', 'ジ', 'ヂ', 'ビ', 'ピ',]),
		kanaint_list_convert(['ウ', 'ク', 'ス', 'ツ', 'ヌ', 'フ', 'ム', 'ユ', 'ル', 'グ', 'ズ', 'ヅ', 'ブ', 'プ', 'ヴ',]),
		kanaint_list_convert(['エ', 'ケ', 'セ', 'テ', 'ネ', 'ヘ', 'メ', 'ヱ', 'レ', 'ゲ', 'ゼ', 'デ', 'ベ', 'ペ',]),
		kanaint_list_convert(['オ', 'コ', 'ソ', 'ト', 'ノ', 'ホ', 'モ', 'ヨ', 'ロ', 'ヲ', 'ゴ', 'ゾ', 'ド', 'ボ', 'ポ']),
	]
	SOKUON_BAD_SUC = [CHOUON, HATSUON,] + AIUEO + SUTEGANA_AIUEO + YAYUYO + SUTEGANA_YAYUYO
	HATSUON_BAD_SUC = [CHOUON,] + SUTEGANA_AIUEO + SUTEGANA_YAYUYO
	SUTEGANA_YAYUYO_GOOD_PRE = GOJUUON_TABLE_BY_DAN[1] + kanaint_list_convert(['ヴ','テ','フ',])
	SUTEGANA_AIUEO_COMMON_GOOD_PRE = GOJUUON_TABLE_BY_DAN[2]
	BAD_FIRST_LETTER = [SOKUON, HATSUON, CHOUON,] + SUTEGANA_AIUEO + SUTEGANA_YAYUYO + kanaint_list_convert(['ヮ', 'ヵ', 'ヶ',])

class GojuuonDan(IntEnum):
	A = 0
	I = 1
	U = 2
	E = 3
	O = 4

class GojuuonGyou(IntEnum):
	A = 0
	KA = 1
	SA = 2
	TA = 3
	NA = 4
	HA = 5
	MA = 6
	YA = 7
	RA = 8
	WA = 9
	GA = 10
	ZA = 11
	DA = 12
	BA = 13
	PA = 14
	SUTE_A = 15
	SUTE_YA = 16
	OTHERS = 17