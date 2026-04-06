"""
Zachary’s Karate Club の同時分布行列の計算と可視化
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# karate_clubのグラフをインポート
G = nx.karate_club_graph()

# degree_mixing_matrixを計算
degree_mixing_matrix = nx.degree_mixing_matrix(G, weight=None, nodes=None, normalized=True)

# クラブ名を取得
club_names = ['Mr. Hi', 'Officer']

# attribute_mixing_matrixを計算
attribute_mixing_matrix = nx.attribute_mixing_matrix(G, attribute='club', normalized=True)

# degree_mixing_matrixとattribute_mixing_matrixをヒートマップとして可視化
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(degree_mixing_matrix, cmap='Blues', interpolation='nearest')
axes[0].set_title('Degree Mixing Matrix')
axes[0].set_xlabel('Degree')
axes[0].set_ylabel('Degree')

axes[1].imshow(attribute_mixing_matrix, cmap='Reds', interpolation='nearest')
axes[1].set_title('Attribute Mixing Matrix (Club Membership)')
axes[1].set_xticks(np.arange(len(club_names)), club_names)
axes[1].set_yticks(np.arange(len(club_names)), club_names)
axes[1].set_xlabel('Club')
axes[1].set_ylabel('Club')

plt.show()
