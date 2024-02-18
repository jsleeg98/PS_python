import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 팀 점수 계산
def team_score(graph, members):
    score = 0
    for i in range(0, len(members) - 1):
        for j in range(i+1, len(members)):
            score += graph[members[i]-1][members[j]-1]
            score += graph[members[j]-1][members[i]-1]
    return score

# 백트레킹
def dfs(graph, li_cur, cur, team_num, N):
    global res
    if len(li_cur) == team_num:  # 팀이 다 구성된 경우
        t1 = team_score(graph, li_cur)  # 1팀 점수 계산
        # 2팀 멤버 찾기
        li_t2 = []
        for i in range(1, N+1):
            if not i in li_cur:
                li_t2.append(i)
        t2 = team_score(graph, li_t2)  # 2팀 점수 계산
        if res > abs(t1 - t2):  # 가장 작은 점수차이 저장
            res = abs(t1 - t2)

    else:
        for i in range(cur + 1, N+1):  # 팀 멤버 구성
            li_cur.append(i)
            dfs(graph, li_cur, i, team_num, N)
            li_cur.pop()


res = 1000
dfs(graph, [], 0, N//2, N)
print(res)