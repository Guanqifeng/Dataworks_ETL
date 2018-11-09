#几秒器
import time


def calculateWatch():
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl - C to quit.')
    input()
    print("Start!")
    starttime  = time.time()
    lasttime = starttime
    lamp = 1
    try:
        while True:
            input()
            laptime = round(time.time() - lasttime,2)
            totalTime = round(time.time() - starttime,2)
            print('Lap #%s: %s (%s)' % (laptime, totalTime, lamp), end='')
            lamp += 1
            lasttime = time.time()
    except KeyboardInterrupt as e:
        print('\nDone!')

if __name__ == '__main__':
    calculateWatch()
