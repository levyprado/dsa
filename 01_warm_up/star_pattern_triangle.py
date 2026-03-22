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