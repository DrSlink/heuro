"""Unit tests for functions and algorithms."""
import unittest
from heuro.landscapes.so import rastrigin
from heuro.landscapes.so import rosenbrock
from heuro.landscapes.so import sphere
from heuro.population.hill_climbing import SimpleHC
from heuro.population.hill_climbing import ShotgunHC
from heuro.population.evolution import Genetic


class TestLandscapes(unittest.TestCase):
    """Tests for landscapes."""

    def test_rastrigin_min(self):
        """Test for Rastrigin function global minimum."""
        for i in range(1, 5):
            self.assertEqual(rastrigin([0] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')

    def test_rosenbrock_min(self):
        """Test for Rosenbrock function global minimum."""
        for i in range(1, 5):
            self.assertEqual(rosenbrock([1] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')

    def test_sphere_min(self):
        """Test for sphere function global minimum."""
        for i in range(1, 5):
            self.assertEqual(sphere([0] * i), 0,
                             f'incorrect value for min point with '
                             f'{i} dimentions')


class TestPopulations(unittest.TestCase):
    """Tests for population-based algorithms."""

    def test_simple_hc(self):
        """Test for simple hill climbing algorithm converging."""
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
        """Test for shotgun hill climbing algorithm converging."""
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
        """Test for genetic algorithm converging."""
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
