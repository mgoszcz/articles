import time

from lib.events import SAVE_NEEDED

MAX_WAIT_TIME = 10

class WaitMethods:

    def __init__(self):
        self.save = SAVE_NEEDED

    def wait_for_save_completed(self):
        wait_time = 0.0
        while self.save.is_set():
            wait_time += 0.5
            time.sleep(0.5)
            if wait_time > MAX_WAIT_TIME:
                raise TimeoutError('Save did not happen in 10 seconds')

    def wait_for_save_needed(self, timeout: float = 2.0):
        wait_time = 0.0
        while not self.save.is_set():
            wait_time += 0.5
            time.sleep(0.5)
            if wait_time > timeout:
                raise TimeoutError(f'Save needed not set in {timeout} seconds')
