import networkx
import matplotlib.pyplot
g = networkx.Graph()

a = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2]
b = [11,22,33,44,55,234,56,88,90,98,123,345,98,123,345]
c = [111,111,1111,122,122,122,134,1234,12424,111,123,123,2,2,2]
g.add_edges_from(zip(b,a))
g.add_edges_from(zip(b,c))

networkx.draw(g)

matplotlib.pyplot.show()