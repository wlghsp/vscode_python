# 131번 
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
# 132번 
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")
# 133번 
# 변수 = "A"
# print(변수)
# 변수 = "B"
# print(변수)
# 변수 = "C"
# print(변수)

# 134번
# 변수 = "A"
# print("출력:", 변수)
# 변수 = "B"
# print("출력:", 변수)
# 변수 = "C"
# print("출력:", 변수)

# 135번
# b = "A".lower()
# print("변환:", b)
# b = "B".lower()
# print("변환:", b)
# b = "C".lower()
# print("변환:", b)

# 136번, # 137번
# for i in [10, 20, 30]:
#     print(i)
# 138번 
# for i in [10,20,30]:
#     print(i)
#     print("------")
# 139번 
# print("++++")
# for i in [10, 20, 30]:
#     print(i)

# 140번 
# for i in [10,20,30,40]:
#     print("------")

# 141번 
# 리스트 = [100, 200, 300]
# for i in 리스트:
#     print(i + 10)

# 142번
# for i in 리스트:
#     print("오늘의 메뉴:"+i) 
# 리스트 = ["김밥", "라면", "튀김"]
# for i in 리스트:
#     print("오늘의 메뉴:", i)
# 143번
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트:
#     print(len(i))

# 144번
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i, len(i))

# 145번
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0])

# 146번
# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print("3 x",i)

# 147번
# 리스트 = [1, 2, 3]
# for i in 리스트:
#     # print("3 x", i, "=",3 *i)
#     print("3 x {} = {}".format(i, 3 * i))

# 148번
# 리스트 = ["가", "나", "다", "라"]

# for i in 리스트[1:]:
#     print(i)
# 149번
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::2]:
#     print(i)

# 150번
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::-1]:
#     print(i)

# 151번
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i <0:
#         print(i)

# 152번
# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 153번
# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#     if i < 20 and i % 3 == 0:
#         print(i)

# 154번
# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) > 3:
#         print(i)

# 155번
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)

# 156번    
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.islower():
#         print(i)

# 157번
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0].upper()+ i[1:]) 

# 158번
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     이름 = i.split(".")[0]
#     print(이름)

# 159번
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     split = i.split(".")
#     if split[1] == "h":
#         print(i) 

# 160번
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     split = i.split(".")
#     if split[1] == "h" or split[1] =="c":
#         print(i) 

# 161번
# for i in range(0,100):
#     print(i)

# 162번
# for i  in range(2002, 2051, 4):
#     print(i)

# 163번
# for i in range(3, 31, 3):
#     print(i)

# 164번
# for i in range(100):
#     print(99-i)

# 165번
# for num in range(10) :
#     print(num / 10)

# 166번
# for i in range(1, 10):
#     print(3,"x", i, " = ",3*i)

# 167번
# num = 3
# for i in range(1,10,2):
#     print (num, "x", i, " = ", num * i)

# 168번
# sum = 0
# for i in range(1, 11):
#     sum += i
# print("합:",sum)

# 169번
# sum = 0
# for i in range(1,11,2):
#     sum += i
# print("합:",sum)

# 170번
# result= 1
# for i in range(1,11):
#     result = result * i
# print(result)

# 171번
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(price_list[i])

# for i in range(len(price_list)):
#     print(price_list[i])

# 172번
# price_list = [32100, 32150, 32000, 32500]
# for i, data in enumerate(price_list):
#     print(i, data)

# 173번
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list)-1)-i, price_list[i])

# 174번
# price_list = [32100, 32150, 32000, 32500]
# for i in range (1, len(price_list) ) :
#     print(100 + i - 1* 10, price_list[i])

# 175번
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)-1):
#     print(my_list[i], my_list[i+1])
# for i in range(1, len(my_list)):
#     print(my_list[i-1], my_list[i])


# 176번
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i], my_list[i+1],my_list[i+2])

# 177번
# my_list = ["가", "나", "다", "라"]
# for i in range(1, len(my_list)):
#     print(my_list[-i], my_list[-i-1])

# 178번 
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#     print(my_list[i+1]-my_list[i])

# 179번 
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#     print(abs(my_list[i]+my_list[i+1]+my_list[i+2])/3)

# 180번
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []

# for i in range(len(low_prices)):
#    volatility.append(high_prices[i]-low_prices[i])

# print(volatility)

