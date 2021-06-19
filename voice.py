import speech_recognition as speechRecog
import pyttsx3


class SpeechRecognition():
	def __init__(self):
		self.recog = speechRecog.Recognizer()
		self.eng = pyttsx3.init()


	def speak(self, command):
		print("Bot say:", command)
		self.eng.say(command)
		self.eng.runAndWait()


	def get_voice_input(self):
		while(True):
			try:
				with speechRecog.Microphone() as source2:

					self.recog.adjust_for_ambient_noise(source2, duration=0.5)

					audioListen = self.recog.listen(source2)
					getText = self.recog.recognize_google(audioListen)
					getText = getText.lower()

					print("You say:", getText)
					return getText

			except speechRecog.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
