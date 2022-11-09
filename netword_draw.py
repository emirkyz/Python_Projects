import matplotlib.pyplot as plt
import networkx as nx

G = nx.gnp_random_graph(10, 0.5)
pos = nx.spring_layout(G)

plt.figure(figsize=(8, 8))

node_size = 50
ring_size = 100 + node_size

edges = nx.draw_networkx_edges(G, pos, alpha=0.4)
nodes = nx.draw_networkx_nodes(
    G,
    pos,
    node_size=node_size,
    node_color='red',
)

rings = nx.draw_networkx_nodes(
    G,
    pos,
    node_size=ring_size,
    node_color='green',
)

nodes.set_zorder(2)
rings.set_zorder(1)

plt.axis("off")
plt.show()

import matplotlib

n = 7
m = 5
outer_gs = matplotlib.gridspec.GridSpec(2, 2, height_ratios=[n, 1], width_ratios=[m, 1], hspace=0.1, wspace=0.1)
inner_gs = matplotlib.gridspec.GridSpecFromSubplotSpec(n, m, subplot_spec=outer_gs[0, 0], hspace=0, wspace=0)
line_gs = matplotlib.gridspec.GridSpecFromSubplotSpec(n, 1, subplot_spec=outer_gs[0, 1], hspace=0, wspace=0.1)
col_gs = matplotlib.gridspec.GridSpecFromSubplotSpec(1, m, subplot_spec=outer_gs[1, 0], hspace=0.1, wspace=0)
ax_11 = []
ax_12 = []
ax_21 = []
ax_22 = []
fig = plt.figure(figsize=(18, 10))
for i in range(n):
    ax_11.append([])
    for j in range(m):
        ax_11[i].append(fig.add_subplot(inner_gs[i, j]))
        if not ax_11[i][j].get_subplotspec().is_first_col():
            ax_11[i][j].axes.yaxis.set_visible(False)
        ax_11[i][j].axes.xaxis.set_visible(False)

for i in range(n):
    ax_12.append(fig.add_subplot(line_gs[i, 0]))
    ax_12[i].axes.yaxis.set_visible(False)
    ax_12[i].axes.xaxis.set_visible(False)

for i in range(m):
    ax_21.append(fig.add_subplot(col_gs[0, i]))
    if not ax_21[i].get_subplotspec().is_first_col():
        ax_21[i].axes.yaxis.set_visible(False)

ax_22 = fig.add_subplot(outer_gs[1, 1])
ax_22.axes.yaxis.set_visible(False)
plt.show()