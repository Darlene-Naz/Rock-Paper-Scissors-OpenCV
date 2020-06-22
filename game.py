import utils
import pygame
import cv2
import random
import numpy as np
import keras as k
import keras.backend as K
import tensorflow as tf
from components import RockPaperScissor, Camera
from tensorflow.keras.models import load_model

# --- Init
camera = Camera()
rps = RockPaperScissor()
rps.setCImg(1)

model = load_model("models/final_custom_model6.h5")

while rps.carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rps.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rps.startTimer(3)

    # --- opencv pImg
    frame_roi = camera.get_frame()
    rps.setPImg(frame_roi)

    if rps.duration == 0 and rps.timer_started:

        # --- cImg
        num = random.randint(0, 2)
        rps.setCImg(num)

        # testing only
        x = camera.save_current_frame(frame_roi)
        y = model.predict(x)
        print(np.max(y))
        print(np.argmax(y, axis=1))
        print(utils.gestureText[int(np.argmax(y, axis=1))])

        rps.stopTimer()

    # --- Drawing background code
    rps.draw_ui()

    # --- updating Timer
    rps.updateTimer()

rps.quit()
camera.quit()
