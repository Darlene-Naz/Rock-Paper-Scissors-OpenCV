import utils
import pygame
import cv2
import random
import numpy as np
from components import RockPaperScissor, Camera
from tensorflow.keras.models import load_model


def rpsGame(totalScore=3):
    # --- Init
    camera = Camera()
    rps = RockPaperScissor(totalScore)
    rps.setCImg(1)

    model = load_model("models/inception_model.h5")

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
            c_num = random.randint(0, 2)
            rps.setCImg(c_num)

            # model predicts
            x = camera.save_current_frame(frame_roi)
            y = model.predict(x)
            print("[MODEL] Max Probability: " + str(np.max(y)))
            p_num = np.argmax(y, axis=1)[0]
            print("[GAME] Player: " + utils.gestureText[int(np.argmax(y, axis=1))])
            print("[GAME] Computer: {}".format(utils.gestureText[c_num]))
            rps.decideWinner(c_num, p_num)

            rps.stopTimer()

        # --- Drawing background code
        rps.draw_ui()

        # --- updating Timer
        rps.updateTimer()

    rps.quit()
    camera.quit()


if __name__ == "__main__":
    print("[INFO] To get started, press 'SPACE' after adjusting hand in the box")
    rpsGame(totalScore=3)
