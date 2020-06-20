import cv2
import numpy as np

print("Initializing Camera ...")
cap = cv2.VideoCapture(0)
print("Camera Window Loaded!")

font = cv2.FONT_HERSHEY_SIMPLEX
default_msg = 0

while cap.isOpened():
    ret, frame = cap.read()

    # define region of interest
    roi = frame[100:450, 100:450]
    rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    cv2.rectangle(frame, (100, 100), (450, 450), (0, 255, 0), 2)

    if default_msg == 0:
        cv2.putText(
            frame,
            "Put your hand in the box",
            (50, 50),
            font,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )
    else:
        cv2.putText(frame, "OK", (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"):
        break
    elif k & 0xFF == ord("s"):
        default_msg = 1

cap.release()
cv2.destroyAllWindows()
