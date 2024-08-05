#구구단 출력- 3단만
# dan = 3
# for i in range(1,10):
#     print(f'{dan}*{i} = {dan*i}')

# #구구단 출력 원리
# for i in range(1,5): # i = 1,2,3,4
#     for j in range(1,5):# j = 1,2,3,4
#         print("가", end = " ")
#     print() #행바꿈
# '''
# i = 1
#     j =1,
#     j =2,
#     j =3,
#     j =4,
# i = 2
# '''
# #전체 구구단(중첩 for문)
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}*{j} = {i*j}')
#     print()
#
#별 찍기(행은 그대로 4행이고, 열이 변해야하므로
# for i in range(1,5):
#     for j in range(1,i+1):  #i가 1 이면 j 가 0이되잔수
#         print("*",end = '')
#     print()

# #파이썬의 단일 for
# for i in range(1,5):
#     print("*" * i )
#

#이등변 거꾸로 삼각형
# for i in range(1,5):
#     for j in range(1,6-i):
#         print("*",end = '')
#     print()

for i in range(1,5):
    print("*" * (5-i) )

#이등변 삼각형 오른쪽으로 붙여 -공백문자세야함

for i in range(1,5):
    print(" "*(4-i) + "*" *i) # i = 1일때 공백3개 * 1개


