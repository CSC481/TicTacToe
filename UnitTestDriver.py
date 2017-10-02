import unittest, os, sys
import os, sys

lib_path = os.path.abspath(os.path.join('unittests'))
sys.path.append(lib_path)

#import the actual unit test
#import CheckWinLogic_Unittest
import CheckWinLogic_UT
import helloWorld
print "\n###################\nChecking CheckWinLogic...\n###################\n"
#suite = unittest.TestLoader().loadTestsFromModule(CheckWinLogic_Unittest)
#unittest.TextTestRunner(verbosity=2).run(suite)

