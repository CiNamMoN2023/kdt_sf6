#연산자(operator)
#산술 연산 +,-,*,/,//(몫),%(나머지),**(거듭제곱)
n1 = 10
n2 = 20

print(n1+n2)#30
print(n1-n2)#-10
print(n1*n2)#200
print(n1//n2)#0
print(n1%n2)#10
print(n1**n2)#10^20


#산술 연
sum = n1+n2
sub = n1-n2
mul = n1 *n2
div = n1/n2

print(sum)
print(sub)
print(mul)
print(div)

#30개의 빵을 4명이 나눠 가질떄 몫과 나머지
bread = 30
person = 4

print("빵의개수:",bread//person)
print("남은 빵의 개수:",bread%person)

quotient = bread//person
remainder = bread%person

print("빵의개수:",quotient)
print("남은 빵의 개수:",remainder)
