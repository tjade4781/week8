def chop(lst):
    del lst[0]
    del lst[-1]


def middle(lst):
    new = lst[1:]
    del new[-1]
    return None


my_list = ['Jade', 'David', 'James', 'Gerald']
my_list2 = ['Jade', 'David', 'James', 'Gerald']

chop_list = chop(my_list)
print(my_list)
print(chop_list)

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)
