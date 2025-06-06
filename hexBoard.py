from random import sample, randint
offsets = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

class Board:
	def __init__(self, size, numRange):
		self.board = {}
		self.numRange = numRange
		self.size = size
	def fillBoard(self):
		size = self.size - 1

		for q in range(-size, size + 1):
			r1 = max(-size, -q - size)
			r2 = min(size, -q + size)
			for r in range(r1, r2 + 1):
				self.board[(q, r)] = (0, 0)
	

	def setRandomHeights(self, numTowers):
		selectedSpots = sample(list(self.board.keys()), numTowers)
		heights = [randint(1, self.numRange) for _ in range(numTowers)]
		while not set(e + 1 for e in range(self.numRange)).issubset(heights):
			heights = [randint(1, self.numRange) for _ in range(numTowers)]
		
		for i, e in enumerate(selectedSpots):
			self.board[e] = (heights[i], 0) # height, blocked (to populate)

	# get a list of all hexes inline in order for each direction, regardless of blocks
	def getLines(self, spot):
		sights = []
		for dq, dr in offsets:
			sights.append([])
			q, r = spot
			q += dq
			r += dr

			while (q, r) in self.board:
				sights[-1].append((q, r))
				q += dq
				r += dr
		return sights

	def populateBlocked(self):
		for coord, tile in self.board.items():
			if tile[0] == 0:
				continue
			
			lines = self.getLines(coord)
			blocked = 0
			for line in lines:
				for spot in line:
					if self.board[spot][0] > tile[0]:
						blocked += 1
						break
			self.board[coord] = (tile[0], blocked)


			









	
