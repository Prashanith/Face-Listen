import cv2
from tensorflow.keras.models import model_from_json
import numpy as np
from PIL import Image
import glob

class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Angry", "Disgust",
                    "Fear", "Happy",
                    "Neutral", "Sad",
                    "Surprise"]
    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()
    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

facec = cv2.CascadeClassifier('/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/expression_analyzer/static/haarcascade_frontalface_default.xml')
model = FacialExpressionModel('/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/expression_analyzer/static/model.json', '/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/expression_analyzer/static/model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX


def getExpression(path):
    if(path is None):
        path = '/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/expression_analyzer/cnn_model/04776483.jpg'
    fr = cv2.imread(path)
    gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray_fr, 1.3, 5)
    for (x, y, w, h) in faces:
        fc = gray_fr[y:y+h, x:x+w]
        roi = cv2.resize(fc, (48, 48))
        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        print("------------------------------------------")
        print(pred)
        print("------------------------------------------")
        cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
        cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
    return fr
    
# getExpression()
