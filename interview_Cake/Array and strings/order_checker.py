# Given all three lists, write a function to check that my service is first-come, first-served. 
# All food should come out in the same order customers requested it.

Take_Out_Orders =  [1, 3, 5]
Dine_In_Orders =  [2, 4, 6]
Served_Orders =  [1, 2, 4, 6, 5, 3]

def Checker(take_out_orders, dine_in_orders, served_orders):
    if len(served_orders) == 0:
        return True

    if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
        return Checker(take_out_orders[1:], dine_in_orders, served_orders[1:])
    elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
        return Checker(take_out_orders, dine_in_orders[1:], served_orders[1:])
    else:
        return False
print(Checker(Take_Out_Orders, Dine_In_Orders, Served_Orders))

def Checker_two(take_out_orders, dine_in_orders, served_orders):

    take_out_orders_min = 0
    dine_in_orders_min = 0
    take_out_orders_max = len(take_out_orders) - 1
    dine_in_orders_max = len(dine_in_orders) - 1

    for orders in served_orders:

        if take_out_orders_min <= take_out_orders_max and orders == take_out_orders[take_out_orders_min]:
            take_out_orders_min += 1

        elif dine_in_orders_min <= dine_in_orders_max and orders == dine_in_orders[dine_in_orders_min]:
            dine_in_orders_min += 1

        else:
            return False

    return True

print(Checker_two(Take_Out_Orders, Dine_In_Orders, Served_Orders))