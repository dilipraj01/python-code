str = ""
inp = input("Enter any world: ")
cot = 0
count = 0
vowels = ["a","e","i","o","u"]
inpt = list(inp)
inpt1 = list(inp)           #  I am using 2 duplicate lists bcz if the condition is true it will delete the position of the element
for a in range(0,len(inp)):
    for b in range(a+1,len(inp)):
        if inp[a] == inp[b]:
            cot += 1
            a = b
            b = a + 1  # to compare all element one after another
        else:
            a = b
            b = a+1
        if a == len(inp)-1:
            break
    break
if cot > 0:  # it tells if they occur one after another
    for m in inpt:
        str += m
    print(str)

else:
    for k in range(0, len(inpt1)):
        for l in range(0, len(vowels)):
            if inpt1[k] == vowels[l]:
                inpt.remove(inpt1[k])      # duplication comparison

    for m in inpt:
        str += m
    print(str)
