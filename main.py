import os
from pprint import pprint
import networkx as nx
from utils import (
    read_graph, odd_vertices, brute_force_minimum_matching, is_eulerian,
    min_edge_weight, total_weight, eulerian_route_pairs_and_nodes
)
from viz import draw_graph, draw_augmented_graph


def chinese_postman(file_path, out_dir="out"):
    # 0. Preparação de entrada e saída.
    G = read_graph(file_path) # Retorna erro se o grafo não for conexo
    pos = nx.spring_layout(G, seed=42)

    os.makedirs(out_dir, exist_ok=True)
    output_path_G = os.path.join(out_dir, "original.png")
    draw_graph(G, pos, output_path_G, title="Grafo original")

    base_cost = total_weight(G)

    # 1. Verifica se já é euleriano
    if is_eulerian(G):
        route_pairs, node_seq = eulerian_route_pairs_and_nodes(G)
        added_cost = 0.0
        total = base_cost + added_cost

        print("Sequência de nós do caminho final:", " -> ".join(map(str, node_seq)))
        print("Caminho final (arestas):", route_pairs)
        print(f"Custo base: {base_cost}")
        print(f"Custo adicional: {added_cost}")
        print(f"Custo total: {total}")
        return

    # 2. Vértices ímpares
    odd = odd_vertices(G)
    print("Vértices ímpares:", odd)

    # 3. Emparelhamento
    matching, cost = brute_force_minimum_matching(G, odd) # simples (por força bruta)
    print("Emparelhamento escolhido:", matching)
    print("Custo adicional:", cost)

    # 4. Duplicação das arestas dos caminhos escolhidos
    G_aug = G.copy()
    for u, v in matching:
        path = nx.shortest_path(G, u, v, weight="weight")
        for a, b in zip(path, path[1:]):
            w = min_edge_weight(G, a, b)
            G_aug.add_edge(a, b, weight=w, duplicate=True)
    output_path_G_aug = os.path.join(out_dir, "augmented.png")
    draw_augmented_graph(G_aug, pos, output_path_G_aug, title="Após duplicação")

    # 5. Circuito euleriano
    route_pairs, node_seq = eulerian_route_pairs_and_nodes(G_aug) # obter circuito euleriano
    total = total_weight(G_aug)
    added_cost = total - base_cost

    print("Sequência de nós do caminho final:", " -> ".join(map(str, node_seq)))
    pprint(f"Caminho final (arestas):{route_pairs}", width=30)
    print(f"Custo base: {base_cost}")
    print(f"Custo adicional: {added_cost}")
    print(f"Custo total: {total}")

if __name__ == "__main__":
    entrada = "graph3.input"
    chinese_postman(entrada)
