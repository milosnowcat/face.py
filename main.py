#                      .                    .                           
#                 :-:--=:-:::.             :=-**##*=:                   
#                  :=----------.         .-%@@@@@@@@@%:                 
#                 :-------------:        :@@@@@@@@@@@@%.                
#                :-=-----------==:       +@@@@@@@@@@@@@#                
#              .------------=------.     =@@@@@@@@@@@@@#                
#               :=-=-------===-=--      .+%@@@@@@@@@@@#=                
#                --=--------==-=-.       -*%@@@@@@@@@*-.                
#                   ::----===+-             .#%@@@@*.                   
#                      -+++=: .               :+##+                     
#                     -+=====.              .=%@@%%%#=                  
#                  :-----------:.        :+#%%%@@@@@%@%+-               
#                -----------------      -%%%%%@@@%@@%%@%%*              
#               .-==----------==--:     #%%%@%@@@@@@@@@@%%.             
#               :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             
#               ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             
#              :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            
#                --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             
#                --=-----------*=---  :===#@@%%@@@%@%%%--=              
#                -==-----------++--=  ---:#@%@@@%%%@@@%--=              
#                -=------------=:--=. =-- %@%%%%%%@%%%@=-=              
#               .-+-------------.:---.--: %%%%%%%%@%%@@+==              
#               :-++*++++++*+***. --=+--  *###########**-=              
#               --*+++++++++*+++: :--*-: :------=------*-=              
#               =-*++++++++*+***- .--*-. :-------------+-=              
#              .--*+++=+*++*+***+ :==*=: -------=------===:             
#              :=+++++==+++*++**+ -*++=. -------+-------+=:             
#               -++++=+==**+++***  :-:   -------+-------+.              
#                -+++=++=****+**#        -------+=------=               
#                .++==*=---=*+**+        =------+*------=               
#                 ----=    :---=          ====-.::+====                 
#            :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      
#            .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  
#                :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  
#                  =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  
#                  ====   .:+===:   -==+= :===*+: -==== .--:.      ..   
#                  =--=     ----:         .----   :=---                 
#                  ----     :---:         .=---   .=---                 
#                  ----     :---:         .=---    =---                 
#                  ---:     :---:         .=---    +---                 
#                  +##%.    =*##-         -%%#:    %%%#                 
#                 :@@@@-    #@@@+         %@@@*   :@@@%:                
#                 .====.    -++=:         =+==-    --==.                

# @milosnowcat

import utils

def main():
    """
    The main function captures video from the webcam, detects faces, and compares them to known faces to
    recognize and label them.
    """
    cap = utils.cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = utils.cv2.flip(frame, 1)
        orig = frame.copy()
        faces = utils.FACE_CLASSIF.detectMultiScale(frame, 1.1, 5)

        for (x, y, w, h) in faces:
            face = orig[y:y + h, x:x + w]
            face = utils.cv2.cvtColor(face, utils.cv2.COLOR_BGR2RGB)
            actual_face_encoding = utils.face_recognition.face_encodings(face, known_face_locations=[(0, w, h, 0)])[0]
            result = utils.face_recognition.compare_faces(utils.faceRecognition()[0], actual_face_encoding)
            if True in result:
                index = result.index(True)
                name = utils.faceRecognition()[1][index]
                color = (125, 220, 0)
            else:
                name = "Desconocido"
                color = (50, 50, 255)

            utils.cv2.rectangle(frame, (x,y + h), (x + w, y + h + 30), color, -1)
            utils.cv2.rectangle(frame, (x,y), (x + w, y + h), color, 2)
            utils.cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, utils.cv2.LINE_AA)

        utils.cv2.imshow("Frame", frame)
        k = utils.cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    utils.cv2.destroyAllWindows()

utils.extractFaces()
main()
