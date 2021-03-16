import individual
from operators import dominated
from GA import crossover
import Config
import numpy as np
import matplotlib.pyplot as plt


def initpop():
    a = []
    for i in range(Config.get_population_num()):
        tmp = [np.random.randint(50, 200), np.random.randint(1, 50), np.random.randint(50, 200)]
        a.append(individual.Individual(tmp))
    return a




def draw_pareto(Pop):
    dec_array = []
    for p in Pop:
        dec_array.append(p.get_obj())
    dec_array = np.reshape(dec_array, newshape=(-1, 2))
    plt.scatter(dec_array[:, 0], dec_array[:, 1])
    plt.show()


if __name__ == '__main__':
    Pop = initpop()
    draw_pareto(Pop)

    for i in range(5):
        offspring = crossover.cross(Pop)

        Pop = Pop + offspring
        P_set = dominated.non_dominated_sort(Pop)

        select = []
        for k in P_set:
            for p in k:
                select.append(p)
                if len(select) == Config.get_population_num():
                    break
            if len(select) == Config.get_population_num():
                break
        Pop = select
        for j in range(10):
            print(Pop[j].get_dec(),Pop[j].get_obj())

        print ("*"*50)
        print("evaluation{0}".format(i))

        if (i % 100) == 0:
            draw_pareto(Pop)


