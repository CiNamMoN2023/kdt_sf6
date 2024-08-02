# 리스트 함수
# 추가 - 리스트.append(), 리스트.insert()
# 삭제 - 리스트.pop(), 리스트.remove()
# 정렬 = 리스트.sort(), 뒤집기 -reverse()
lower = ['a','b','c','d']

#'e'추가
lower.append('e')
print(lower)

#'e'삭제
lower.pop() #맨 뒤 삭제
print(lower)

#'b'와 'c'사이에 'e'추가
lower.insert(2,'e')
print(lower)

#'c'삭제
lower.remove('c')
print(lower)

# 정렬(오름차순)
lower.sort()
print(lower)

lower.reverse()
print(lower)


