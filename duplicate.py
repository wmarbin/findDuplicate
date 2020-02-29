def dupli(num):
    i = num[0]
    j = num[0]
    result = {}
    while True:
        print(i)
        i = num[i]
        j = num[num[j]]
        if i == j:
            break

    dummy1 = num[0]
    dummy2 = i
    while dummy1 != dummy2:

        dummy1= num[dummy2]
        dummy2= num[dummy2]
    return dummy1


print(dupli([4,5,2,2,3,1]))