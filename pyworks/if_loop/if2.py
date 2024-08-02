#실습 1
speed = 60
if speed >= 50:
    print(f'속도 위반입니다. ')
else:
    print(f'규정 속도 준수!!')
print(f'주행 속도는{speed}입니다.')


speed = float(input("주행속도를 입력하세요: "))
if speed >= 50:
    print(f'속도 위반입니다. ')
else:
    print(f'규정 속도 준수하고 계십니다!!')
print(f'주행 속도는{speed:.2f}입니다.')