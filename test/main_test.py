import numpy as np
import Config
import individual


# 初始化群体
Pop = []
for i in range(99):
    ind = individual.Individual(np.random.rand(Config.get_dec_num()))
    Pop.append(ind)
