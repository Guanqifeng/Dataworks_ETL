import bisect
import random

if __name__ == '__main__':
    SIZE = 7

    my_list = []

    for i in range(SIZE):
        needle = random.randrange(SIZE * 2)
        bisect.insort(my_list, needle)
        print("%2d -> " % needle, str(my_list))