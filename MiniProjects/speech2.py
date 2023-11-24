##SPEECH TO TEXT
import speech_recognition as sr
r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('say kuch bolo......')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print('ye bola aapne>>>',text)









    
