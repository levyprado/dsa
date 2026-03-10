# Create a star pattern with provided n
# n = 4
# * * * *
# * * * *
# * * * *
# * * * *

def star_pattern(n):
    for i in range(n):
        row = ''
        for j in range(n):
            row += ' * '
        print(row)

star_pattern(4)

# Create a star pattern with provided n
# n = 4
# *
# * *
# * * *
# * * * *

def star_pattern_v2(n):
    for i in range(n):
        row = ''
        for j in range(i+1):
            row += ' * '
        print(row)


star_pattern_v2(4)

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
            # 1
            # 2 2
        print(row)

number_pattern_v2(5)