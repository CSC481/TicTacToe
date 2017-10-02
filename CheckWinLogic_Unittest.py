#This can run independently

import unittest
from checkWinLogic import WinLogic


#Each def test a specific patern. Hardcoded, yes, but the failure output list per function so 
class CheckWinLogic(unittest.TestCase):
	def test_temp_hasPlayerWon_CollumnOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,0,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 1

	def test_temp_hasPlayerWon_CollumnTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,1,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 2
		
	def test_temp_hasPlayerWon_CollumnThree(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,2,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 3
		
	#Check Rows
	def test_temp_hasPlayerWon_RowOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,0)
		self.assertTrue(win.hasPlayerWon(player)) #win case 4

	def test_temp_hasPlayerWon_RowTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,1)
		self.assertTrue(win.hasPlayerWon(player)) #win case 5
		
	def test_temp_hasPlayerWon_RowThree(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,2)
		self.assertTrue(win.hasPlayerWon(player)) #win case 6
	def test_temp_hasPlayerWon_DiagOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		win.SetGrid(player,0,0)
		win.SetGrid(player,1,1)
		win.SetGrid(player,2,2)
		self.assertTrue(win.hasPlayerWon(player)) #win case 7
		
	def test_temp_hasPlayerWon_DiagTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		win.SetGrid(player,0,2)
		win.SetGrid(player,1,1)
		win.SetGrid(player,2,0)
		self.assertTrue(win.hasPlayerWon(player)) #win case 8

#unittest.main()
if __name__ == '__main__':
	#hasPayerWon()
    unittest.main()
