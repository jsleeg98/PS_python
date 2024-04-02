import heapq
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


MAX_D = 300
MAX_N = 50000
INF = sys.maxsize

is_in_readyq = [[] for _ in range(MAX_D + 1)]

rest_judger = []

judging_domain = [0 for _ in range(MAX_N + 1)]

s = [0 for _ in range(MAX_D + 1)]
g = [0 for _ in range(MAX_D + 1)]
e = [0 for _ in range(MAX_D + 1)]

domainToIdx = {}
global cnt
cnt = 0

global ans
ans = 0

url_pq = [[] for _ in range(MAX_D + 1)]

def Init(qurey):  # 100 n u0
    global n
    (empty, n, url) = qurey
    n = int(n)

    global cnt

    for i in range(1, n + 1):
        rest_judger.append(i)

    idx = 0
    for i in range(len(url)):
        if url[i] == '/':
            idx = i
            break

    domain = url[:idx]
    num = int(url[idx + 1:])

    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    is_in_readyq[domain_idx].append(num)

    newUrl = (1, 0, num)
    heapq.heappush(url_pq[domain_idx], newUrl)

    global ans
    ans += 1

def NewUrl(query):
    (empty, tme, id, url) = query
    tme = int(tme)
    id = int(id)

    global cnt

    idx = 0
    for i in range(len(url)):
        if url[i] == '/':
            idx = i
            break

    domain = url[:idx]
    num = int(url[idx + 1:])

    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    if num in is_in_readyq[domain_idx]:
        return
    is_in_readyq[domain_idx].append(num)

    newUrl = (id, tme, num)
    heapq.heappush(url_pq[domain_idx], newUrl)

    global ans
    ans += 1

def Assign(query):
    (empty, tme) = query
    tme = int(tme)

    if len(rest_judger) == 0:
        return

    min_domain = 0
    minUrl = (INF, 0, 0)

    global cnt

    for i in range(1, cnt + 1):
        if e[i] > tme:
            continue

        if len(url_pq[i]) > 0:
            curUrl = url_pq[i][0]

            if minUrl[0] != curUrl[0]:
                if minUrl[0] > curUrl[0]:
                    minUrl = curUrl
                    min_domain = i
            elif minUrl[1] != curUrl[1]:
                if minUrl[1] > curUrl[1]:
                    minUrl = curUrl
                    min_domain = i

    if min_domain:
        judger_idx = heapq.heappop(rest_judger)

        heapq.heappop(url_pq[min_domain])

        s[min_domain] = tme
        e[min_domain] = INF

        judging_domain[judger_idx] = min_domain

        is_in_readyq[min_domain].remove(minUrl[2])

        global ans
        ans -= 1

def Finish(query):
    (empty, tme, id) = query
    tme = int(tme)
    id = int(id)

    if judging_domain[id] == 0:
        return

    heapq.heappush(rest_judger, id)

    domain_idx = judging_domain[id]
    judging_domain[id] = 0

    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]

def Check(query):
    global ans
    print(ans)


q = int(input())

for _ in range(q):
    query = input().split()

    if int(query[0]) == 100:
        # 채점기를 준비합니다.
        Init(query)
    if int(query[0]) == 200:
        # 새로운 url을 입력받아 레디큐에 추가해줍니다.
        NewUrl(query)
    if int(query[0]) == 300:
        # 다음 도메인을 찾아 assign합니다.
        Assign(query)
    if int(query[0]) == 400:
        # 채점 하나를 마무리합니다.
        Finish(query)
    if int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
        Check(query)