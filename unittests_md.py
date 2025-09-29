import sys, unittest
from md import calcenergy

from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from asap3 import EMT


class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        atoms = FaceCenteredCubic(
            directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            symbol='Cu',
            size=(10, 10, 10),
            pbc=True,
        )
        atoms.calc = EMT()
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)
        [epot, ekin, etot, inst_temp] = calcenergy(atoms)
        print(inst_temp)
        assert abs(300 - inst_temp) <= 3


if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())