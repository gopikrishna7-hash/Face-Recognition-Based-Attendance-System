import os
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def train_model():
    faces = []
    labels = []

    path = "static/faces"

    for file in os.listdir(path):
        img = cv2.imread(f"{path}/{file}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (100, 100))

        faces.append(gray.flatten())

        name = file.split("_")[0]
        labels.append(name)
    if len(faces) == 0:
        print("No training data found!")
        return None
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(faces, labels)

    return model