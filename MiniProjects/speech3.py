import speech_recognition as sr
import webbrowser as wb
r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('SAY SOMETHING.....')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if text =='bye':
                break
            elif text =='iPhone':
                wb.open_new_tab('https://www.amazon.in/s?k=iphone&ref=nb_sb_noss')
            print('YOUR TEXT:',text)
        except Exception as e:
            print(e)
            
