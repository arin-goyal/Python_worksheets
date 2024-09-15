# Installing an external module
# pip install pyttsx3 (text to speech module)

import pyttsx3
engine = pyttsx3.init()
engine.say("good morning boss, how are you today ?")
engine.runAndWait()
