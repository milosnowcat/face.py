import cv2
import os

def extractFaces(path):
    imagesPath = f"{path}/images"

    if not os.path.exists(f"{path}/faces"):
        os.makedirs(f"{path}/faces")
        print("New folder: assets/faces")

    faceClassif = cv2.CascadeClassifier("assets/data/haarcascades/haarcascade_frontalface_default.xml")

    count = 0
    for imageName in os.listdir(imagesPath):
        print(imageName)
        image = cv2.imread(imagesPath + "/" + imageName)
        faces = faceClassif.detectMultiScale(image, 1.02, 5)
        for (x, y, w ,h) in faces:
            face = image[y:y + h, x:x + w]
            face = cv2.resize(face, (150, 150))
            print(count)
            cv2.imwrite(path + "/faces/" + str(count) + ".jpg", face)
            count += 1

    cv2.destroyAllWindows()
