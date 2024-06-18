import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpl
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 16,
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
    "axes.unicode_minus": False,
}
rcParams.update(config)

# Output directory
outdir = input(r'Please enter the image output path (e.g. D:\Users\test):')

t = int(input('t ='))

plt.figure(figsize=(12, 12), dpi = 1000)
G = nx.Graph()
colors = dict(zip(range(10), mpl.TABLEAU_COLORS))
node_colors = []
k = 0
G.add_nodes_from([k,k+1,k+2])
node_colors += [colors[0]]*3
G.add_edges_from([(k,k+1),(k,k+2),(k+1,k+2)])
edge_lis = [[(k,k+1),(k,k+2),(k+1,k+2)]]
k = k+3
for i in range(2, t+1):
    temp_lis = []
    for elst in edge_lis:
        G.add_nodes_from([k,k+1,k+2])
        G.add_edges_from([(k,k+1),(k,k+2),(k+1,k+2)])
        node_colors += [colors[i-1]]*3
        for ind, e in enumerate(elst):
            G.add_edges_from([(k+ind,e[0]),(k+ind,e[1])])
            elis = [e,(k+ind,e[0]),(k+ind,e[1])]
            temp_lis.append(elis)
        k = k+3
    edge_lis = temp_lis.copy()
    
nx.draw(
    G,
    pos=nx.planar_layout(G),
    node_size = 20,
    node_color = node_colors,
    width = 0.5
)
plt.savefig(outdir+'\\t=%d.png'%(t))
plt.savefig(outdir+'\\t=%d.jpg'%(t))
plt.show()