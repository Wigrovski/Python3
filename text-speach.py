import os
from gtts import gTTS

import os
from gtts import gTTS

with open("text.txt") as file:
    t = gTTS(file.read(), "ru")
t.save("text.mp3")

os.system("text.mp3")
