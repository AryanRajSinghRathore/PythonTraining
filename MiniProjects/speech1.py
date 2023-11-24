import pyttsx3
ssynth=pyttsx3.init()
voices=ssynth.getProperty('voices')
##print(voices)
ssynth.setProperty('volume',100)
ssynth.setProperty('rate',200)
ssynth.setProperty('voice',voices[0].id)
ssynth.say('HELLO MAN SINGH RATHORE ')
ssynth.runAndWait()
