"""
Zachary’s Karate Club の可視化と属性毎の頂点数の確認
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

# 属性付きノードリストの保存
df_nodes = pd.DataFrame(dict(G.nodes(data=True))).T
df_nodes.to_csv("data/karate_club_nodes.csv", index=False)

print(df_nodes)