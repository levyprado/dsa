# Create the following pattern with provided n
# n = 5
# - - - - *
# - - - * *
# - - * * *
# - * * * *
# * * * * *

def star_pattern_v3(n):
    for i in range(n):
        row = ''
        for j in range(n-(i+1)):
          row += ' - '
        for k in range(i+1):
          row += ' * '
        print(row)

star_pattern_v3(5)