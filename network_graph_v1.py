import networkx as nx
from matplotlib import pyplot as plt
import re
import ast 

with open("node_interactions.txt", 'r') as f:
    node_string = f.read()
    node_lists = re.findall(r'\(.\w*.\W*\w*\W*\d\)', node_string) 

#node_list = [i for i in node_lists]
interactions = []
for i in node_lists:
    interactions.append(ast.literal_eval(i))
    #print(i)
#print(node_string[0:10])
nw = nx.Graph()
q = 0
for i in interactions:
    q += 1
    if i[2] > 1:
        nw.add_edge(i[0], i[1], weight = i[2])
        print(q)

#nx.draw(nw)
#plt.show()

nx.write_gexf(nw, "hashtag_network.gexf_degree_min_1")
