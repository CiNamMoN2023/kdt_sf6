vending_machine = ['게토레이','레쓰비','생수','이프로']

while True:
    print("===========RESTART")
    beverage = str(input("마시고 싶은 음료?"))
    if beverage in vending_machine:
        vending_machine.remove(beverage)
        print(beverage,"드릴게요")
        print("남은음료는",vending_machine)
    else:
        print(f'{beverage}는 지금 없네요')


