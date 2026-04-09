import sys
input = sys.stdin.readline

N,G = input().split()
N = int(N)
nick = set()
for i in range(N):
    name = input()
    nick.add(name)
    if G == 'Y':
        game = len(nick)//1

    if G == 'F':
        game = len(nick)//2
            
    if G == 'O':
        game = len(nick)//3

print(int(game))
