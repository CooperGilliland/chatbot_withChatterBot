import speech_recognition as sr


def Record():
    #set recording parameters
    sampleRate = 48000
    chunkSize = 2048
    r = sr.Recognizer() #create recognition functionality
    #create microphone object with default mic
    with sr.Microphone(device_index=None, sample_rate=sampleRate, chunk_size=chunkSize) as source:
        r.adjust_for_ambient_noise(source) #calibrate mic based on current environment levels
        print("Speak now")
        audio = r.listen(source) #record audio until levels return to ambient
        try:
            text = r.recognize_google(audio) #use GSR to convert to text
            print(text)
            return text #return the recorded text
        except sr.UnknownValueError:
            print("GSR does not recognize your audio")
        except sr.RequestError as e:
            print("GSR hs not recognized your request; {0}".format(e))
