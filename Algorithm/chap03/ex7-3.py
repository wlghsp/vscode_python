
# 39번- Justin, 14번-John

def search_no(a, b, x):
    n = len(a)
    for i in range(0, n): 
        if x == a[i]:
            return b[i]
        
    return "?"


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

num = input("학생 번호는: ")
print(search_no(stu_no,stu_name, int(num)))