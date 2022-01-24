import KanaInt

# KanaInt('あ')
# KanaInt('ヰ')
# KanaInt('あああ')
# KanaInt('☆')
# KanaInt(0)
# KanaInt(334)

# class Test(int):
# 	def __new__(self, arg):
# 		self = int.__new__(self, arg)
# 		print('hello')
# 		return self
# 	def __init__(self, arg) -> None:
# 		print(arg)
# 		super().__init__()
# Test(334)

a = KanaInt.KanaInt(25)
print(a.to_str())

print(KanaInt.KanaInt('て').dan_equal_to(KanaInt.KanaInt('ね')))