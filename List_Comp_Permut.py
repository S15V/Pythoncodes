
if __name__ == '__main__':
    x = int(input('Enter x'))
    y = int(input('Enter y'))
    z = int(input("Enter z"))
    n = int(input('Enter n'))

    res = [[i, j, k] for i in range(0,x)
                     for j in range(0,y)
                     for k in range(0,z) if (i+j+k)!=n]

    print(" ",res)
