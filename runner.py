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

		if sentence == "good bye":
			break

		compare = Compare(INSTRUCTIONS, DB().get_data())
		instruction = compare.getInstruction(sentence)
		symbol = compare.getStock(sentence)


		recognizer.speak("You are instructing to {0} {1}. Is it correct?".format(instruction[0], symbol[0]))
		confirmation = recognizer.get_voice_input()

		if "yes" in confirmation.lower():
			recognizer.speak("Done")
