import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

# 어느 방향으로 회전해야하는지 확인하는 함수(T, 회전 시키려는 톱니 인덱스, 방향, wheels)
def check_move(T, N, D, wheels):
    dir = [0] * T  # 방향 리스트 초기화
    dir[N] = D  # 입력 톱니바퀴 방향 초기화
    # 왼쪽 방향 체크
    left = wheels[N][6]  # 왼쪽에 있는 극 초기화
    L_D = D  # 방향 초기화
    for i in range(N - 1, -1, -1):
        if left != wheels[i][2]:  # 극이 다르다면
            L_D *= -1  # 반대 방향으로 움직임
            dir[i] = L_D  # 방향 저장
            left = wheels[i][6]  # 다음 왼쪽에 있는 극 갱신
        else:  # 그렇지 않으면 종료
            break

    # 오른쪽 방향 체크
    right = wheels[N][2]  # 오른쪽에 있는 극 초기화
    R_D = D  # 방향 초기화
    for i in range(N + 1, T, 1):
        if right != wheels[i][6]:  # 극이 다르다면
            R_D *= -1  # 반대 방향으로 움직임
            dir[i] = R_D  # 방향 저장
            right = wheels[i][2]  # 다음 오른쪽에 있는 극 갱신
        else:  # 그렇지 않으면 종료
            break

    return dir

# 회전 시키는 함수(방향 리스트, 바퀴 리스트)
def rotate(dirs, wheels):
    for i in range(len(wheels)):
        if dirs[i] == 1:  # 시계방향 회전
            tmp = wheels[i].pop()
            wheels[i].appendleft(tmp)
        elif dirs[i] == -1:  # 반시계방향 회전
            tmp = wheels[i].popleft()
            wheels[i].append(tmp)


T = int(input())
wheels = []
for _ in range(T):
    d = deque(input().rstrip())
    wheels.append(d)

C = int(input())
for _ in range(C):
    N, D = map(int, input().split())
    dirs = check_move(T, N - 1, D, wheels)
    rotate(dirs, wheels)

# 12시 방향의 값이 S극인 개수
cnt = 0
for i in range(T):
    if wheels[i][0] == '1':
        cnt += 1
print(cnt)


