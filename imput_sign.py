import cv2
import numpy as np
import os
"""
# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/A")
    os.makedirs("data/train/B")
    os.makedirs("data/train/P")
    os.makedirs("data/train/I")
    os.makedirs("data/train/H")
    os.makedirs("data/test/0")
    os.makedirs("data/test/A")
    os.makedirs("data/test/B")
    os.makedirs("data/test/P")
    os.makedirs("data/test/I")
    os.makedirs("data/test/H")
"""
# Train or test
mode = 'train'
directory = 'data/' + mode + '/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    # Getting count of existing images
    count = {'zero': len(os.listdir(directory + "/0")),
             'A': len(os.listdir(directory + "/A")),
             'B': len(os.listdir(directory + "/B")),
             'P': len(os.listdir(directory + "/P")),
             'I': len(os.listdir(directory + "/I")),
             'H': len(os.listdir(directory + "/H"))}


    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ZERO : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "A : " + str(count['A']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "B : " + str(count['B']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "P : " + str(count['P']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "I : " + str(count['I']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "H : " + str(count['H']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    cv2.imshow("Frame", frame)

    # _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(mask, kernel, iterations=1)
    # img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(count['zero']) + '.jpg', roi)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory + 'A/' + str(count['A']) + '.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory + 'B/' + str(count['B']) + '.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory + 'I/' + str(count['I']) + '.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory + 'P/' + str(count['P']) + '.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory + 'H/' + str(count['H']) + '.jpg', roi)

cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""