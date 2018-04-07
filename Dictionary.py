dict1 = {1: "munny", 2: "sunny", 3: "tillu"}
dict2 = {"pi": 3.14}
dict2[4] = "rithu"
# print(dict1.viewitems())
# print(dict1.values())
# print(dict1.copy())
#
x=dict2.copy()
print(x)
y=dict2
print(y)
print dict1[2]
print(len(dict1))
if 2 in dict1:
    print "yes"
