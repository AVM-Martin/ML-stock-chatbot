import nltk


class Compare:
	def __init__(self, instruction_list, stock_list):
		self.instruction_list = instruction_list
		self.stock_list = stock_list

	def getTopSimilar(self, data, inp):
		inp = inp.upper()
		#return max top 3
		value = []
		for dat, freq in data:
			value.append( (nltk.edit_distance(dat, inp), -freq, dat) )
		value = sorted(value)

		n = min(len(data), 3)
		result = []
		for i in range(n):
			result.append(value[i][2])
		return result


	def getStock(self, inp):
		return self.getTopSimilar(self.stock_list, inp)


	def getInstruction(self, inp):
		return self.getTopSimilar(self.instruction_list, inp)
