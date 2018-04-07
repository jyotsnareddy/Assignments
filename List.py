string1 = "{df{da}}"
x = string1.count("{")
y = string1.count("}")
if x == y:
    print "true"
else:
    print "false"
list1 = [1,1,2,3]
list1.append(4)
print(list1)
temp = (list1.pop(1))
print(temp)
list1.insert(2,8)
print(list1)
list1.remove(2)
print(list1)
list1.extend([1,2])
print(list1)
list1.reverse()
print(list1)
print(list1.index(1,3,6))
list1.sort()
print list1
print(sorted(list1))

string1 = "This is Jyotsna Enukonda"
print(string1.index("Jy"))
print(string1.count("E"))
print(string1.capitalize())
print(string1.center(2))
print(string1.endswith("s"))
print(string1.find("Jyo",9,15))
print(string1.swapcase())
print(string1[-7:])


