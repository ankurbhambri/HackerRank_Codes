'''
step 1 Sorting the nodes
step 2
    a pick the smallest edge
    b check if added edge forms cycle
    c if cycle not found then include the edge
step 3 repeat step 2 unless v-1 edge are included
'''


def find_parent_arr(prnt, part_arr=[]):
    if part_arr[prnt] == prnt:
        return prnt
    return find_parent_arr(part_arr[prnt], part_arr)


def kruskal(srt_arr, v, e):

    ip_arr = sorted(srt_arr, key=lambda i: i['wt'])
    op_arr = []
    part_arr = []

    # parent array
    for i in range(v):
        part_arr.append(i)

    count = 0
    i = 0
    while count != v - 1:
        crrnt_edge = ip_arr[i]
        # check we can add this edge in mst or not
        src_parent = find_parent_arr(crrnt_edge['src'], part_arr)
        des_parent = find_parent_arr(crrnt_edge['des'], part_arr)
        if src_parent != des_parent:
            op_arr.insert(count, crrnt_edge)
            part_arr[src_parent] = des_parent
            count += 1
        i += 1

    # Print array
    for i in range(v - 1):

        print(op_arr[i]['src'], op_arr[i]['des'], op_arr[i]['wt'])


# driver code
dd = [
    {'src': 0, 'des': 1, 'wt': 2},
    {'src': 1, 'des': 3, 'wt': 1},
    {'src': 0, 'des': 2, 'wt': 4},
    {'src': 4, 'des': 2, 'wt': 9},
    {'src': 4, 'des': 5, 'wt': 5},
    {'src': 3, 'des': 5, 'wt': 7},
    {'src': 4, 'des': 3, 'wt': 11},
    {'src': 2, 'des': 5, 'wt': 10},
    {'src': 0, 'des': 3, 'wt': 3},
    {'src': 2, 'des': 1, 'wt': 8},
    {'src': 2, 'des': 3, 'wt': 6},
]
dd1 = [
    {'src': 0, 'des': 1, 'wt': 4},
    {'src': 1, 'des': 2, 'wt': 2},
    {'src': 2, 'des': 3, 'wt': 10},
    {'src': 3, 'des': 4, 'wt': 6},
    {'src': 4, 'des': 5, 'wt': 1},
    {'src': 5, 'des': 6, 'wt': 5},
    {'src': 0, 'des': 6, 'wt': 2},
    {'src': 6, 'des': 3, 'wt': 7},
    {'src': 6, 'des': 4, 'wt': 4},
    {'src': 6, 'des': 5, 'wt': 8},
    {'src': 6, 'des': 1, 'wt': 1},
    {'src': 6, 'des': 2, 'wt': 3},
]
# vertices = 6
# edges = 11
kruskal(dd, 6, 11)

kruskal(dd1, 7, 12)
