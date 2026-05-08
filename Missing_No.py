#Find Missing Number in List 1 to N
def find_missing(lst, n):
    return n*(n+1)//2 - sum(lst)
