from hexBoard import Board

from z3 import Solver, sat, Int, Sum, Or, If

def makeBoard(size, towers, numRange):
	b = Board(size, numRange)
	b.fillBoard()
	b.setRandomHeights(towers)
	b.populateBlocked()
	return b


# assume board is setup from makeboard
def solve(board : Board):
	solver = Solver()
	
	vars = {}
	# populate integers
	for coord, tile in board.board.items():
		if tile[0] == 0:
			# tiles are not base tiles
			continue

		i = Int(f"{coord}")
		solver.add(i >= 1)
		solver.add( i <= board.numRange)
		vars[coord] = i

	for coord, tile in board.board.items():
		if tile[0] == 0:
			continue

		sights = board.getLines(coord)
		myVar = vars[coord]

		lineChecks = []
		for line in sights:
			comparisons = []
			for e in line:
				if e in vars:
					comparisons.append(vars[e] > myVar)
			if comparisons:
				lineChecks.append(
					If(Or(*comparisons), 1, 0)
				)
		solver.add(Sum(*lineChecks) == tile[1])
	
	if solver.check() == sat:
		model = solver.model()
		block = []
		for coord, var in vars.items():
			val = model.evaluate(var, model_completion=True)
			block.append(var != val)
		solver.add(Or(*block))

		if solver.check() == sat:
			pass
		else:
			print("found unique")
			print(board.board)
	else:
		print("unsat")

for i in range(100):
	solve(makeBoard(4, 22, 4))