# Create the following pattern with provided n
# n = 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def number_pattern_v2(n):
    for i in range(n):
        row = ''
        for j in range(i+1):
            row += ' ' + str(i+1) + ''
        print(row)

number_pattern_v2(5)