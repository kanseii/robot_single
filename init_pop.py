import pickle
import numpy as np

std = 1
pop_size = 100
gene_size = 102       # DNA length
population = std*np.random.randn(pop_size,gene_size)
filename = "init_population"
with open(filename + ".pkl", 'wb') as file:
    pickle.dump(population, file)
