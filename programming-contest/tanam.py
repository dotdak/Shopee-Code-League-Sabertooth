def forward(matrix, k):
    return sum(matrix[k])

def forward_backward(matrix, k):
    max_s = float('-inf')
    max_end = 0
    for i in matrix[k]:
        max_end += i
        max_s = max(max_s, max_end)
        if max_end < 0:
            break
    return max_s if max_s > 0 else 0

def backward_forward(matrix, k):
    max_s = float('-inf')
    max_end = 0
    for i in range(len(matrix[k])-1, -1, -1):
        max_end += matrix[k][i]
        max_s = max(max_s, max_end)
    return max_s if max_s > 0 else 0


MOVE = {
    'fw': forward,
    'f&b': forward_backward,
    'bw': forward,
    'b&f': backward_forward
} # 'forward','forward & back', 'backward', 'backward & back'

def re(matrix, k, pos, s, ans):
    if k == len(matrix):
        ans.append(s)
        return
    if pos == 0:
        s1 = MOVE['fw'](matrix, k)
        re(matrix, k+1, 1, s+s1, ans)
        s2 = MOVE['f&b'](matrix, k)
        re(matrix, k+1, 0, s+s2, ans)
    if pos == 1:
        s1 = MOVE['bw'](matrix, k)
        re(matrix, k+1, 0, s+s1, ans)
        s2 = MOVE['b&f'](matrix, k)
        re(matrix, k+1, 1, s+s2, ans)

def solution(matrix):
    maxx = 0
    ans = []
    re(matrix, 0, 0, 0, ans)
    return max(ans)

# matrix= [[1,4,-5], [-1,-9,100]]
# matrix= [[1,4,-5], [-1,-1,100]]
# matrix= [[-9, -8, 1, 2, 3]]

testcase = int(input())
for _ in range(testcase):
    n, m = list(map(int, input().split(" ")))
    matrix = []
    for _ in range(n):
        line = list(map(int, input().split(" ")))
        matrix.append(line)
    print(solution(matrix))
