import numpy as np
import Config


def pareto(p_1, p_2):
    """
    :param p_1: 个体1的目标值序列
    :param p_2: 个体2的目标值序列
    :return: p_1支配p_2返回true，否则返回false
    """
    tem1 = tem2 = 0
    for i, j in zip(p_1.get_obj(), p_2.get_obj()):
        if i < j:
            tem1 += 1
        if i > j:
            tem2 += 1
    return tem1 > 0 and tem2 == 0


def non_dominated_sort(Pop):
    P = []
    P1 = []
    # from pyeas.individual import Individual
    # assert isinstance(Pop[0], Individual)
    for p in Pop:
        p.pareto_init()

    for p in Pop:
        for q in Pop:
            if pareto(p, q):
                p.set_p_pareto(q)
            elif pareto(q, p):
                p.set_pareto_p(1)
        if p.get_pareto_p() == 0:
            P1.append(p)

    P.append(P1)

    index = 0
    while len(P[index]) != 0:
        H = []
        for p in P[index]:
            for q in p.get_p_pareto():
                q.set_pareto_p(-1)
                if q.get_pareto_p() == 0:
                    H.append(q)
        # end of p
        index += 1
        P.append(H)

    return P[:-1]


def crowding_distance_assiginment(Pop):
    """
    :param Pop: a list of [p1, p2, p3]
    :return:
    """
    N = len(Pop)
    dec_array = []
    for p in Pop:
        dec_array.append(p.get_obj())
    dec_array = np.array(dec_array)

    index = np.argsort(dec_array, axis=0)

    CrowdDis = np.zeros(N)
    CrowdDis[index[0, ...]] = float('inf')

    for f in range(Config.get_objectives_num()):
        for j in range(1, N - 1):
            CrowdDis[index[j][f]] = CrowdDis[index[j][f]] + \
                                    (Pop[index[j + 1][f]].get_obj()[f] - Pop[index[j - 1][f]].get_obj()[f]) / \
                                    (Pop[index[-1][f]].get_obj()[f] - Pop[index[0][f]].get_obj()[f])

    return np.argsort(CrowdDis)

