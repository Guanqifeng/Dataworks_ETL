import time
from progressbar import *

total = 1000
def dosomework():
    time.sleep(0.01)
if __name__ == '__main__':
    progress = ProgressBar()
    for i in progress(range(1000)):
        dosomework()
