## for daly dataset
import pickle

## for opencv-python
import numpy as np
import cv2

## sample video
video_id = "jnXjdVA91kY.mp4"
video_name = "D:/workspace-dataset/DALY/download_videos/videos/Becoming Miranda Sings!-jnXjdVA91kY.mp4"

## open daly dataset from the pickle file
with open("D:\workspace-dataset\DALY\daly1.1.0.pkl", "rb") as f:
    daly = pickle.load(f, encoding='latin1')

## play sample video
cap = cv2.VideoCapture(video_name)

fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

action = daly['annot'][video_id]['annot']['ApplyingMakeUpOnLips']

action_frame_list = []
for i in range(0, len(action)):
    print(int(action[i]['beginTime'] * fps))
    print(int(action[i]['endTime'] * fps))
    action_frame_list.append([int(action[i]['beginTime'] * fps), int(action[i]['endTime'] * fps)])
print(action_frame_list)

start_frame = 2500
cap.set(1, start_frame);

frame_number = start_frame

i = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    frame_number = frame_number + 1
    print(frame_number)

    ret, frame = cap.read()

    if frame_number >= action_frame_list[i][0] and frame_number <= action_frame_list[i][1]:
        print('YEAH!')
        xmin = action[i]['keyframes'][0]['boundingBox'][0][0]
        ymin = action[i]['keyframes'][0]['boundingBox'][0][1]
        xmax = action[i]['keyframes'][0]['boundingBox'][0][2]
        ymax = action[i]['keyframes'][0]['boundingBox'][0][3]
        frame = cv2.rectangle(frame, (int(width * xmin), int(height * ymin)), (int(width * xmax), int(height * ymax)), (255,0,0), 5)
        cv2.putText(frame, 'ApplyingMakeUpOnLips', (int(width * xmin) + 10, int(height * ymin) + 30), font, 1, (255,0,0), 3, cv2.LINE_AA)

    elif frame_number == action_frame_list[i][1] + 1:
        i = i + 1
        if i == len(action):
            i = 0


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
