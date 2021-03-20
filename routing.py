from functools import lru_cache
from collections import defaultdict
num_city = 8
num_warehouse = 3
num_road = 11

warehouse = [[12, 5, 1], [11, 10, 6], [1, 6, 7]]


edge_list = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5],
             [5, 6], [5, 7], [5, 8], [4, 6], [3, 7], [7, 8]]

orders = [[3, 4], [4, 4], [7, 5]]


class Solution:

    def solve(self, N, D, edge_list, warehouse, orders):
        global_wh = {d[2]: {'num_item': d[0], 'cost_per_km': d[1]}
                     for d in warehouse}
        adj_list = defaultdict(list)
        for i in edge_list:
            adj_list[i[0]].append(i[1])
        # orders = 0 mean qty, = 1 at city ith

        order_dict = defaultdict(int)
        for order in orders:
            order_dict[order[1]] += order[0]

        # find min cost between cities
        cost = [[float('inf')] * N for _ in range(N)]
        for i, arr in adj_list.items():
            for j in arr:
                cost[i-1][j-1] = 1
                cost[j-1][i-1] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if i == j:
                        cost[i][j] = 0
                    cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])

        o_tup = []
        for ith, num in order_dict.items():
            o_tup.append((ith, num))
        o_tup = tuple(o_tup)

        @lru_cache(None)
        def dp(qty_tup):
            if sum(s[1] for s in qty_tup) == 0:
                d = []
                for ith, wh in global_wh.items():
                    d.append((ith, wh['num_item']))
                return 0, tuple(d)

            res = float('inf')
            res_wh = None
            for i in range(len(qty_tup)):
                new_tup = list(qty_tup)
                temp = list(new_tup[i])
                temp[1] -= 1
                ith = temp[0]
                new_tup[i] = tuple(temp)

                res_sub = dp(tuple(new_tup))
                warehouse = res_sub[1]
                warehouse = list(warehouse)
                best_cost = float('inf')
                best_wh = None
                for i, wh in enumerate(warehouse):
                    if wh[1] <= 0:
                        continue
                    warehouse[i] = list(wh)
                    i_warehouse = wh[0]
                    if global_wh[i_warehouse]['cost_per_km'] * cost[i_warehouse-1][ith-1] < best_cost:
                        best_cost = global_wh[i_warehouse]['cost_per_km'] * \
                            cost[i_warehouse-1][ith-1]
                        best_wh = i
                warehouse[best_wh][1] -= 1
                if res_sub[0] + best_cost < res:
                    res_wh = warehouse
                    res = res_sub[0] + best_cost
            return res, res_wh

        return dp(o_tup)


print(Solution().solve(8, num_warehouse, edge_list, warehouse, orders))