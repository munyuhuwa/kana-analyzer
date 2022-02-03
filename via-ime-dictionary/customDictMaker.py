# -*- coding:utf-8 -*-
# IME辞書形式からカスタムの母音情報辞書を作成
#
# 入力形式
# 1列目 読み
# 2列目 表示
# (3列目 品詞)
# カンマ区切りCSV
#
# 出力形式
# 1列目 母音文字列
# 2列目 表示

import sys
import csv
import os

import phonetics

input_file_path = sys.argv[1]
f = open(input_file_path, "r")
r = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

table = []
for ime_row in r:
    table.append([
        phonetics.getVowelString(ime_row[0]),
        ime_row[1],
    ])

# 重複を削除
seen = []
table = [row for row in table if row not in seen and not seen.append(row)]

out_file_path = "./assets/dict.csv"
out_file_path = os.path.join(os.path.dirname(__file__), out_file_path)
with open(out_file_path, "w") as f:
    w = csv.writer(f)
    w.writerows(table)