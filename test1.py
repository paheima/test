# import datetime
# import re
#
# a = '华创证券'
#
# b = '华创'
#
# if b in a:
#     print('1')
#
#
# R_rate = '2023-6-15'
# # R_rate = datetime.datetime.strptime(R_rate, '%Y-%m-%d')
# print(R_rate)
#
# RN_time = datetime.datetime.now()
# print(RN_time)
#
# day = 1
# tmp = datetime.timedelta(days=day)
#
# print(R_rate + tmp)

# print(isinstance(R_rate, str))

# text = ['98.6833', '1000', '其他']
# prices = re.findall(r"^\d+\.\d+$|^\d+$", text)
#
# print(prices)

# p = '98.5'
# print(eval(p))
# if 20.0 <= float(p) < 200.0 and isinstance(int(p), float):
#     print(1)


# List = []
# A = {'A': 1, 'B': 2}
# List.extend(A.keys())
# print(List)
# for i in A.items():
#     print(i)

# lst1 = ['A', 'B', 'C', 'A']
# c1 = lst1.count('A')
# print(c1)

A = 0
B = 2
print(A % B)
