def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))




