"""
相関係数を用いたネットワークの類似性の計算
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# CSVファイルからエッジリストを読み込む関数
def read_edge_list_from_csv(file_path):
    df = pd.read_csv(file_path)
    edges = [(row['Source'], row['Target']) for index, row in df.iterrows()]
    return edges

# CSVファイルからエッジリストを読み込む
edges_A1 = read_edge_list_from_csv('data/A1_edges.csv')
edges_A2 = read_edge_list_from_csv('data/A2_edges.csv')

# グラフを作成
G1 = nx.Graph(edges_A1)
G2 = nx.Graph(edges_A2)


# レイアウトを指定してネットワークを可視化
pos = {0:[0,0], 1:[0, 1], 2:[0.5, 0.5], 3:[1, 1], 4:[1, 0]}

plt.figure(figsize=(12, 5))

plt.subplot(121)
nx.draw(G1, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=8, font_color='black')
plt.title("Friend")

plt.subplot(122)
nx.draw(G2, pos, with_labels=True, node_size=300, node_color='lightcoral', font_size=8, font_color='black')
plt.title("Advice")

plt.tight_layout()
plt.show()

# 隣接行列を取得
A1 = nx.adjacency_matrix(G1, nodelist=[0,1,2,3,4]).toarray()
A2 = nx.adjacency_matrix(G2, nodelist=[0,1,2,3,4]).toarray()

# 隣接行列をベクトルに変換
vec_A1 = A1.flatten()
print(vec_A1)
vec_A2 = A2.flatten()
print(vec_A2)

# 相関係数を計算
correlation_coefficient, _ = pearsonr(vec_A1, vec_A2)

print("ネットワークの相関係数:",correlation_coefficient)