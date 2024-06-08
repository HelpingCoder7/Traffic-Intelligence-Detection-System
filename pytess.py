import easyocr
from PIL import Image
import cv2
import pyttsx3

def speak_speed(img):
    reader = easyocr.Reader(['en'],gpu=True)

    texts = reader.readtext(img) 
    # print(len(text))
    
    
    if len(texts) > 0:
        
        enginee = pyttsx3.init()
        voices= enginee.getProperty('voices')
        enginee.setProperty('voice',voices[1].id)
        # print(text)
        for (bbox,text,other) in texts:
            what_to_say = f'The speed in this area is {text} kilo meter per hour'
            enginee.say(what_to_say)
            enginee.runAndWait()
            return text
    

# img = r"C:\Users\HP\Downloads\000_1_0002.png"

# points=speak_speed(img)
# print(points)

