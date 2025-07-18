#balance : 초기 잔액을 설정하는 변수를 초기화해주세요
#금액은 여러분 마음대로 설정해주세요
#사용자로 부터 atm 기계에 사용 목적에 해당되는 기능 선택
balance=10000
while True:
    num=input("사용하실 기능을 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료): ")
    if num == '4':
        break
    if num == '1':#입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount=int(input("입금할 금액을 입력 해주세요:"))#str:5000 ->int ->
        if deposit_amount <= 0:
        balance += deposit_amount #balance=10000+deposit_amount
        print(f'입금하신 금액은{deposit_amount}원이고, 현재 잔액은{balance}원입니다')
    if num == '2':
        withdraw_amount=int(input("출금할 금액을 입력 해주세요:"))
        withdraw_amount=min(balance,withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은{withdraw_amount}원이고, 현재 잔액은{balance}원입니다')
    if num == '3':
        pass

print(f'서비스를 종료합니다. 현재 잔액은{balance}입니다')