import md
import unittest, sys
import os



class intTest(unittest.TestCase):
    def tearDown(self):
        os.remove("cu.traj")

    def testRunMD(self):
        md.run_md()
        assert os.path.exists("cu.traj")



if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(intTest)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())