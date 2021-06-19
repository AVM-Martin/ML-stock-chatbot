import nltk


class Compare:
	def __init__(instruction_list, stock_list):
		self.instruction_list = instruction_list
		self.stock_list = stock_list

	def getTopSimilar(self, data, inp):
		inp = inp.upper()
		#return max top 3
		value = []
		for dat, freq in data:
			value.append( (nltk.edit_distance(None, dat, inp), freq, dat) )
		value = sorted(value, reverse=True)

		n = min(len(data), 3)
		return value[:n][2]


	def getStock(self, inp):
		return self.getTopSimilar(self.stock_list, inp)


	def getInstruction(instruction_list, inp):
		return self.getTopSimilar(self.instruction_list, inp)


