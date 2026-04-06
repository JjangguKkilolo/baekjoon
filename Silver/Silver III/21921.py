N, X = map(int, input().split())
visit = list(map(int, input().split()))
visit_sum = 0
count_max = 1
for i in range(X):
    visit_sum += visit[i]

result = visit_sum

for i in range(X,N):
    visit_sum += visit[i] - visit[i-X]

    if result < visit_sum:
        result = visit_sum
        count_max = 1
    elif result == visit_sum:
        count_max +=1
    
    
if result>0:
    print(result)
    if count_max>0:
        print(count_max)
else:
    print('SAD')


