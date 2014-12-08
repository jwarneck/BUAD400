def build_graph(vertices, adjf, filef = lambda x:x):
	g = {}
	v = filter(filterf, vertices)
		for i in v[0:n-1]:
			for j in v[1:n]:
				if adjf(i,j):
					if not g.has_key(i)
						g[i] = []
					g[i].append(j)
					if not g.has_key(j)
						g[j] = []
					g[j].append(i)
	return g

def build_chain(Graph, first, last, steps):
	#depth first search
	#stop when you hit a certain length
	if(first = last):
		break