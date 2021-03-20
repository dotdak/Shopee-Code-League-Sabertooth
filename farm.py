g_graph = {
    1: {
        'node': [2, 3, 5, 6, 7],
        'coin': 700,
    },
    2: {
        'node': [1, 3, 4, 6, 8],
        'coin': 701,
    },
    3: {
        'node': [1, 2, 4, 5, 9],
        'coin': 702,
    },
    4: {
        'node': [2, 3, 8, 9, 10],
        'coin': 703,
    },
    5: {
        'node': [1, 3, 7, 9, 11],
        'coin': 704,
    },
    6: {
        'node': [1, 2, 7, 8, 12],
        'coin': 705,
    },
    7: {
        'node': [1, 5, 6, 11, 12],
        'coin': 706,
    },
    8: {
        'node': [2, 4, 6, 10, 12],
        'coin': 707,
    },
    9: {
        'node': [3, 4, 5, 10, 11],
        'coin': 708,
    },
    10: {
        'node': [5, 8, 9, 11, 12],
        'coin': 709,
    },
    11: {
        'node': [5, 7, 9, 10, 12],
        'coin': 710,
    },
    12: {
        'node': [6, 7, 8, 10, 11],
        'coin': 711,
    },
}

def increase_coin(graph):
    for k in graph:
        graph[k]['coin'] = min(graph[k]['coin'] + 200, 700 + k) if graph[k]['coin'] > 0 else 200 + k

def take_coin(graph, node):
    coin = graph[node]['coin']
    graph[node]['coin'] = 0
    return coin

def move_from(graph, node):
    next = graph[node]['node'][0]
    for k in graph[node]['node']:
        next = k if graph[k]['coin'] > graph[next]['coin'] else next
    return next

def solution(D, graph=g_graph):
    pos = 3
    s = take_coin(graph, pos)
    for _ in range(0, D - 1, 2):
        pos = move_from(graph, pos)
        s += take_coin(graph, pos)
        increase_coin(graph)
    return s

D = int(input())
print(solution(D))