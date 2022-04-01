import face_recognition
import os

# Load the jpg files into numpy arrays
kpath = "B:\Code\Hackathon\HackOverflow\Intrusion Detection System\FaceRecognition\Known Images"
upath = r"B:\Code\Hackathon\HackOverflow\Intrusion Detection System\FaceRecognition\Unkown Images"
K_image_paths = [os.path.join(kpath,f) for f in os.listdir(kpath)]
U_image_path = [os.path.join(upath,f) for f in os.listdir(upath)]

K_encoded_face = []
unknown_face_encoding = []

known_faces = []

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
try:
    #for known faces 
    for ipath,jpath in zip(K_image_paths, U_image_path):
        Kimage = face_recognition.load_image_file(ipath)
        #since there is only one face in the unknown image we'll grab the index 0
        K_encoded_face = (face_recognition.face_encodings(Kimage)[0])
        known_faces.append(K_encoded_face)
    #for unkown faces
    for jpath in U_image_path:
        Uimage = face_recognition.load_image_file(jpath)
        for uface in face_recognition.face_encodings(Uimage):
            unknown_face_encoding.append(uface)
        
except IndexError:
    print("Face not recognized")
    quit()



# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
for buff in unknown_face_encoding:
    #compare the unkown faces with the known face
    results = face_recognition.compare_faces(known_faces, buff)
    #if the face is unkown then there wont be any True value in the list as all the known faces did not match this face
    if(True not in results):
        print("Unkown Face")

