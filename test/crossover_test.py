from individual import Individual
from GA import crossover
import numpy as np
import Config

Config.set_lower_upper( np.array([50, 1, 50]), np.array([200, 50, 200]) )
a = Individual.init_individual()

out = crossover.cross(a)
