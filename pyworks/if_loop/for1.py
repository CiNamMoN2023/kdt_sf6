'''
for i in list:
'''
# range()
a = range(10)
b = range(1,11)
c = range(1,11,2)
#for 문 1부터 10까지 출력
for i in range(1,11):
    print(i, end = " ")# 주의! 리스트가 아니고 i의 값이 변하는 것임.

for i in range(1,101):
    print(i, end = " ")

#for 문 -1부터 10까지 더하기(합계)
total = 0 #합계를 저장할 변수-0으로 초기화 하는 동작
for i in range(1,11):
    total = total + i
    print("i = ",i,"total =",total)
print(total)#for 문을 빠져나오고 출력