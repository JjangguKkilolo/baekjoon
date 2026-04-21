import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

M = int(input())

for i  in range(M):
    cursor = input().split()
    
    match cursor[0]:
        case "L":
            if left_stack:
                right_stack.append(left_stack.pop())
            
        case "D":
            if right_stack:
                left_stack.append(right_stack.pop())
        case "B":
            if left_stack:
                left_stack.pop()
        case "P":
            left_stack.append(cursor[1])
        case _:
            print("error")

print("".join(left_stack+right_stack[::-1]))
        
        
