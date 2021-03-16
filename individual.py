import numpy as np
import Config


"""
定义个体属性
"""


class Individual:
    def __init__(self, dec):
        self.__dec = dec
        self.__obj = Config.get_problem(dec)

        self.__s = []
        self.__n = 0

    def set_dec(self, dec):
        self.__dec = dec
        self.__obj = Config.get_problem(dec)

    def get_dec(self):
        return self.__dec

    def get_obj(self):
        return self.__obj

    def pareto_init(self):
        self.__s = []
        self.__n = 0

    def get_p_pareto(self):
        return self.__s

    def set_p_pareto(self, q):
        self.__s.append(q)

    def get_pareto_p(self):
        return self.__n

    def set_pareto_p(self, q):
        self.__n += q

    @staticmethod
    def init_individual():
        # 初始化种群
        if Config.get_encoding() == "real":
            lower = Config.get_lower()
            upper = Config.get_upper()
            Pop = []
            for i in range(Config.get_population_num()):
                dec = np.random.rand(Config.get_dec_num()) * (upper - lower) + lower
                Pop.append(Individual(dec))
        if Config.get_encoding() == "binary":
            Pop = []
            for i in range(Config.get_population_num()):
                dec = np.random.randint(0, 2, Config.get_dec_num())
                Pop.append(Individual(dec))
        if Config.get_encoding() == "integer":
            lower = Config.get_lower()
            upper = Config.get_upper() + 1
            Pop = []
            for i in range(Config.get_population_num()):
                dec = np.random.rand(Config.get_dec_num()) * (upper - lower) + lower
                dec = dec.astype(int)
                Pop.append(Individual(dec))
        return Pop


