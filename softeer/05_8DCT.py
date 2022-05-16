lst = list(map(int, input().split()))

ascending_list = sorted(lst)
descending_list = ascending_list[::-1]

if lst == ascending_list:
    print('ascending')
elif lst == descending_list:
    print('descending')
else:
    print('mixed')