from GA import min_fun
import numpy as np


class Config:
    """
    默认全局配置

    encoding    # encoding of the problem
    evaluated   # number of evaluated individuals
    evaluation  # maximum number of evaluations
    gen         # current generation
    maxgen      # maximum generation
    run         # run number
    runtime     # runtime
    save        # number of saved populations
    result      # set of saved populations
    PF          # true Pareto front
    parameter   # parameters of functions specified by users
    outputFcn   # function invoked after each generation
    """
    population_num = 100 # 种群大小
    objectives_num = 1 # 目标数量
    dec_num = 4 # 决策变量数量
    lower = np.zeros(dec_num) # 下界
    upper = np.ones(dec_num) # 上界
    evaluation = 20 # 进化代数
    algorithm = []
    problem = min_fun.min_fun # 适应度
    encoding = "real" # 编码方式，实数编码
    # evaluated
    # gen
    # maxgen
    # run
    # runtime
    # save
    # result
    # PF
    # parameter
    # outputFcn


def set_lower_upper(lower, upper):
    Config.lower = lower
    Config.upper = upper


def get_dec_num():
    return Config.dec_num


def get_population_num():
    return Config.population_num


def get_objectives_num():
    return Config.objectives_num


def get_lower():
    return Config.lower


def get_upper():
    return Config.upper


def set_problem(p):
    Config.problem = p


def get_problem(a):
    return Config.problem(a)


def get_evaluation():
    return Config.evaluation


def get_encoding():
    return Config.encoding

