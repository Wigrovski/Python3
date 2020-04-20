import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 160)
infile = "text.txt"
f = open(infile, 'r')
theText = f.read()
f.close()
engine.save_to_file(theText,' text.mp3')
engine.runAndWait()
