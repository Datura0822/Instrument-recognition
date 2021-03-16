import math
import numpy as np
import time
import Config
import  individual
"""
    Module function：SBX simulated binary crossover
    Currently only contains sbx algorithm
"""


def cross(parents, crossover_p=1, crossover_d=20, mutation_p=1, mutation_d=20, encode="real"):
    """
    :param parents: 父代种群
    :param crossover_p: is the probabilities of doing crossover
    :param crossover_d: is the distribution index of simulated binary crossover
    :param mutation_p: is the expectation of number of bits doing mutation
    :param mutation_d: is the distribution index of polynomial mutation
    :param encode: Population gene sequence coding coding method
    :return: 生成的子代种群
    """

    dec_array = []
    for p in parents:
        dec_array.append(p.get_dec())
    dec_array = np.array(dec_array).reshape(Config.get_population_num(), Config.get_dec_num())

    if len(dec_array) % 2 != 0:
        dec_array = np.delete(dec_array, -1, 0)
    parent1, parent2 = np.array_split(dec_array, 2, 0)
    p_num, d_num = parent1.shape


    # if encode == "integer":
    #
    #     for i in range(p_num):
    #         index = np.random.randint(0, Config.get_dec_num())
    #         tmp = parent1[i][index]
    #         parent1[i][index] = parent2[i][index]
    #         parent2[i][index] = tmp
    #
    #     for i in range(p_num):
    #         if(np.random.rand(1)<0.2):
    #             index = np.random.randint(0, Config.get_dec_num() )
    #             parent1[i][index] = np.random.randint(Config.get_lower()[index], Config.get_upper()[index] + 1)
    #             parent1[i][index] = np.random.randint(Config.get_lower()[index], Config.get_upper()[index] + 1)
    #
    #     offs = []
    #     for i in range(p_num):
    #         offs.append(individual.Individual(parent1[i]))
    #         offs.append(individual.Individual(parent2[i]))
    #     return offs


    if encode == "real":
        # Simulated binary crossover

        beta = np.zeros((p_num, d_num))
        mu = np.random.rand(p_num, d_num)
        beta[mu <= 0.5] = (2 * mu[mu <= 0.5]) ** (1 / (crossover_d + 1))
        beta[mu > 0.5] = (2 - 2 * mu[mu > 0.5]) ** (-1 / (crossover_d + 1))

        # 交换个体某一个维度的值，增加个体多样性
        np.random.seed(int(time.time()))
        beta = beta * (-1) ** np.random.randint(0, 2, size=(p_num, d_num))

        # 根据交叉概率判断是否进行交叉
        beta[np.random.rand(p_num, d_num) > crossover_p] = 1

        offspring = np.vstack(
            (
                (parent1 + parent2) / 2 + beta * (parent1 - parent2) / 2,
                (parent1 + parent2) / 2 - beta * (parent1 - parent2) / 2
            )
        )

        # Polynomial mutation
        lower = np.tile(Config.get_lower(), (2 * p_num, 1))
        upper = np.tile(Config.get_upper(), (2 * p_num, 1))
        site = np.random.rand(2 * p_num, d_num) < mutation_p / d_num
        mu = np.random.rand(2 * p_num, d_num)
        offspring = np.minimum(np.maximum(offspring, lower), upper)

        temp = site & (mu <= 0.5)
        offspring[temp] = offspring[temp] + (upper[temp] - lower[temp]) * \
                          ((2 * mu[temp] + (1 - 2 * mu[temp]) * (
                                      1 - (offspring[temp] - lower[temp]) / (upper[temp] - lower[temp])) ** (
                                        mutation_d + 1)) ** (1 / (mutation_d + 1)) - 1)

        temp = site & (mu > 0.5)
        offspring[temp] = offspring[temp] + (upper[temp] - lower[temp]) * \
                          (1 - (2 * (1 - mu[temp]) + 2 * (mu[temp] - 0.5) * (
                                  1 - (upper[temp] - offspring[temp]) / (upper[temp] - lower[temp])) ** (
                                        mutation_d + 1)) ** (1 / (mutation_d + 1)))

    offs = []
    offspring = offspring + 1
    for i in offspring.astype(int):
        offs.append(individual.Individual(i))
    return offs

