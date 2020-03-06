def total(basket_discounts, items):
    price_after_basic_dis = []
    for item in items:
        price_after_basic_dis.append(item[1] - item[1]*item[2]/100)
        
    total_price_after_basic = sum(price_after_basic_dis)
    
    basket_dis_slabs = {}
    for basket_discount in basket_discounts:
        basket_dis_slabs[basket_discount[0]] = basket_discount[1]
        
    basket_dis_slabs = dict( sorted(basket_dis_slabs.items(), key=operator.itemgetter(0),reverse=True))
    
    final_price = []
    
    for slab in basket_dis_slabs.keys():
        if total_price_after_basic >= slab:
            for i, basic_price in enumerate(price_after_basic_dis):
                priceitem_basketdis = basic_price - basic_price*basket_dis_slabs[slab]/100
                max_dis_item_price = items[i][1] - items[i][1]*items[i][3]/100
                
                if priceitem_basketdis>= max_dis_item_price:
                    final_price.append(priceitem_basketdis)
                else:
                    final_price.append(max_dis_item_price)

            break;
            
        
    return sum(final_price)

m = int(input().strip())
basket_discounts = []
for i in range(m):
    (amount, discount) = input().strip().split()
    basket_discounts.append((int(amount), int(discount)))

n = int(input().strip())
items = []
for i in range(n):
    (name, price, base_discount, max_discount) = input().strip().split()
    items.append((name, int(price), int(base_discount), int(max_discount)))

print("%.02f" % total(basket_discounts, items))