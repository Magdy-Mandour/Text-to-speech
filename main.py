from gtts import gTTS
import os

myText = "let's try this goddamn simple easy project for the second time"

language = 'en'

result = gTTS(text=myText, lang=language, slow=False)

result.save('output.mp3')

os.system('start output.mp3')
