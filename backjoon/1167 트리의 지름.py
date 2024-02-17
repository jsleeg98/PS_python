import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

V = int(sys.stdin.readline())
graph = [[] for i in range(V + 1)]

for i in range(V):
    cmd = list(map(int, sys.stdin.readline().split()))
    node = cmd[0]
    idx = 1
    while cmd[idx] != -1:
        end, dist = cmd[idx], cmd[idx+1]
        graph[node].append((end, dist))
        idx += 2



def BFS(start, visit):
    q = deque()
    q.append((start, 0))
    visit[start] = 1
    ddist = 0
    end_node = 0
    while q:
        now, dist = q.popleft()
        for i in graph[now]:
            if visit[i[0]] == 0:
                q.append((i[0], dist + i[1]))
                visit[i[0]] = 1
                if ddist < dist + i[1]:
                    end_node = i[0]
                    ddist = dist + i[1]
    return end_node, ddist

# 트리의 지름은 임의의 한 노드에서 가장 먼 노드에서의 가장 먼 거리
# 트리의 지름에 해당하는 노드 중 하나는 반드시 임의의 한 노드에서 측정한 거리 중 가장 먼 거리에 있음

visit = [0 for i in range(V + 1)]
end_node, ddist = BFS(1, visit)
visit = [0 for i in range(V + 1)]
end_node, ddist = BFS(end_node, visit)
print(ddist)