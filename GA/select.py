import individual
from GA import crossover
import numpy as np
import Config


def select():

    a = []
    for i in range(0,Config.get_population_num()):
        tmp = [np.random.randint(50, 200), np.random.randint(1, 50),np.random.randint(50, 200)]
        a.append(individual.Individual(tmp))

    for i in range(0,5):
        b = crossover.cross(a)
        a = a + b
        a.sort(key = lambda ind: (ind.get_obj()[0], -ind.get_dec()[2]))
        # if i>5:
        #     a.sort(key = lambda ind:(ind.obj[0],ind.obj[1]))
        # else:
        #     a.sort(key=lambda ind: ind.obj[0])
        a = a[:Config.get_population_num()]
    return [a[0].get_dec(), a[0].get_obj()]

