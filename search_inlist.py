lt =[1,2,3,4,5,6,7,8]

for x in lt:
    print(x,end=" ")
print()

x= int(input('enter the element to search in the list'))

if x in lt:
    print('the element exists in the list')
else:
    print('no such elements in the list')

