#balance : 초기 잔액을 설정하는 변수를 초기화해주세요
#금액은 여러분 마음대로 설정해주세요
#사용자로 부터 atm 기계에 사용 목적에 해당되는 기능 선택
balance=10000
receipts=[]

while True:
    num=input("사용하실 기능을 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료): ")
    if num == '4':
        break
    if num == '1':#입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount=int(input("입금할 금액을 입력 해주세요:"))#str:5000 ->int ->
        if deposit_amount >= 0:
            balance += deposit_amount #balance=10000+deposit_amount
        print(f'입금하신 금액은{deposit_amount}원이고, 현재 잔액은{balance}원입니다')
        receipts.append(('입금내역',deposit_amount,balance))
    if num == '2':
        withdraw_amount=int(input("출금할 금액을 입력 해주세요:"))
        withdraw_amount=min(balance,withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은{withdraw_amount}원이고, 현재 잔액은{balance}원입니다')
        receipts.append(('출금내역',("출금금액",withdraw_amount),("현재잔액",balance)))
    if num == '3':
        if receipts:
            for i in receipts:
                print(f"{i[0]}: {i[1]}원 | 잔액:{i[2]}")
        else:
            print("영수증 내역이 없습니다.")

print(f'서비스를 종료합니다. 현재 잔액은{balance}입니다')