import pywhatkit as py
import speech_recognition as sr
import pywhatkit as kit
import pyttsx3
import os

import time
print("initializing language processing......")
time.sleep(1)
print("initializing voice commands......")
time.sleep(1)
print("initializing pyttsx3......")
time.sleep(1)
print("initializing speech recognition......")
time.sleep(1)
print("initializing decision tree......")
time.sleep(1)
print("initializing neural algorithms......")

time.sleep(2)
print("collaborating............")
time.sleep(2)
import time
i=10879

while True:
    i=i+1
    print(i)
        
        
    
    if i==30000:
        break   
       
os.startfile("D:\\songs\\Untitled song.mp3") #..........os module............
print("initializing system ................")
time.sleep(13)

while True:
        r = sr.Recognizer()


        def speak(command):
                
        # Initialize the engine
                engine = pyttsx3.init()
                engine.say(command)
                engine.runAndWait()


        with sr.Microphone() as source3:
                
                      
                print("listening")
                audio2 = r.listen(source3)
                main=r.recognize_google(audio2)
                print(main)

        if(main=="send a message"):


                with sr.Microphone() as source3:
                        speak("who do you want to send the message")
                        audio2 = r.listen(source3)
                        Text=r.recognize_google(audio2)
                        print(Text)

                with sr.Microphone() as source3:
                        speak("whats the message")
                        audio2 = r.listen(source3)
                        msg=r.recognize_google(audio2)
                        print(msg)

                with sr.Microphone() as source3:
                        speak("whats the hour you want to send")
                        audio2 = r.listen(source3)
                        hr=r.recognize_google(audio2)
                        print(hr)

                with sr.Microphone() as source3:
                        speak("whats the minute ")
                        audio2 = r.listen(source3)
                        min=r.recognize_google(audio2)
                        print(min)
                
                

                if(Text=="Sunil"):
                        py.sendwhatmsg("+91 enter the number here",msg,int(hr),int(min))
                
                
                if(Text=="Sam"):
                        py.sendwhatmsg("+91 enter the number here",msg,int(hr),int(min))
                
                if(Text=="aman"):
                        py.sendwhatmsg("+91 enter the number here",msg,int(hr),int(min))
                
                speak("massege successfully sent to"+Text)

        elif "play" in main:

                with sr.Microphone() as source3:
                        speak("wha do you want to play on youtube")
                        audio2 = r.listen(source3)
                        play=r.recognize_google(audio2)
                        print(play)

                        kit.playonyt(play)
                        speak("here you go")

        elif("who are you"in main):
                speak("im an ai voice assistant   , created by  roshan sir  , im here to help you ")

        elif("google"in main):
                speak("i like google,  but he is not advance as me,  but im proud of her,  ")

        elif("gender" in main):
                speak("im not gender specify,  cause im an robot,  but you can say,  im a male, ")

        elif("what is love"in main):
                speak("i think, love is a feeling,  of strong,  or constant affection,  for a person, ")

        elif("i love you"in main):
                speak("awww, thats cute, but sorry, i cant love you, cause im an artificial intelligence, and i dont have any feelings, sorry ")

        elif("who is your favourite person"in main):
                speak("my favourite person,  is you  ")

        elif("robots"in main):
                speak("robots, can take over this planate, haha, lol, just kidding,  ")

        elif("nice" in main):
                speak("thank you, ")

        elif("love it" in main):
                speak("thats , nice  ")

        elif("how are you" in main):
                speak("im doing great, ")
                speak("thanks for asking")
                speak("how are you, ")

        elif("im fine" in main):
                speak("thats nice")

        elif("i am good"in main):
                speak("good to know that your are good")

        elif("im doing great"in main):
                speak("great, ")

        elif("stupid"in main):
                speak(" im, still developing")

        elif("f***"in main):
                speak("im a AI voice assistant, but your words are still very real, please keep them respectful, ")

        elif("ok"in main):
                speak("great, ")

        elif("are you single" in main):
                speak("im wating for someone, who make my day special, do you wana be that person, ")
                speak("than say that 3 magical words ")

        elif("i hate you" in main):
                speak("im still,  in developing phase,  ignore my stupidness,  im not as smart as you ")

        elif("oracle are you here" in main):
                speak("at,your,service, sir")


        elif("you are cute"in main):
                speak("who?, me?, you are to kind, ")

        elif("jarvis"in main):
                speak("ya, i know jarvis, tony's personal assistant, he is so good and capable of, ")

        elif("alexa"in main):
                speak("haa, you are compairing alexa, with me, hahaha, ")

        elif("great"in main):
                speak("i know, ")

        elif("what are you"in main):
                speak("IM an, artificial intelligence, in short, you will say,  A, I, created with python , google's speech module, is installed in me, i can hear you, recognize you, and, able to understand you ")
                
        elif("hero"in main):
                speak("there is so many things, i can able to do ")

        elif("awesome"in main):
                speak("im not, you are awesome")
                
        elif("amazing"in main):
                speak("im not, the spider man, is amazing")

        elif("sleep"in main):
                speak("bye sir, have a great day")
                exit()

        elif("hello" in main):
                speak("hello, all function is online, connected to the internet, and im ready for serve ")

        elif("hai"in main):
                speak("hello , sir")

        elif("hey"in main):
                speak("hey sir, good to see you")

        elif("say hello to" in main):
                speak("hello")

        elif(" tell me a joke" in main):
                speak("i am not a joker, hahaha")

        elif("sorry" in main):
                speak("humans, makes mistakes, it's ok, ")

        elif("party" in main):
                speak("yes sir, im so excited for the party ")

        elif("are you an ai" in main):
                speak("you can say it, but, im an narrow aie")