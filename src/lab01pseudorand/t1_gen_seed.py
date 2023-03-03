from random import randint, seed
from time import time

seed(int(time()))

KEYSIZE = 16
NUM_OF_KEYS = 10

keys = []
for _ in range(NUM_OF_KEYS):
    key = []
    for _ in range(16):
        i = randint(0, 255)
        key.append(f'{i:0{2}X}')
    keys.append(''.join(key))
print('\n'.join(keys))
