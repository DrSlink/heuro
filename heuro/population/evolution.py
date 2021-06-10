import random


class Individual:
    def __init__(self, random_gen, func, constr=None, vec=None):
        self.random = random_gen
        if vec:
            self.vec = vec
        else:
            self.vec = []
            for con in constr:
                self.vec.append(self.random.uniform(con[0], con[1]))
        self.fitness = func(self.vec)

    def mutate(self, func, constr):
        mutation_prob = 1 / len(self.vec)
        for i in range(len(self.vec)):
            if self.random.random() < mutation_prob:
                self.vec[i] = self.random.triangular(constr[i][0],
                                                     constr[i][1], self.vec[i])
        self.fitness = func(self.vec)

    def mate(self, pair, func):
        new_vec = []
        for i in range(len(self.vec)):
            # new_vec.append(self.random.choice([self.vec[i], pair.vec[i]]))
            new_vec.append((self.vec[i] + pair.vec[i]) / 2)
        child = Individual(self.random, func, vec=new_vec)
        return child
