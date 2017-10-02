import unittest
#import the actual unit test
import CheckWinLogic_Unittest

print "\n###################\nChecking CheckWinLogic...\n###################\n"
suite = unittest.TestLoader().loadTestsFromModule(CheckWinLogic_Unittest)
unittest.TextTestRunner(verbosity=2).run(suite)

