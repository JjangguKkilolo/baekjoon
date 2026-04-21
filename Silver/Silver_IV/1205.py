N, new_score, P = map(int, input().split())

if N > 0:
    rank = list(map(int, input().split()))
    if N == P and rank[-1] >= new_score:
        print(-1)
    else:
        rank.append(new_score)
        rank.sort(reverse=True)
        print(rank.index(new_score)+1)
        

elif N == 0:
    print(1)
