import unittest
from heuro.landscapes.so import rastrigin
from heuro.landscapes.so import rosenbrock
from heuro.landscapes.so import sphere
from heuro.population.hill_climbing import SimpleHC
from heuro.population.hill_climbing import ShotgunHC
from heuro.population.evolution import Genetic


class TestLandscapes(unittest.TestCase):

    def test_rastrigin_min(self):
        for i in range(1, 5):
            self.assertEqual(rastrigin([0] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')

    def test_rosenbrock_min(self):
        for i in range(1, 5):
            self.assertEqual(rosenbrock([1] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')

    def test_sphere_min(self):
        for i in range(1, 5):
            self.assertEqual(sphere([0] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')


class TestPopulations(unittest.TestCase):

    def test_simple_hc(self):
        shc = SimpleHC(seed=42)
        gen = shc.fit(sphere, [(-5., 5.), (-5., 5.)])
        conv = False
        _ = next(gen)
        for i in range(100):
            res = next(gen)
            if res[4]:
                conv = True
                break
        self.assertTrue(conv,
                        'simple hill climbing algorithm do not converge')

    def test_shotgun_hc(self):
        shc = ShotgunHC(seed=42)
        gen = shc.fit(sphere, [(-5., 5.), (-5., 5.)])
        conv = False
        _ = next(gen)
        for i in range(100):
            res = next(gen)
            if res[4]:
                conv = True
                break
        self.assertTrue(conv,
                        'shotgun hill climbing algorithm do not converge')

    def test_evolution_genetic(self):
        shc = Genetic(seed=42)
        gen = shc.fit(sphere, [(-5., 5.), (-5., 5.)])
        conv = False
        _ = next(gen)
        for i in range(100):
            res = next(gen)
            if res[4]:
                conv = True
                break
        self.assertTrue(conv, 'genetic algorithm do not converge')


if __name__ == '__main__':
    unittest.main()
