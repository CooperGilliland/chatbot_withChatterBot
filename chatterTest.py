from chatterbot import ChatBot
import SpeechRec
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
import os


def CheckInput(text):
    # check user input for exit condition
    if text == "exit":
        return False
    else:
        # Use the chatbot to respond
        Respond(text)
        return True


def Respond(text):
    # generate a generic response
    response = chatterbot.get_response(text)
    print(response)
    # take only the text from the response Statement object
    res = response.text
    # call the google tts api with the response text
    tts = gTTS(text=res, lang='en')
    # save the audio from the api
    tts.save(mpFile)
    # let the system use the default mp3 player
    os.startfile(mpFile)


if __name__ == '__main__':
    try:
        # define parameters for chatterbot
        chatterbot = ChatBot("Test Bot")
        mpFile = "chatRes.mp3"
        chatterbot.set_trainer(ChatterBotCorpusTrainer)
        chatterbot.train(
            # train on the included english language corpus
            "chatterbot.corpus.english"
        )
        print(
            "This is a demonstration the Chatterbot API working with text to speech, and speech recognition\nGo ahead "
            "and ask it something\nWhen you are done just type exit")
        test = True
        while test:
            print("Press 1 for text input, or 2 for voice\n->")
            mode = input()  # get user input for mode selection
            if mode == "1":
                # collect user input
                print("Awaiting Text Input-> ")
                text = input()
                # Process input
                test = CheckInput(text)
            elif mode == "2":
                # Call the function for recording audio
                print("Please wait")
                text = SpeechRec.Record()
                # process input
                test = CheckInput(text)
            else:
                print("Invalid Input")
        os.remove(mpFile)
    except Exception as e:
        print("Due to an error, the program has been terminated.")
