"""
相関係数を用いたネットワークの類似性の計算
"""

import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

import itertools

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

# 隣接行列を取得
A1 = nx.adjacency_matrix(G1, nodelist=[0,1,2,3,4]).toarray()
# 隣接行列をベクトルに変換
vec_A1 = A1.flatten()

# 5つのノードのすべての並び替えを生成
permutations = list(itertools.permutations([0, 1, 2, 3, 4]))

gcor_list = []
for i in range(len(permutations)):
    A2 = nx.adjacency_matrix(G2, nodelist=list(permutations[i])).toarray()
    # 隣接行列をベクトルに変換
    vec_A2 = A2.flatten()
    # 相関係数を計算
    correlation_coefficient, _ = pearsonr(vec_A1, vec_A2)
    gcor_list.append(correlation_coefficient)

# ヒストグラムを作成
plt.hist(gcor_list, bins=5, edgecolor='black', alpha=0.7)
# `bins`は階級（ビン）の数を指定します。この例では5つの階級にデータを分割しています。

# グラフのタイトルやラベルを設定
plt.xlabel("Correlation")
plt.ylabel("Frequency")

# ヒストグラムを表示
plt.show()


# 確認したい値
target_value = 0.5

# データをソート
sorted_data = np.sort(gcor_list)

# target_valueを超える最小の値の位置を見つける
position = np.searchsorted(sorted_data, target_value)

# 上位何パーセントに含まれるか計算
percentile = (1 - position / len(gcor_list)) * 100

print(f"{target_value} は上位 {percentile}% に含まれます。")