from operators import read_write
import numpy as np

data = read_write.my_open('../data/train/1/input.txt')
b = np.random.randint(1, 10)
a = [np.random.randint(1, 10), np.random.randint(1, 10),np.random.randint(1, 10)]
# read_write.my_save()