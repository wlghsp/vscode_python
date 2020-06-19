# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",","")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))

# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)

# ticker = "BTC_KRW"
# print(ticker.lower())

# a = "hello"
# a = a.capitalize()
# print(a)

# words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
# print(words)
# print([len(word) for word in words])

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))
# print(file_name.endswith(("xlsx", "xls")))


# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))

# a = "hello world"
# a = a.split()
# print(a)

# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)

# date = "2020-05-01"
# date = date.split("-")
# print(date[0])
# print(date[1])
# print(date[2])

# data = "039490     "
# data = data.rstrip()
# print(data)

movie_rank = ["닥터 스트레인지", "슈퍼맨", "슈플릿","배트맨" ]

# movie_rank.append("배트맨")
# movie_rank.insert(1, "슈퍼맨")

# del movie_rank[2]
# del movie_rank[2]

# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# langs = lang1+ lang2
# print(langs)

# nums = [1, 2, 3, 4, 5, 6, 7]
# print(max(nums))
# print(min(nums))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# average = sum(nums)/len(nums)
# print(average)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort(reverse=True)
# print(data)

