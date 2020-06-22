import time

class Timer:

    def __init__(self):
        """A timer that can be used to measure elapsed time, manage time steps
        in loops, control execution times, etc.
        The constructor, starts the timer at instantiation."""
        self.paused = False
        self.pauseInitTime = None
        self.pauseElapsed = 0
        self.initTime = time.time()

    def getElapsed(self):
        """Returns the time elapsed since instantiation or last reset minus sum
        of paused time."""
        if self.paused:
            return self.pauseInitTime - self.initTime - self.pauseElapsed
        else:
            return time.time() - self.initTime - self.pauseElapsed

    def isWithin(self, delay):
        """Returns True if elapsed time is within (less than) delay argument.
        This method is useful to control execution of while loops for a fixed
        time duration."""
        if self.getElapsed() < delay:
            return True
        else:
            return False

    def pause(self):
        """Pauses the timer."""
        self.pauseInitTime = time.time()
        self.paused = True

    def reset(self):
        """Resets the timer initial time to current time."""
        self.paused = False
        self.pauseInitTime = None
        self.pauseElapsed = 0
        self.initTime = time.time()

    def resume(self):
        """Resumes the timer following call to .pause() method."""
        if self.paused:
            self.pauseElapsed += time.time() - self.pauseInitTime
            self.paused = False
        else:
            print("Warning: Timer.resume() called without prior call to Timer.pause()")

    def sleepToElapsed(self, delay, reset = True):
        """Sleeps until elapsed time reaches delay argument. If reset argument
        is set to True (default), the timer will also be reset. This method is
        useful to control fixed time steps in loops."""
        if self.getElapsed() < delay:
            time.sleep(delay - self.getElapsed())
        if reset:
            self.reset()