# -*- coding:utf-8 -*-

import sys

import soramimi

text = input("文章を入力してください。\n")
out_text = soramimi.soramimi(text)
print(out_text)