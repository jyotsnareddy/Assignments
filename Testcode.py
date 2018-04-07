x = [2,1,4,3]
c = [2,1,4,3]
temp = 0
position = input("please enter the position number")
for iter in x :
    while c[position] != 0:
        i=0
        for each in c:
            if each != 0:
                c[i]=each - 1
                i=i+1
                if c[position] != 0:
                    temp = temp + 1
            elif c[position] != 0:
                i=i+1
        break
temp = temp +1
print "total time taken is:: " , temp
