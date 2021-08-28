lt =[1,2,3,4,5,6,7,8]

for x in lt:
    print(x,end=" ")
print()

first = lt[0]
last = lt[-1]
print(first)
print(last)

first,last= last, first

for x in lt:
    print(x,end=" ")
print()
