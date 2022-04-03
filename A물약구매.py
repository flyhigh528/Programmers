def potion_shop():
    input_cnt = 0
    item_cnt = 1
    potion_price = []
    sale_cnt = 0
    buy_cnt = 0
    price = 0

    while item_cnt != buy_cnt:
        info = input("상점 정보 입력 : ")
            
        #info 처리    
        if input_cnt == 0:
            item_cnt = int(info)
            input_cnt += 1
        elif input_cnt == 1:
            potion_price = info.split()
            potion_price = [int (i) for i in potion_price]
            input_cnt += 1
        elif input_cnt > 1 and sale_cnt == 0:
            sale_cnt = int(info)
        else:
            # 할인이 원래 가격보다 크면 1 아니면 할인 가격적용
            if int(info.split()[1]) >= potion_price[int(info.split()[0])-1] :
                potion_price[int(info.split()[0])-1] = 1
            else:
                potion_price[int(info.split()[0])-1] = potion_price[int(info.split()[0])-1] - int(info.split()[1])
            sale_cnt -= 1
                
        # 물약 구매
        if input_cnt > 1 and sale_cnt == 0:
            price = price + min(potion_price)
            potion_price[potion_price.index(min(potion_price))] = 1001
            buy_cnt += 1

        print('아이템갯수:{},구매갯수{}, 총구매금액{}, 아이템가격{}'.format(item_cnt, buy_cnt, price, potion_price))
    
    print(price)

if __name__ == '__main__':
    potion_shop()