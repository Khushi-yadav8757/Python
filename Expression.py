# What is list comprehension vs generator expression?
#Ans:-

List comprehension → creates list in memory.
Generator expression → creates iterator (lazy).

lst = [x*x for x in range(5)]   # list
gen = (x*x for x in range(5))   # generator
