# Create the following pattern with provided n
# n = 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def number_pattern(n):
    for i in range(n):
        row = ''
        for j in range(i+1):
            row += ' ' + str(j+1) + ''
        print(row)

number_pattern(5)