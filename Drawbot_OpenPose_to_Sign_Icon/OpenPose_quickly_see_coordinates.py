import json
import os

headTop = []
neck = []
pelvis = []
lefthand = []
righthand = []

#information about how to extract data from OpenPose: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md#keypoint-ordering
currentDataFile = json.loads(open(os.path.expanduser("~/Desktop/JSON input/train_00001/image_00001_keypoints.json"), "r").read())

headTop += [[currentDataFile["people"][0]["pose_keypoints_2d"][0], currentDataFile["people"][0]["pose_keypoints_2d"][1]]]
neck += [[currentDataFile["people"][0]["pose_keypoints_2d"][3], currentDataFile["people"][0]["pose_keypoints_2d"][4]]]
pelvis += [[currentDataFile["people"][0]["pose_keypoints_2d"][24], currentDataFile["people"][0]["pose_keypoints_2d"][25]]]

lefthand += [[currentDataFile["people"][0]["pose_keypoints_2d"][9], currentDataFile["people"][0]["pose_keypoints_2d"][10]]]
righthand += [[currentDataFile["people"][0]["pose_keypoints_2d"][21], currentDataFile["people"][0]["pose_keypoints_2d"][22]]]

#####Filter if zero!!!!!!!!!!!!!

print("headTop:", headTop)
print("neck:", neck)
print("pelvis:", pelvis)
print("lefthand:", lefthand)
print("righthand:", righthand)