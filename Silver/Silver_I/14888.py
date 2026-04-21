N = int(input())
A = list(map(int,input().split()))

op_counts = list(map(int, input().split()))

max_a = -1e10
min_a = 1e10

def backtrack(index, current_total, ops):
    global max_a, min_a

    if index == N:
        max_a = max(max_a, current_total)
        min_a = min(min_a, current_total)
        return

    for i in range(4):
        if ops[i] > 0 :
            ops[i] -= 1

            if i == 0:
                backtrack(index+1, current_total + A[index], ops)
            elif i == 1:
                backtrack(index + 1, current_total - A[index], ops)
            elif i == 2:
                backtrack(index + 1, current_total * A[index], ops)
            elif i == 3:
                backtrack(index + 1, int(current_total / A[index]), ops)

            ops[i] += 1

backtrack(1, A[0], op_counts)
print(max_a)
print(min_a)
