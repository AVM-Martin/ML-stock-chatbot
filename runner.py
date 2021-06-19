from nltk.tokenize import word_tokenize as tokenizer

from compare import Compare
from db import DB
from voice import SpeechRecognition


INSTRUCTIONS = [
	("buy", 0),
	("sell", 0),
]


if __name__ == "__main__":
	db = DB()
	recognizer = SpeechRecognition()

	while True:
		recognizer.speak("Please give me an instruction")

		sentence = recognizer.get_voice_input()

		if sentence == "good bye" or sentence == "goodbye":
			recognizer.speak("See you next time")
			break

		compare = Compare(INSTRUCTIONS, DB().get_data())
		instructions = compare.getInstruction(sentence)
		symbols = compare.getStock(sentence)

		for symbol in symbols:
			instruction = instructions[0]

			recognizer.speak(
				"You are instructing to {0} {1}. Is it correct?".format(instruction, symbol)
			)
			confirmation = recognizer.get_voice_input()

			if "yes" in confirmation.lower():
				recognizer.speak("Done")
				break
			elif "cancel" in confirmation.lower():
				recognizer.speak("Sorry")
				break
