#실습 1
# input = int(input("어디까지 계산할까요?:"))
# for i in range(input):
#     input = input + i
#     print(input)
# print(input)

#다른 방법
# num = int(input("몇까지의 합을 계산할까요"))
# total = 0
# for i in range(1,num+1):
#     total += i
# print(f'1부터 {num}까지의 합: {total}')

#실습1 추가문제: 홀수의 합계를 구하쇼
input = int(input("숫자를 입력하세요:"))
for i in range(input):
    if i %2 == 1:
        i = i + input
print(i)

#실습2
# input = int(input("숫자를 입력하세요:"))
# for i in range(input):
#     input = input - i
#     print(input)
# #print("발사",total)
# n= int(input("몇 초"))
# for i in range(n,0,-1):
#     print(i,end = ' ')
# print("발사")
#
# #실습 3
# a = int(input("몇 단을 출력할까요"))
# count = 0
# for b in range(1,10):
#     b = b + count
#     print(f"{a}*{b} ={a*b}")