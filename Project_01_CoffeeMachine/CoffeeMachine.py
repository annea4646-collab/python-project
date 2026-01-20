MENU={
    'espresso':{
        'ingredients':{
            'water':50,
            'milk' :0,
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
profit = 0 
resources={
    'water':300,
    'milk':200,
    'coffee':100,
}



def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f'죄송합니다. {item}가 충분하지 않습니다')
            return False
    return True

    # ''' 주문을 만들 수 있을 때는 True를 반환하고, 재료가 부족할 경우에는 False를 반환한다 '''


def process_coins():
    print('동전을 투입해주세요')
    print()
    total = int(input('쿼터($0.25) 개수 : ')) * 0.25
    total += int(input('다임($0.10) 개수 : ')) * 0.10
    total += int(input('니켈($0.05) 개수 : ')) * 0.05
    total += int(input('페니($0.01) 개수 : ')) * 0.01
    print()
    return total

    # ''' 투입된 동전으로 계산된 총액을 반환한다 '''


def is_transaction_sucessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 3)
        if change > 0:
            print(f'거스름돈 ${change}를 돌려드립니다')
            print()
        global profit
        profit += drink['cost']
        return True
    else:
        print('죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다')
        return False
    
    # ''' 지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 반환한다 '''


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]     
    print(f'여기 {drink_name}가 나왔습니다. 즐기세요!')

    # ''' 자원(resources)에서 필요한 재료(ingredients)를 차감한다 '''

prompt ="""
☕ 어떤 음료를 원하시나요? (영문 입력)
-------------------------------------
에스프레소  espresso        $1.5
라떼        latte           $2.5
카푸치노    cappuccino      $3.0
-------------------------------------
보고서출력  report

>>> """

while True:
    print(prompt)
    cho=input()
    print()
    
    if cho in MENU:
        drink = MENU[cho]

        if is_resource_sufficient(drink['ingredients']):
            money = process_coins()
            if is_transaction_sucessful(money, drink['cost']):
                make_coffee(cho, MENU[cho]['ingredients'])
    elif cho == 'report':
        print(f"남은자원\n- 물:\t{resources['water']}ml\n- 우유:\t{resources['milk']}ml\n- 커피:\t{resources['coffee']}g\n\n현금:\t${profit}")
    
    elif cho == 'off':
        print('프로그램을 종료합니다')
        break
    else: 
        print('⚠️ 잘못 입력하셨습니다. 다시 입력해주세요.')
print()


