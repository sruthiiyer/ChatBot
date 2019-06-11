import speech_recognition as sr

r = sr.Recognizer()

def function(audio):

    try:

        print("PLeeeesss")
        
        x=r.recognize_google(audio)
        
        print('google thinks u hv said :\n' + r.recognize_google(audio))
        
        return x
        
    except:
        
        print('cant recognise ur voice...try again')


