#자리배치도
#고객수 - customer, 좌석열- column, 행 -row
#나눴을때 나머지가 있으면 행 수가 변함
customer = int(input("고객 수 입력:")) #5행
column = int(input("좌석 열 수 입력:")) 4 #4열
if customer % column== 0:
    row = customer//column#몫
else:
    row = customer//column + 1 #나머지가 있으면 행이 늘어남

for i in range(0,row):
    for j in range(1,column +1):
        num = i * column + j
        if num > customer:
            break
        print(num,end = ' ')
    print()

# 예를 들어 5행 이라고 해보자
# 그럼
#
# column 4열이라고 해보자
#
#
# for i in range(0,5):
#     for j in range(1,5):
#         num = i * column + j #  0 * 4 +1
#         if num > customer:
#             1> customer :
#             ㅠㄱㄷ마