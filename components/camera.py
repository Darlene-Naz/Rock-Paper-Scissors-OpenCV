import cv2
import numpy as np


class Camera:
    def __init__(self):
        print("[System] Initializing Camera...")
        self.cap = cv2.VideoCapture(0)
        print("[System] Camera Window Loaded!")

    def get_frame(self):
        ret, frame = self.cap.read()
        frame = np.rot90(frame)
        # define region of interest
        roi = frame[0:280, 0:335]
        rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        return rgb_roi

    def save_current_frame(self, rgb_roi):
        bgr = cv2.cvtColor(rgb_roi, cv2.COLOR_RGB2BGR)
        x = cv2.resize(bgr, (100, 100))
        cv2.imwrite("components/img.jpg", x)
        print("[Debug] Image Saved!")
        x = x / 255
        img_arr = np.array(x)
        img = np.array([img_arr])
        return img

    def quit(self):
        self.cap.release()
        cv2.destroyAllWindows()

