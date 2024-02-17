import speech_recognition as sr
 
# Initialize the recognizer 
r = sr.Recognizer() 
 
# Exception handling to handle
# exceptions at the runtime
def getPhrase():
    try:
        audiofile = sr.AudioFile("audio.wav")

        with audiofile as source:
        # use the microphone as source for input.
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source, phrase_time_limit=20)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ",MyText)
            return str(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

