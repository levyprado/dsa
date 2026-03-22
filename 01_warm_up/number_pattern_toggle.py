# n = 5
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1

def number_pattern_toggle_refreshed(n):
  toggle = 1
  for i in range(n):
    row = ''
    for j in range(i+1):
      row += str(toggle)
      toggle = 1 - toggle
    print(row)

number_pattern_toggle_refreshed(5)