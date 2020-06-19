# my_variable = ()
# print(type(my_variable))

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")


# my_tuple = (1, )
# print(type(my_tuple))

# t = 1, 2, 3, 4
# print(type(t))

# t = ('a', 'b', 'c')
# print(t)
# t = ('A', 'b', 'c')
# print(t)

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)
# print(data)

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(data)

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# data = tuple(range(2, 100, 2))
# print(data)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(valid_score)

# ice = {"메로나":1000, "폴라포": 1200, "빵빠레":1800}
# print(ice)
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print(ice["메로나"])

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice["메로나"]= 1300
print(ice["메로나"])

del ice["메로나"]  
print(ice)