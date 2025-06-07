import json
from ast import literal_eval

def export(filename, edgeSize, numRange=4):
	with open(filename) as f:
		
		content = literal_eval(f.read())
		combined = []
		for e in content:
			combined.append({
				"size" : edgeSize,
				"numRange" : numRange,
				"hexes" : [
					{
						"height" : tile[0],
						"at" : [coord[0], coord[1], - coord[0] - coord[1]]
					} for coord, tile in e.items()
				]
			})
		
		return json.dumps(combined)



# 4 sized ones
for i in range(15, 38):
	with open(f"importable/towersCombined{i}.json", "w") as f:
		f.write(export(f"out/out4-{i}.txt", 4))

