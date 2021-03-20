from itertools import combinations

n, k = list(map(int, input().split(" ")))
vs = list(map(int, input().split(" ")))

for _ in range(n):
    vs.append(int(input()))

def solution(n, k, vs):
    count = 0
    sum_count = set()
    for i in range(1, len(vs) + 1):
        com = combinations(vs, i)
        for j in set(com):
            sum_count.add((sum(j), len(j)))
    for s, num in sum_count:
        if s/num >= k:
            count += 1
    return count

# print(solution(3, 3, [1,3,4]))
# print(solution(6, 3, [1,1,4,5,1,4]))

print(solution(n, k, vs))
