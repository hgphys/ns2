"""
Zachary’s Karate Club に対する代表的なノード間の類似性の計算
"""
import networkx as nx
import numpy as np
import pandas as pd

# karate_clubのグラフをインポート
G = nx.karate_club_graph()

# 注目するノードのペア
v = 0
w = 1

# 代表的なノード間の類似度
print("注目するノードのペア:", v, " と ", w)
print("CN:", len(list(nx.common_neighbors(G,v,w))))
print("JC:", list(nx.jaccard_coefficient(G,[(v,w)]))[0][2])
print("AA:", list(nx.adamic_adar_index(G,[(v,w)]))[0][2])
print("PA:", list(nx.preferential_attachment(G,[(v,w)]))[0][2])