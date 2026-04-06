"""
Zachary’s Karate Club における共通する隣接ノードの計算
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# karate_clubのグラフをインポート
G = nx.karate_club_graph()

# 各クラブの色を指定します。
club_colors = {
    'Mr. Hi': 'blue',
    'Officer': 'red'
}

# ノードの色をクラブに応じて設定
node_colors = [club_colors[G.nodes[node_id]['club']] for node_id in G.nodes]

# ネットワークを可視化
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=300)
plt.title('Karate Club Network')
plt.show()

# 注目するノードのペア
v = 0
w = 1

# 隣接ノードのリスト
list_neighbor_v = list(G.neighbors(v))
list_neighbor_w = list(G.neighbors(w))
list_common_neighbors_vw =list(nx.common_neighbors(G,v,w))

print("注目するノードのペア:", v, " と ", w)
print("ノード",v, "の隣接ノード:", list(list_neighbor_v))
print("ノード",w, "の隣接ノード:", list(list_neighbor_w))
print("共通するノード", list_common_neighbors_vw)