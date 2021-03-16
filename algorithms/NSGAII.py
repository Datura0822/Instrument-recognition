from individual import Individual
from operators import dominated
from GA import crossover
import Config
import numpy as np
import matplotlib.pyplot as plt


def draw_pareto(Pop, name):
    dec_array = []
    for p in Pop:
        dec_array.append(p.get_obj())
    dec_array = np.reshape(dec_array, newshape=(-1, 2))
    plt.cla()
    plt.title('evaluation:{}'.format(name), fontsize=24)
    plt.scatter(dec_array[:, 0], dec_array[:, 1])
    plt.show()
    plt.pause(0.01)

# 设置可调整参数的范围
Config.set_lower_upper( np.array([50, 10, 50, -20]), np.array([150, 50, 150, -10]) )

# 初始化种群
Pop = Individual.init_individual()

# plt.ion()
# draw_pareto(Pop, 1)

error = [0.5, 0.5, 0.5]
param = []
for i in range(Config.get_evaluation()):
    # 交叉操作，生成子代
    offspring = crossover.cross(Pop)

    Pop = Pop + offspring
    # 非支配排序，获得子代
    P_set = dominated.non_dominated_sort(Pop)

    select = []
    for row in P_set:

        if len(select) == Config.get_population_num():
            break

        tem = len(select) + len(row)

        if tem > Config.get_population_num():
            need_p = Config.get_population_num() - len(select)
            index = dominated.crowding_distance_assiginment(row)
            for dis in range(len(index)-1, len(index)-need_p-1, -1):
                select.append(row[index[dis]])
        else:
            select = select + row

    Pop = select

    for j in range(10):
        # if(Pop[j].get_obj()[0] < error[0] and Pop[j].get_obj()[1] < error[1] and Pop[j].get_obj()[2] < error[2]):
        #     error = Pop[j].get_obj()
        #     param = Pop[j].get_dec()
        #     print(error)
        print(Pop[j].get_dec(), Pop[j].get_obj())


    # print ("*" * 50)

    # draw_pareto(Pop, i)

# print('param:',param)