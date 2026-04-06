"""
確率的ブロックモデルによるグラフ生成
"""
import networkx as nx
import random
import matplotlib.pyplot as plt
import seaborn as sns

# ブロックモデルを作成する関数
def create_block_model(num_blocks, block_size, p_in, p_out):
    G = nx.Graph()
    
    # ブロック内のエッジを生成
    for block in range(num_blocks):
        nodes_in_block = list(range(block * block_size, (block + 1) * block_size))
        G.add_nodes_from(nodes_in_block)
        for i in nodes_in_block:
            for j in nodes_in_block:
                if i != j and random.random() < p_in:
                    G.add_edge(i, j)
    
    # ブロック間のエッジを生成
    for block1 in range(num_blocks):
        for block2 in range(block1 + 1, num_blocks):
            for node1 in range(block1 * block_size, (block1 + 1) * block_size):
                for node2 in range(block2 * block_size, (block2 + 1) * block_size):
                    if random.random() < p_out:
                        G.add_edge(node1, node2)
    
    return G

# ブロックモデルのグラフを生成
num_blocks = 2
block_size = 50
p_in = 0.5
p_out = 0.5

block_model_graph = create_block_model(num_blocks, block_size, p_in, p_out)

# グラフの情報を出力
print(f"ノード数: {block_model_graph.number_of_nodes()}")
print(f"エッジ数: {block_model_graph.number_of_edges()}")

# 各ブロック内のノード数を出力
for block in range(num_blocks):
    nodes_in_block = list(range(block * block_size, (block + 1) * block_size))
    print(f"ブロック {block}: {len(nodes_in_block)}ノード")

# ブロックモデルの可視化
# ノードの前半を赤、後半を青に分ける
node_colors = ['red' if i < num_blocks * block_size // 2 else 'blue' for i in range(block_model_graph.number_of_nodes())]

pos = nx.spring_layout(block_model_graph)
nx.draw(block_model_graph, pos, node_color=node_colors, with_labels=True)
plt.show()

# 隣接行列を取得
adj_matrix = nx.to_numpy_array(block_model_graph)

# ヒートマップとして可視化
sns.set()
plt.figure(figsize=(8, 8))
sns.heatmap(adj_matrix, cmap="binary", annot=False, square=True, cbar=False, xticklabels=False, yticklabels=False)
plt.show()