import cv2
import os
import pickle

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackgroud = cv2.imread('Resources/background.png')

# Mode Images into List
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
    # print(len(imgModeList))

# Load the Encodeing file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)

print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img(0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    imgBackgroud[162:162 + 480, 55:55 + 640] = img
    imgBackgroud[44:44 + 633, 808:808 + 414] = imgModeList[1]

    # cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendence", imgBackgroud)
    cv2.waitKey(1)
