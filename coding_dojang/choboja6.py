# 181번
# apart = [["101호", "102호"],["201호", "202호"],["301호", "302호"]]

# 182번
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 183번
# stock = {"시가":[100,200,300],"종가":[80,210,330]}

# 184번
# stock = {"10/10":[80,110,70, 90],"10/11":[210,230,190,200]}

# 185번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")

# 186번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for col in row:
#         print(col, "호")

# 187번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col, "호")

# 188번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#         print("-"*5)

# 189번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#     print("-"*5)

# 190번
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
# print("-"*5)

# 191번
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for col in row:
#         print(col*1.00014)

# 193번
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#     for col in row:
#         result.append(col*1.00014)
# print(result)

# 194번
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for line in data:
#     sub = []
#     for col in line:
#         sub.append(col*1.00014)
#     result.append(sub)
# print(result)

# 195번 
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for line in ohlc[1:]:
#     print(line[3])

# 196번
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for line in ohlc[1:]:
#     if line[3] > 150:
#         print(line[3]) 

# 197번
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for line in ohlc[1:]:
#     if line[3] >= line[0]:
#         print(line[3])

# 198번
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for line in ohlc[1:]:
#     volatility.append(line[1]-line[2])
# print(volatility)

# 199번
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for line in ohlc[1:]:
#     if line[3] > line[0]:
#         print(line[1]-line[2])

# 200번
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# profit = 0
# for line in ohlc[1:]:
#         profit +=(line[0]-line[3])
# print(profit)

# 201~203번
# def print_coin():
#         print("비트코인")
# for i in range(100):
#         print_coin()

# 204번
# def print_coin():
#         for i in range(100):
#         print("비트코인")
# print_coin()

# 215번
# def print_with_smile(string):
#     print(string + ":D")

# print_with_smile("안녕")

# 216번
# def print_upper_price(price):
#     print(price * 1.3)
# print_upper_price(3000)

# 217번
# def print_sum(a,b):
#     print(a+b)
# print_sum(3,5)

# 219번
# def print_arithmetic_operation(a, b):
#     print(a,"+",b,"=",a+b)
#     print(a,"-",b,"=",a-b)
#     print(a,"*",b,"=",a*b)
#     print(a,"/",b,"=",a/b)
# print_arithmetic_operation(3, 4)

# 220번
# def print_max(a,b,c):
#     max_val = 0 
#     if a > max_val:
#         max_val = a
#     if b > max_val:
#         max_val = b
#     if c > max_val:
#         max_val = c
#     print(max_val)
# print_max(3,2,0)

# 221번
# def print_reverse(string):
#     print(string[::-1])
# print_reverse("python")

# 222번
# def print_score(score):
#     print(sum(score)/len(score))
# print_score ([1, 2, 3])

# 223번
# def print_even(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i)
# print_even ([1, 3, 2, 10, 12, 11, 15])

# 224번
# def print_keys(dict):
#     for keys in dict.keys():
#         print(keys)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225번
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(dict,date):
#     print(dict[date])
# print_value_by_key  (my_dict, "10/26")

# 226번
# def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for x in range(chunk_num) :
#         print(line[x * 5: x * 5 + 5])

# print_5xn("아이엠어보이유알어걸")

# 227번
# def printmxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num+1) :
#         print(line[x * num: x * num + num])
# printmxn("아이엠어보이유알어걸", 3)

# 228번
# def calc_monthly_salary(num):
#     month = int(num/12)
#     print(month) 
# calc_monthly_salary(12000000)

# 232번
# def make_url(string):
#     a = "www."+string+".com"
#     return a
# print(make_url("naver"))

# 233번
# def make_list(string):
#     list = []
#     for i in string:
#         list.append(i)
#     return list
# def make_list(string):
#     return list(string)
# print(make_list("abcd"))

# 234번 
# def pickup_even(list):
#     my_list = []
#     for i in list:
#         if i % 2 == 0:
#             my_list.append(i)
#     return my_list
# print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235번
# def convert_int(string):
#     return int(string.replace(',',''))
# print(convert_int("1,234,567"))

# 241번
