#This can run independently
import unittest, sys, os

#modifying sys path to import winLogic
lib_path = os.path.abspath(os.path.join('..','Game'))
sys.path.append(lib_path)

class CheckMenuLogic(unittest.TestCase):


#unittest.main()
if __name__ == '__main__':
	#hasPayerWon()
    unittest.main()