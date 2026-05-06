import sys

def solve():
    N = int(sys.stdin.readline().strip())
    

    for r in range(2 * N):
        c1 = (2 * N - 1) - r

        if r < N:
            c2 = 3 * N - r
        else:
            c2 = N + 1 + r
            
        if r < N:
            c3 = 3 * N + 2 + r
        else:
            c3 = 5 * N + 1 - r
        
        line = [' '] * (c3 + 1)
        
        line[c1] = '*'
        line[c2] = '*'
        line[c3] = '*'

        print("".join(line))

if __name__ == '__main__':
    solve()
