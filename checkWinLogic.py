class WinLogic:
	matrix = [[0 for x in range(3)] for y in range(3)] 
	player = ""
	debug = False
	def __init__(self):
		 return
		 
	def ClearMatrix(self):
		if WinLogic.debug:
			print "Clearing Matrix"
		WinLogic.matrix = [[0 for x in range(3)] for y in range(3)]
	
	def SetPlayer(self, player):
		if WinLogic.debug:
			print "Setting player as: " + player
		WinLogic.player = player
		
	def GetPlayer(self):
		if WinLogic.debug:
			print "Returning: " + WinLogic.player
		return WinLogic.player
	
	def SetGrid(self, val, w, h):
		if WinLogic.debug:
			print "Setting grid..."
		WinLogic.matrix[w][h] = val
		
	def GetGrid(w, h):
		return WinLogic.matrix[w] [h]
		
	def hasPlayerWon(self, player):
		return False
		if WinLogic.debug:
			print "Checking for winner"
		if(WinLogic.matrix[0] [0] == MyClass.player):
			if WinLogic.debug:
				print WinLogic.player + " has won"
			return True
		else:
			if WinLogic.debug:
				print "No Player has won"
			return False
			

m = WinLogic()
if m.debug:
	m.SetPlayer("test")
	m.SetGrid(m.GetPlayer(),0,0)
	m.hasPlayerWon(m.GetPlayer)
	m.ClearMatrix()
	m.hasPlayerWon(m.GetPlayer)

#m.SetPlayer("Test")
#print m.GetPlayer()
#hasPlayerWon("test")
#print m[0] [0]
		


