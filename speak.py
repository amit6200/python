from text_to_speech import speak
s=input("Enter anything to speak ")
speak(s,"en",save=True,file="speak.mp3",speak =True)