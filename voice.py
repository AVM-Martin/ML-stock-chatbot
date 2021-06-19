import speech_recognition as speechRecog
import pyttsx3


class SpeechRecognition():
	def __init__(self):
		self.recog = speechRecog.Recognizer()


	def speak(self, command):
		eng = pyttsx3.init()
		eng.say(command)
		eng.runAndWait()


	def get_voice_input(self):
		while(True):
			try:
				with speechRecog.Microphone() as source2:

					recog.adjust_for_ambient_noise(source2, duration=0.5)

					audioListen = recog.listen(source2)
					getText = recog.recognize_google(audioListen)
					getText = getText.lower()

					print("You say: "+getText)
					return getText

			except speechRecog.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
