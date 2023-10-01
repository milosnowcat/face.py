import cv2
import os
import face_recognition

PATH = "assets"
FACE_CLASSIF = cv2.CascadeClassifier("assets/data/haarcascades/haarcascade_frontalface_default.xml")

def extractFaces():
    imagesPath = f"{PATH}/images"

    if not os.path.exists(f"{PATH}/faces"):
        os.makedirs(f"{PATH}/faces")
        print("New folder: assets/faces")

    count = 0
    for imageName in os.listdir(imagesPath):
        print(imageName)
        image = cv2.imread(imagesPath + "/" + imageName)
        faces = FACE_CLASSIF.detectMultiScale(image, 1.02, 5)
        for (x, y, w ,h) in faces:
            face = image[y:y + h, x:x + w]
            face = cv2.resize(face, (150, 150))
            print(count)
            cv2.imwrite(PATH + "/faces/" + str(count) + ".jpg", face)
            count += 1
        os.remove(imagesPath + "/" + imageName)

def faceRecognition():
    imageFacesPath = f"{PATH}/faces"

    facesEncodings = []
    facesNames = []
    for file_name in os.listdir(imageFacesPath):
        image = cv2.imread(imageFacesPath + "/" + file_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
        facesEncodings.append(f_coding)
        facesNames.append(file_name.split(".")[0])
    
    return (facesEncodings, facesNames)
