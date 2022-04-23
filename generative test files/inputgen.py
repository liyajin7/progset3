from random import *
import random

if __name__ == "__main__":
    random.seed()

    for i in range(100):
        print(randint(1, 10**12))