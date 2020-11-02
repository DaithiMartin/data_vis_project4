import networkx as nx
import matplotlib.pyplot as plt
import simplejson as json

# load the data in .gml format
G = nx.read_gml("dolphins.gml")

# plot to get sense of the data
# nx.draw(G)
# plt.show()

# convert to json and write to file
data = nx.readwrite.node_link_data(G)
del data['directed']
del data['multigraph']
del data['graph']

node_list = list(G.nodes)
deg_list = [node[1] for node in G.degree]

augmented_nodes = [{"id": name, "degree": degree} for name, degree in zip(node_list, deg_list)]

data['nodes'] = augmented_nodes
print()

with open('dolphins.json', 'w') as outfile:
    json.dump(data, outfile)
