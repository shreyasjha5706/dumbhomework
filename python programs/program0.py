n = int(input("How many rows woud you like to print? (int): "))
for i in range(1, n+1):
    print("*"*i)

n = int(input("How many rows for the descending pattern? (int): "))
for i in range(n, 0, -1):
    print("*"*i)