import random


class SimpleHC:
    def __init__(self, seed=None):
        self.random = random.Random(seed)

    def mutate(self, vector, constr, annealing):
        new_vec = []
        for i in range(len(vector)):
            left = vector[i] + (constr[i][0] - vector[i]) * annealing
            right = vector[i] + (constr[i][1] - vector[i]) * annealing
            new_vec.append(self.random.triangular(left, right, vector[i]))
        return new_vec

    def fit(self, func, constr, steps_without_improve=10):
        best_vec = []
        for con in constr:
            best_vec.append(self.random.uniform(con[0], con[1]))
        best_val = func(best_vec)
        yield best_vec, best_val, best_vec, best_val, True
        made_steps = 0
        whole_steps = 1
        while made_steps != steps_without_improve:
            annealing = 1 - whole_steps / (whole_steps + steps_without_improve)
            current_vec = self.mutate(best_vec, constr, annealing)
            current_val = func(current_vec)
            made_steps += 1
            whole_steps += 1
            is_better = current_val < best_val
            yield best_vec, best_val, current_vec, current_val, is_better
            if is_better:
                best_val = current_val
                best_vec = current_vec
                made_steps = 0
        return best_vec, best_val


class ShotgunHC:
    def __init__(self, seed=None):
        self.simple_hc = SimpleHC(seed=seed)

    def fit(self, *args, restarts_without_improve=10, **kwargs):
        gen = self.simple_hc.fit(*args, **kwargs)
        best_vec, best_val = yield from gen
        made_steps = 0
        while made_steps != restarts_without_improve:
            gen = self.simple_hc.fit(*args, **kwargs)
            current_vec, current_val = yield from gen
            made_steps += 1
            if current_val < best_val:
                best_val = current_val
                best_vec = current_vec
                made_steps = 0
        return best_vec, best_val
