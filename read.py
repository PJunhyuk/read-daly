## for daly dataset
import pickle

## for opencv-python
import numpy as np
import cv2

## for file list parsing
import glob

import argparse as ap

import random

video_name_list = glob.glob("D:/workspace-dataset/DALY/download_videos/videos/*.mp4")

parser = ap.ArgumentParser()
parser.add_argument('-n', "--videoNumber", help="Number of Video")
parser.add_argument('-r', "--randomVideo", help="Random Video")

args = vars(parser.parse_args())

if args["videoNumber"] is not None:
    video_number = int(args["videoNumber"])
else:
    video_number = 0

if args["randomVideo"] is not None:
    video_number = random.randrange(0, len(video_name_list))
else:
    video_number = 0

video_id_list = []

for i in range(0, len(video_name_list)):
    video_name_len = len(video_name_list[i])
    video_id_list.append(video_name_list[i][video_name_len-15:video_name_len])

## sample video
video_id = video_id_list[video_number]
video_name = video_name_list[video_number]

## open daly dataset from the pickle file
with open("D:\workspace-dataset\DALY\daly1.1.0.pkl", "rb") as f:
    daly = pickle.load(f, encoding='latin1')

## play sample video
cap = cv2.VideoCapture(video_name)

fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(daly['annot'][video_id]['annot'].keys())
action_list = list(daly['annot'][video_id]['annot'].keys())
print(action_list)
action = daly['annot'][video_id]['annot'][action_list[0]]

action_frame_list = []
for i in range(0, len(action)):
    print(int(action[i]['beginTime'] * fps))
    print(int(action[i]['endTime'] * fps))
    action_frame_list.append([int(action[i]['beginTime'] * fps), int(action[i]['endTime'] * fps)])
print(action_frame_list)

if action_frame_list[0][0] > 500:
    start_frame = action_frame_list[0][0] - 300
else:
    start_frame = 0

cap.set(1, start_frame);

frame_number = start_frame

font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    frame_number = frame_number + 1
    print(str(frame_number))

    ret, frame = cap.read()

    for j in range(0, len(action)):
        if frame_number >= action_frame_list[j][0] and frame_number <= action_frame_list[j][1]:
            print('YEAH!')
            xmin = action[j]['keyframes'][0]['boundingBox'][0][0]
            ymin = action[j]['keyframes'][0]['boundingBox'][0][1]
            xmax = action[j]['keyframes'][0]['boundingBox'][0][2]
            ymax = action[j]['keyframes'][0]['boundingBox'][0][3]
            frame = cv2.rectangle(frame, (int(width * xmin), int(height * ymin)), (int(width * xmax), int(height * ymax)), (255,0,0), 5)
            cv2.putText(frame, action_list[0], (int(width * xmin) + 10, int(height * ymin) + 30), font, 1, (255,0,0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
