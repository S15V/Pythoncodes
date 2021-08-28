
def Kangaroo(x1,x2,v1,v2):
    for n in range(0,10000):
        if x1+(n*v1)==x2+(n*v2) and v2!=v1:
            x='YES'
            return x
    else:
        y='NO'
        return y

if __name__=='__main__':
    print('\\\\\\\\\\\\\Kangaroo Question/////////////')
    x1 = int(input('Enter the position of kangaroo1'))
    x2 = int(input('Enter the position of Kangaroo2'))
    v1 = int(input('Enter the speed of x1'))
    v2 = int(input('enter the speed of x2'))
    result = Kangaroo(x1,x2,v1,v2)
    print(result)
