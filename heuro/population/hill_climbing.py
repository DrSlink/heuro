import random


class SimpleHC:
    def __init__(self, seed=None):
        self.random = random.Random(seed)

    def mutate(self, vector, constr):
        new_vec = []
        mutation_prob = 1 / len(vector)
        for i in range(len(vector)):
            if self.random.random() < mutation_prob:
                new_vec.append(self.random.triangular(constr[i][0], constr[i][1], vector[i]))
            else:
                new_vec.append(vector[i])
        return new_vec

    def fit(self, func, constr, steps_without_improve=100):
        best_vec = []
        for con in constr:
            best_vec.append(self.random.uniform(con[0], con[1]))
        best_val = func(best_vec)
        made_steps = 0
        while made_steps != steps_without_improve:
            current_vec = self.mutate(best_vec, constr)
            current_val = func(current_vec)
            made_steps += 1
            if current_val < best_val:
                best_val = current_val
                best_vec = current_vec
                made_steps = 0
        return best_vec, best_val


class ShotgunHC:
    def __init__(self, seed=None):
        self.simple_hc = SimpleHC(seed=seed)

    def fit(self, *args, restarts_without_improve=100, **kwargs):
        best_vec, best_val = self.simple_hc.fit(*args, **kwargs)
        made_steps = 0
        while made_steps != restarts_without_improve:
            current_vec, current_val = self.simple_hc.fit(*args, **kwargs)
            made_steps += 1
            if current_val < best_val:
                best_val = current_val
                best_vec = current_vec
                made_steps = 0
        return best_vec, best_val
