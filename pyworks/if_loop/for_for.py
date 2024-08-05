#숫자가 연속으로 증가하는 알고리즘
for i in range(0,4):
    for j in range(1,5):
        print(i* 4 +j,end ='')
    print()
#1234
#1234
#1234
#1234



#우리가 원하는 건
'''
1234
5678
9101112
13141516
'''

#이번엔 1부터 15까지만 자리배치
for i in range(0,4):
    for j in range(1,5):
        num = i *4 +j
        if num>15:
            break
        print(num,end =' ')
    print()