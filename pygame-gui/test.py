import pygame as pg
import threading

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
font = pg.font.Font(None, 54)
font_color = pg.Color("springgreen")

duration = 0
timer_started = False
done = False


while not done:

    screen.fill((30, 30, 30))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    duration = 4

    if timer_started:
        pg.time.wait(1000)
        if duration > 0:
            duration = duration - 1

    text = font.render(str(duration), True, font_color)
    screen.blit(text, (50, 50))

    pg.display.flip()
    clock.tick(30)

pg.quit()


# import logging
# import threading
# import time


# def worker(arg):
#     while not arg["stop"]:
#         logging.debug("worker thread checking in")
#         time.sleep(1)


# def main():
#     logging.basicConfig(
#         level=logging.DEBUG, format="%(relativeCreated)6d %(threadName)s %(message)s"
#     )
#     info = {"stop": False}
#     thread = threading.Thread(target=worker, args=(info,))
#     thread_two = threading.Thread(target=worker, args=(info,))
#     thread.start()
#     thread_two.start()

#     while True:
#         try:
#             logging.debug("Checking in from main thread")
#             time.sleep(0.75)
#         except KeyboardInterrupt:
#             info["stop"] = True
#             logging.debug("Stopping")
#             break
#     thread.join()
#     thread_two.join()


# if __name__ == "__main__":
#     main()
