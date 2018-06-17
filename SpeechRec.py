import speech_recognition as sr


def Record():
    try:
        # set recording parameters
        sampleRate = 48000
        chunkSize = 2048
        r = sr.Recognizer()  # create recognition functionality
        # create microphone object with default mic
        with sr.Microphone(device_index=None, sample_rate=sampleRate, chunk_size=chunkSize) as source:
            r.adjust_for_ambient_noise(source)  # calibrate mic based on current environment levels
            print("Speak now")
            audio = r.listen(source)  # record audio until levels return to ambient
        text = r.recognize_google(audio)  # use GSR to convert to text
        print(text)  # output a text version of what the user said
        return text  # return the recorded text
    except sr.UnknownValueError:  # catch the error where the user audio is unknown
        print("GSR does not recognize your audio")
    except sr.RequestError as e:  # catch  failed requests
        print("GSR hs not recognized your request; {0}".format(e))
