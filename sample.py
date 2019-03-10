# import webbrowser as wb
# chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# rec = sr.Recognizer()
# with sr.Microphone() as source:
#     rec.adjust_for_ambient_noise(source)
#     print("Common Amey please speak")
#     audioFile = rec.listen(source)

# try:
#     text = rec.recognize_google(audioFile)
#     print("You said this macha: {}".format(text))
#     wb.get(chrome_path).open(text)
# except Exception as e:
#     print("Sorry Amey you dont know how to", e)

# Writing the file

# with open("microphone-results.wav","wb") as f:
#     f.write(audioFile.get_wav_data())
# import timeout


import speech_recognition as sr
import webbrowser
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
from textblob import TextBlob
r3 = sr.Recognizer()
r2 = sr.Recognizer()
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    speak.Speak('Welcome to the world of davinci - How are you doing')
    print("[Your feelings]")
    audioFeeling = r.listen(source)
    text = TextBlob(r3.recognize_google(audioFeeling))
    print(text.sentiment.polarity)

with sr.Microphone() as source:
    speak.Speak('Is there any particular book you want to read')
    print("[ YES | NO ]")
    audio = r.listen(source)


    if "yes" in r3.recognize_google(audio):
        url = "https://www.goodreads.com/search?utf8=✓&search%5Bquery%5D="
        r3 = sr.Recognizer()
        with sr.Microphone() as source:
            speak.Speak('which book do you want')
            audioyes = r.listen(source)
            try:
                text = r3.recognize_google(audioyes)
                speak.Speak('davinci thinks you said:' + text)
                print("davinci thinks you said:" + text)
                webbrowser.open_new(url+text)
            except sr.UnknownValueError:
                print("sorry Coukdn't understand")
            except sr.RequestError as e:
                print("Failed to retrive results", e)

    if "no" in r3.recognize_google(audio):
        with sr.Microphone() as source:
            speak.Speak('Here are few of my recommendations')
            print('Here are few of my recommendations')
            audiono = r.listen(source)
            try:
                text = r3.recognize_google(audiono)
                speak.Speak('davinci thinks you said:' + text)
                print("davinci thinks you said:" + text)

                # webbrowser.open_new(url+text)
            except sr.UnknownValueError:
                print("sorry Coukdn't understand")
            except sr.RequestError as e:
                print("Failed to retrive results", e)


# if "books" in r3.recognize_google(audioFeeling):


# speak.Speak('hmmm')
    # r3 = sr.Recognizer()
    # try:
    #     text = r3.recognize_google(audioFeeling)    
    #     print(text)
    #     text = TextBlob(text)
    #     print(text.sentiment)
    # except sr.UnknownValueError:   
    #     speak.Speak("sorry Couldn't understand")
    # except sr.RequestError as e:
    #     speak.Speak("Failed to retrive results") 


        # print("sorry Coukdn't understand")
        # print("Failed to retrive results", e)
           
    # speak.Speak('is there any specific kind of book would like to raed")    
    # print("[I don't know | good | exiciting | love story]")    


        # speak.Speak('searching for books - Which book do you want:')
        # print("searching for books - Which book do you want:")
        # audio = r.listen(source)
        # try:
        #     text = r3.recognize_google(audio)
        #     speak.Speak('davinci thinks you said:' + text)
        #     print("davinci thinks you said:" + text)
        #     b = TextBlob(text)
        #     print(b.sentiment)
        #     # webbrowser.open_new(url+text)
        # except sr.UnknownValueError:
        #     print("sorry Coukdn't understand")
        # except sr.RequestError as e:
        #     print("Failed to retrive results", e)


#         if "news" in r3.recognize_google(audioFeeling):

#     url = "https://www.goodreads.com/search?utf8=✓&search%5Bquery%5D="
#     r3 = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak.Speak('searching for books - Which book do you want:')
#         print("searching for books - Which book do you want:")
#         audio = r.listen(source)

#         try:
#             text = r3.recognize_google(audio)
#             print("davinci thinks you said:" + text)
#             webbrowser.open_new(url+text)
#         except sr.UnknownValueError:
#             print("sorry Coukdn't understand")
#         except sr.RequestError as e:
#             print("Failed to retrive results", e)

            
# if "music" in r3.recognize_google(audioFeeling):

#     url2 = "https://www.youtube.com/results?search_query="
#     r3 = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak.Speak('searching for music video - Please tell the name of the music :')
#         print("searching for music video - Please tell the name of the music :")
#         audio = r.listen(source)

#         try:
#             text = r3.recognize_google(audio)
#             speak.Speak('davinci thinks you said:' + text)
#             print("davinci thinks you said:" + text)
#             webbrowser.open_new(url2+text)
#         except sr.UnknownValueError:
#             print("sorry Coukdn't understand")
#         except sr.RequestError as e:
#             print("Failed to retrive results", e)