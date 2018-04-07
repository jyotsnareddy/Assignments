Sides = [[2,4,5,6],[3,4,5,6],[6,7,8,4]]
output = []
for each in Sides:
    finalperi = 0
    for peri in each:
        finalperi = finalperi + peri
    output.append(finalperi)
print ("the perimeter of second list is " + str(output[1]))
print output
import urllib
print sys.path
