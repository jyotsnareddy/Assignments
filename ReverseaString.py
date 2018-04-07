def reverse(string1):

    if string1 is None:
        return string1

    if len(string1) <= 1:
        return string1

    return reverse(string1[1:]) + string1[0]

string1 = "Jyo 123"
print("The reverse of the string", string1, "is ", reverse(string1))
print(reverse("a"))
print(reverse(None))
