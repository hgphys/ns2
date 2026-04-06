"""
Zachary’s Karate Club の次数相関係数、同類選択性係数の計算
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 類似度のリスト
CN = []
JC = []
AA = []
PA = []

# karate_clubのグラフをインポート
G = nx.karate_club_graph()
n = nx.number_of_nodes(G)

# エッジが存在しない頂点間の類似度を計算する
for x in range(n):
    for y in range(x+1,n):
        if not(G.has_edge(x, y)):
            CN.append(tuple([x, y, len(list(nx.common_neighbors(G,x,y)))]))
            JC.append(list(nx.jaccard_coefficient(G,[(x,y)]))[0])
            AA.append(list(nx.adamic_adar_index(G,[(x,y)]))[0])
            PA.append(list(nx.preferential_attachment(G,[(x,y)]))[0])

# トップ k を表示する
k = 3

# エッジが存在しないノード間で類似度の高いものを可視化
print("Common neighbors")
print(sorted(CN, key=lambda x:x[2], reverse=True)[:k])

print("Jaccard coefficient")
print(sorted(JC, key=lambda x:x[2], reverse=True)[:k])

print("Adamic/Adar")
print(sorted(AA, key=lambda x:x[2], reverse=True)[:k])

print("Preferential attachment")
print(sorted(PA, key=lambda x:x[2], reverse=True)[:k])