MENU={
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee':18,
        },
        'cost':1.5,
    },
    'latte':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':24,
        },
        'cost':2.5,
    },
    'cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24,
        },
        'cost':3.0,
    }
}
# 현재까지 벌어들인 수익
profit = 0 

# 현재 남아 있는 재료의 양
resources={
    'water':300,
    'milk':200,
    'coffee':100,
}



def is_resource_sufficient(order_ingredients):
    # 주문에 필요한 재료가 충분한지 확인하는 함수, 주문을 만들 수 있을 때는 True를 반환하고, 재료가 부족할 경우에는 False를 반환한다

    for item in order_ingredients:
        # 재료가 부족한 경우 알림 메시지 출력
        if order_ingredients[item] > resources[item]:
            print(f'재료가 충분하지 않네요, 죄송합니다. {item}')
            return False
    return True



def process_coins():
    # 사용자가 넣은 동전의 총액을 계산하여 반환하는 함수
    print('동전을 넣어주세요')
    total = int(input('quarter 동전이 몇개인가요? ($0.25) ')) * 0.25
    total += int(input('dime 동전이 몇개인가요? ($0.1) ')) * 0.10
    total += int(input('nickle 동전이 몇개인가요? ($0.05) ')) * 0.05
    total += int(input('pennie 동전이 몇개인가요? ($0.01) ')) * 0.01
    return total




def is_transaction_sucessful(money_received, drink_cost):
    # 지불 금액이 음료 가격 이상인지 확인하는 함수, 지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 반환한다
    if money_received >= drink_cost:
        # 잔돈 계산
        change = round(money_received - drink_cost, 2)
        print(f'여기 있습니다. ${change} 잔돈입니다')

        global profit
        profit += drink_cost # 수익 추가
        return True
    else:
        # 금액이 부족하면 환불 메시지 출력
        print('금액이 충분하지 않네요. 환불합니다')
        return False
    
    


def make_coffee(drink_name, order_ingredients):
    # 음료를 만드는 함수, 자원(resources)에서 필요한 재료(ingredients)를 차감한다
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] # 재료 차감
    print(f'여기 있습니다. {drink_name} 맛있게 드세요!')




# 커피 머신이 켜져 있는지 확인하는 변수
is_on = True

while is_on:
    # 사용자 입력 : 음료 선택
    choice=input('무엇을 마시겠습니까? (espresso($1.5)/latte($2.5)/cappuccino($3.0)):')
    if choice == 'off':
        # 'off'를 입력하면 머신 종료
        is_on = False
    
    elif choice == 'report':
        #'report'를 입력하면 재료와 수익 상황 출력
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    else:
        # 사용자가 선택한 음료의 정보를 메뉴에서 가져오기
        drink = MENU.get(choice) # MENU[choice]

        if drink:
            # 재료가 충분한지 확인
            if is_resource_sufficient(drink['ingredients']):
                # 동전 입력 처리
                payment = process_coins()
                # 결제가 성공적이면 음료 만들기
                if is_transaction_sucessful(payment, drink["cost"]):
                    make_coffee(choice, drink['ingredients'])

        else: 
            # Exception Handling - 잘못된 입력 처리, 이게 없을 시 None을 출력. 시스템 다운될 수 있음
            print('잘못된 입력입니다. 다시 음료를 선택해주세요.')


