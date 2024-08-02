'''
유용한 문자열 함수
  개수 -len(), 중복된 문자 개수 -count()
  대문자 변환-upper(),lower()
  문자열을 잘라서 리스트로 반환
  특정한 문자를 변경-replace
'''
f = '바나나'
print(len(f))
print(len("banana"))

# dupl_count = "banana"
# print(count("dupl_count"))
# print(banana,count("a"))

upper_case = "Hello".upper()
lower_case = "Hello".lower()
print(upper_case,lower_case)

friends = "존 루나 제리"
print(friends.split(" "))

alpha = "a:b:c:d"
print(alpha.split(":"))

email = "codingOn@spreatics.com"
print(email.split("@"))

#replace()
msg = "Hello Python"
print(msg.replace("python","C++"))