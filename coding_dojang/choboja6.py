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
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for line in ohlc[1:]:
    volatility.append(line[1]-line[2])
print(volatility)

# 199번
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

