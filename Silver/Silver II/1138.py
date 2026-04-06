N = int(input())
jul = list(map(int, input().split()))
zari = []
for i in range(N-1, -1, -1):
    zari.insert(jul[i],i+1)
    

print(*zari)    
    
