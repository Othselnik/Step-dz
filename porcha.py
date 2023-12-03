my_list = [10, 12, 22, 3, -5, 10]
min_v = 100
max_v = -100
for i in my_list:
    if i > max_v:
        max_v = i
    if i < min_v:
        min_v = i
print(min_v)
print(max_v)