N, K = map(int,input().split())
L = list(input())

eat_people = 0
         
for i in range(N):
    if L[i] == 'P':
        start = max(0,i-K)
        end = min(N,i+K+1)
        for j in range(start, end):
            if L[j] == 'H':
                L[j] = 'O'
                eat_people +=1
                break

print(eat_people)
            
