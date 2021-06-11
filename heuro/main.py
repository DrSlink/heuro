"""Script for project run."""
from heuro.landscapes.so import rastrigin
from heuro.landscapes.so import rosenbrock
from heuro.landscapes.so import sphere
from heuro.population.hill_climbing import SimpleHC
from heuro.population.hill_climbing import ShotgunHC
from heuro.population.evolution import Genetic

from heuro.gui.vision import Vision

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
