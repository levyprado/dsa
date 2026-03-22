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