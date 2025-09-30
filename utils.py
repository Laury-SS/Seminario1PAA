import itertools
import networkx as nx


def read_graph(path):
    G = nx.MultiGraph()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            u, v, w = [x.strip() for x in line.split(";")]
            G.add_edge(u, v, weight=float(w), duplicate=False)
    if not nx.is_connected(G.to_undirected()):
        raise ValueError("O grafo precisa ser conexo para o PCC.")
    return G


def odd_vertices(G):
    return [v for v, d in G.degree() if d % 2 == 1]

def is_eulerian(G):
    return nx.is_eulerian(G)


def shortest_path_length(G, u, v):
    return nx.dijkstra_path_length(G, u, v, weight="weight")

def brute_force_minimum_matching(G, odd):
    """
    Emparelhamento perfeito de custo mínimo:
    - Gera permutações dos vértices ímpares e forma pares consecutivos.
    - Pré-calcula distâncias de menor caminho para eficiência.
    complexidade fatorial em len(odd).
    """
    if not odd:
        return [], 0.0

    import itertools

    # Pré-calcula distâncias entre todos os pares de nós
    dist = dict(nx.all_pairs_dijkstra_path_length(G, weight="weight"))

    best_cost = float("inf")
    best_matching = None
    seen = set()

    # fixa o primeiro elemento da permutação como o menor rótulo
    # para reduzir simetrias
    anchor = min(odd)

    for perm in itertools.permutations(odd):
        if perm[0] != anchor:
            continue

        # Forma pares consecutivos: (p0,p1), (p2,p3), ...
        pairs = [(perm[i], perm[i + 1]) for i in range(0, len(odd), 2)]

        # Forma canônica para evitar contar a mesma combinação em ordens diferentes
        canon = tuple(sorted(tuple(sorted(p)) for p in pairs))
        if canon in seen:
            continue
        seen.add(canon)

        # Custo = soma das distâncias de menor caminho dos pares
        cost = sum(dist[u][v] for (u, v) in pairs)

        if cost < best_cost:
            best_cost = cost
            best_matching = pairs

    return best_matching, best_cost



def min_edge_weight(G, u, v):
    data = G.get_edge_data(u, v)
    return min(attr.get("weight", 1.0) for attr in data.values())


def total_weight(G):
    return float(sum(d.get("weight", 1.0) for _, _, d in G.edges(data=True)))


def eulerian_route_pairs_and_nodes(G):
    """
    Retorna:
      - route_pairs: lista de (u, v) em ordem do circuito euleriano,
      - node_seq: sequência de nós correspondente.
    """
    try:
        eul = list(nx.eulerian_circuit(G, keys=True))  # [(u,v,key), ...]
        route_pairs = [(u, v) for (u, v, _) in eul]
    except TypeError:
        eul = list(nx.eulerian_circuit(G))             # [(u,v), ...]
        route_pairs = eul

    if not route_pairs:
        return [], []

    node_seq = [route_pairs[0][0]] + [v for _, v in route_pairs]
    return route_pairs, node_seq
