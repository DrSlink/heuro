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


class Genetic:
    def __init__(self, seed=None):
        self.random = random.Random(seed)

    def fit(self, func, constr, population_size=10,
            steps_without_improve=10):
        population = []
        for _ in range(population_size):
            population.append(Individual(self.random, func, constr))
        made_steps = 0
        population.sort(key=lambda x: x.fitness)
        best_ind = population[0]
        yield (best_ind.vec, best_ind.fitness,
               best_ind.vec, best_ind.fitness, True)
        for ind in population:
            yield best_ind.vec, best_ind.fitness, \
                  ind.vec, ind.fitness, False
        while made_steps != steps_without_improve:
            sum_fit = sum(ind.fitness for ind in population) + 0.01

            for ind in population:
                ind.pair_prob = 1 - ind.fitness / sum_fit
            new_generation = []
            for i in range(population_size):
                # choices creates parthenogenesis some time))
                probs = [ind.pair_prob for ind in population]
                pair = self.random.choices(population, probs, k=2)
                child = pair[0].mate(pair[1], func)
                child.mutate(func, constr)
                new_generation.append(child)
            population += new_generation
            population.sort(key=lambda ind: ind.fitness)
            population = population[:population_size]
            made_steps += 1
            current_best = population[0]
            is_better = current_best.fitness < best_ind.fitness
            yield (best_ind.vec, best_ind.fitness,
                   current_best.vec, current_best.fitness, is_better)
            for ind in population:
                yield (best_ind.vec, best_ind.fitness,
                       ind.vec, ind.fitness, False)
            if is_better:
                best_ind = current_best
                made_steps = 0
        return best_ind.vec, best_ind.fitness
