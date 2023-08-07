import datetime
import webbrowser
import speech_recognition as sr
import os
import win32com.client as wincom
import openai
import random
from config import apikey
speak = wincom.Dispatch("SAPI.SpVoice")

chatStr= ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr+=f"Nishant: {query}\n Jarvis: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside a try catch block
    speak.Speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"Openai/prompt- {random.randint(1,23434445)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
def ai(prompt):
    openai.api_key = apikey
    text  =f"OpenAI response for Prompt: {prompt} \n *******************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: Wrap this inside a try catch block
    print(response["choices"][0]["text"])
    text+= response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #with open(f"Openai/prompt- {random.randint(1,23434445)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)

def say(text):
    # os.system(f"say {text}")
    speak.Speak(text)


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    speak.Speak("Hello I am Jarvis A,I")
    while True:

        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["wikipedia","https://www.wikipedia.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(f"{site[1]}")
        if "open music" in query :
            musicPath = "C:\\Users\\NISHANT\\Downloads\\Pasoori.mp3"
            os.startfile(musicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak.Speak(strfTime)

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "Jarvis reset chat".lower() in query.lower():
            chatStr=""



        else :
            print("Chatting...")
            chat(query)


