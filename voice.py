import speech_recognition as speechRecog
import pyttsx3 
  
recog = speechRecog.Recognizer() 

def speak(command):
    eng = pyttsx3.init()
    eng.say(command) 
    eng.runAndWait()
      
  
while(True):    
      
    try:
        with sr.Microphone() as source2:
              
            recog.adjust_for_ambient_noise(source2, duration=0.5)
              
            audioListen = recog.listen(source2)
            getText = recog.recognize_google(audioListen)
            getText = getText.lower()
  
            print("You say: "+getText)
            break
          
    except speechRecog.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
