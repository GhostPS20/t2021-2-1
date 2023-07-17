x = int(input())
for i in range(1, x+1):
    if x % 2 != 0:
        print(2*i-1, end=" ")

    else:
        a = 2 * (i-1) - 1
        if a > 0:
            print(a, end=" ")
