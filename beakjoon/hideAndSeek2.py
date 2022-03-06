from collections import deque

N, K = map(int, input().split())

INF = int(1e9)
max_len = max(N, K) * 2 + 1
distance = [INF] * max_len

q = deque()
q.append(N)
distance[N] = 0

cnt = 0
while q:
    now = q.popleft()

    if now == K:
        cnt += 1

    for nxt in [now * 2, now - 1, now + 1]:
        if 0 <= nxt < max_len:
            # 같을 때도 queue에 넣으면서 횟수를 저장하는 방식
            #
            if distance[nxt] == INF or distance[nxt] >= distance[now] + 1:
                distance[nxt] = distance[now] + 1
                q.append(nxt)



print(distance[K])
print(cnt)