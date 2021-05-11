import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from gtts import gTTS
import playsound
import time
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
files = open("labels.txt","r")
labels = (files.read().replace("\n","").split(","))


def say(text):
	tts = gTTS(text=text,lang='th')
	tts.save('sound.mp3')
	playsound.playsound('sound.mp3', True)


txt_predict =""
while True:
    time.sleep(2)
    try:
        image = Image.open('pathreal.png')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        print(txt_predict != prediction,txt_predict,prediction)
        if(txt_predict != labels[np.argmax(prediction)] and txt_predict != ""):
            print(txt_predict)
        txt_predict = labels[np.argmax(prediction)]
        say(txt_predict)
    except:
        pass
    