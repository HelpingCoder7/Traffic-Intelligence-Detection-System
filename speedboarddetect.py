import cv2
import numpy as np
from tensorflow.keras.models import load_model
from pytess import speak_speed
import pyttsx3

def conv_gray(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

def equakize(img):
    img_eq = cv2.equalizeHist(img)
    return img_eq

def preprocessing(img):
    img_gray = conv_gray(img)
    img_eq = equakize(img_gray)
    img_eq = img_eq / 255.0
    return img_eq

cap = cv2.VideoCapture(0)

# address = 'http://172.20.22.165:8080/video'
# cap.open(address)

if not cap.isOpened():
    print("Could not open camera")
    exit()
    
while True:
    
    success,img = cap.read()

    if not success:
        print("Something went wrong")
        
    capture_image = np.asarray(img)


    preprocess_img = preprocessing(capture_image)

    preprocess_img = cv2.resize(preprocess_img,(32,32))

    # h,w=preprocess_img.shape

    # print(h,w)
    # print(preprocess_img.shape)
    preprocess_img=preprocess_img.reshape(1,32,32,1)
    # print(preprocess_img.shape)


    model = load_model('speedboard30.keras')

    prediction = model.predict_step(preprocess_img)

    predicted_value = np.argmax(prediction)
    print(predicted_value)
    
    print('Predicted value is : ',predicted_value)
    
    if predicted_value in range(0,9):
        print('value is ',predicted_value)
        speak_speed(img)
        

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
