"""
Zachary’s Karate Club の次数相関係数、同類選択性係数の計算
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

# degree_assortativity_coefficientを計算
degree_assortativity = nx.degree_assortativity_coefficient(G)
print(f'次数相関係数: {degree_assortativity}')

# attribute_assortativity_coefficientを計算
attribute_assortativity = nx.attribute_assortativity_coefficient(G, 'club')
print(f'属性の同類選択性係数: {attribute_assortativity}')