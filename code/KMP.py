def improvedInitNext(p, m):
    m = len(p)
    next[0] = -1
    i = 0
    j = -1
    while i < m:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

def KMP(p, t, k, m, n):
    m = len(p)
    n = len(t)
    improvedInitNext(p, m)
    i = k
    j = 0
    cnt = 0
    while j < m and i < n:
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        cnt += 1
        i += 1
        j += 1
    if j == m:
        return i-m, cnt
    else:
        return i, cnt

next = [0] * 50
text = 'ababacabcbababcacacaababca'
pattern = 'ababca'
tLen = len(text)
pLen = len(pattern)
k = 0
cnt = 0
while True:
    ans = KMP(pattern, text, k, pLen, tLen)
    k = ans[0] + pLen
    cnt += ans[1]
    if k <= tLen:
        print('패턴 발견 위치 :', ans[0])
    else:
        break
print('비교 횟수 :', cnt)
print('스트링 탐색 종료')