"""Script for project run."""
from landscapes.so import rastrigin
from landscapes.so import rosenbrock
from landscapes.so import sphere
from population.hill_climbing import SimpleHC
from population.hill_climbing import ShotgunHC
from population.evolution import Genetic

from gui.vision import Vision

if __name__ == '__main__':
    constrains = [(-5., 5.), (-5., 5.)]
    simple_hc = SimpleHC(seed=42)
    shotgun_hc = ShotgunHC(seed=42)
    genetic = Genetic(seed=42)

    vis = Vision(functions={'Rastrigin': rastrigin,
                            'Rosenbrock': rosenbrock,
                            'Sphere': sphere},
                 algorithms={'Simple Hill Climbing': simple_hc,
                             'Shotgun Hill Climbing': shotgun_hc,
                             'Genetic Algorithm': genetic},
                 constr=constrains)
    vis.title('Vision')
    vis.mainloop()
