import cv2
import face_recognition
import  pickle
import  os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://markmyface-7b7a5-default-rtdb.firebaseio.com/",
    'storageBucket':"markmyface-7b7a5.appspot.com"
})



#student  images list ayt edkan
folderPath = "Images"
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentId = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentId.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)



    # print(path)
    #print(os.path.splitext(path)[0])
print(studentId)


# open cv use bgr and facereco use rgb so we have to convert
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("encoding started....")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentId]
print("encoding complete")

file = open("EncodeFIle.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("file saved")

