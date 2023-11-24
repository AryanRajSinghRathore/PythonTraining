##PERSONAL ASISTANT
import webbrowser as wb
import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('say kuch bolo......')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print('ye bola aapne>>>',text)
while True:
    
    if text=='iPhone':
        wb.open_new_tab('https://www.amazon.in/s?k=iphone+13&sprefix=ip%2Caps%2C280&ref=nb_sb_ss_pltr-ranker-24hours_1_2')
    elif text=='Bye':
        break
    else:
        print('PLEASE SPEAK AGAIN')
        
   
