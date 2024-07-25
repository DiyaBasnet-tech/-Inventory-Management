def dict_working_quant_sell(code,quantity,dict1):
        for i in dict1.keys(): #writing value in loop
            if code == i:
                cap = int(dict1[code][3])
                if cap == 0:
                    print("Apologies, but the laptop is currently unavailable due to being out of stock..")
                    print("\n")
                if quantity <= cap:
                    dict1[code][3] = cap - quantity
        print(dict1[code][3])
        return dict1
def dict_working_quant_buy(code,quantity,dict1):
    for i in dict1.keys():
        if code == i:
            cap = int(dict1[code][3])
            dict1[code][3] = cap + quantity
    print(dict1[code][3])
    return dict1

def loop_using_flag():
    condtion = True
    while condtion:
        ask = input("Do you want to continue(yes/no):  ")
        if ask.lower() == "no":
            flag= False
            condtion = False
            return flag
        elif ask.lower() == "yes":
            flag= True
            condtion = False
            return flag
        else:
            print("Enter appropriate values")

def add_list_for_total_price(dict2,code,quantity,list):
    name = dict2[code][1]
    c_name = dict2[code][2]
    price = int(dict2[code][3].replace("$", "")) #no multiplication error
    t_price = int(price * quantity)
    list.append([name, c_name, price, quantity, t_price])


def ship_transction(loop_1):
    if loop_1 != True:
        ship = input("Do you want to ship your laptop (y/n): ")
        if ship.lower() != "y" and ship.lower() != "n":
            print("Enter appropriate values.")
        return ship



