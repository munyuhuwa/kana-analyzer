# -*- coding:utf-8 -*-

import re

COMBINED_KANA_TO_VOWEL_SETTING = {
    "あかさたなはまやらわがざだばぱアカサタナハマヤラワガザダバパ": "a",
    "いきしちにひみりゐぎじぢびぴイキシチニヒミリヰギジヂビピ": "i",
    "うくすつぬふむゆるぐずづぶぷウクスツヌフムユルグズヅブプ": "u",
    "えけせてねへめれゑげぜでべぺエケセテネヘメレヱゲゼデベペ": "e",
    "おこそとのほもよろをごぞどぼぽオコソトノホモヨロヲゴゾドボポ": "o",
    "ぁゃァャ": "xa",
    "ぃィ": "xi",
    "ぅゅゥュ": "xu",
    "ぇェ": "xe",
    "ぉょォョ": "xo",
    "ー": "l",
    # "ンッ": "_",
}

kana_to_vowel = {}
for combined_kana, vowel in COMBINED_KANA_TO_VOWEL_SETTING.items():
    for kana in list(combined_kana):
        kana_to_vowel[kana] = vowel

def __getVowel(kana):
    if kana in kana_to_vowel:
        return kana_to_vowel[kana]
    return "_"

def __normalizeLongMora(word):
    word2 = word + ''
    pattern = re.compile(r'([えけせてねへめれゑげぜでべぺエケセテネヘメレヱゲゼデベペ])[いぃイィ]')
    word2 = pattern.sub(r'\1エ', word2)
    pattern = re.compile(r'([おこそとのほもよろをごぞどぼぽオコソトノホモヨロヲゴゾドボポ])[うぅウゥ]')
    word2 = pattern.sub(r'\1エ', word2)
    return word2

def __processSmallKana(vstr):
    pattern = re.compile(r'[aiueo]x')
    return pattern.sub(r'', vstr)

def __processLongMora(vstr):
    pattern = re.compile(r'([aiueo])l')
    return pattern.sub(r'\1\1', vstr)

def getVowelString(word):
    vstr = "".join(map(__getVowel, list(word)))
    vstr = __processSmallKana(vstr)
    vstr = __processLongMora(vstr)
    return vstr

if __name__ == "__main__":
    pass
