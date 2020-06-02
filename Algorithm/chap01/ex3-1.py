

def name_match(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

    


name = ["Tom", "Jerry", "Mike"]
name_match(name)
name2 = ["Tom", "Jerry", "Mike", "John"]
name_match(name2)
