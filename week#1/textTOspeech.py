import gtts
import playsound

text=input("enter your text here")
sound=gtts.gTTS(text, lang="en")
sound.save("MyIntro.mp3")
playsound.playsound("MyIntro.mp3")
