import read
import operation
import write
import random
def main():
    read.title_for_welcome()
    loop = True #iteration 
    while loop == True:
        print("------------------------------------------------------------------------------------")
        print("You may choose your own option")
        print("------------------------------------------------------------------------------------")
        print("\n")
        print("Click 1 to buy laptops")
        print("Click 2 to sell laptops")
        print("Click 3 Exit")
        print("\n")
        print("------------------------------------------------------------------------------------")
        print("\n")
        while True:
            try:
                choice_for_details=int(input("Enter the choice to proceed: "))
            except ValueError:
                print("Recheck the input")
            else:
                break
        print("\n")

        if choice_for_details == 1:
            while True:
                name = (input("Provide your complete name: "))
                try:
                    if name.isalpha():
                        break
                    else:
                        raise ValueError("This string contains non-alphabetical characters.")
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                address = (input("Provide your address: "))
                try:
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("This string contains non-alphabetical characters.")
                except ValueError as e:
                    print(f"Error: {e}")

            test_try = True
            while test_try:
                try:
                    phone = int(input("Provide your phone number: "))
                except ValueError:
                    print("Please retry with a phone number in integer format, not as a string. ")
                else:
                    test_try = False
            loop_try = True
            list_for_store=[]
            while loop_try: #calling function
                cancel = True
                read.tabel_for_better_view()
                dict1=read.laptop_file_for_read()
                code_loop=True
                while code_loop:
                    try:
                        code = int(input("Input the product code of the laptop you wish to purchase: "))
                    except ValueError:
                        print("Use correct number")
                    else:
                        if code<=0 or code>len(dict1):
                            print("Error choose from above")
                        elif int(dict1[code][3]) == 0:
                            print("Laptop Out of Stocks")
                            cancel = False
                            code_loop=False
                        else:
                            code_loop=False
                if cancel:
                    quantity_loop=True
                    while quantity_loop:
                        try:
                            quantity= int(input("Input the qutatity of the laptop you want to purchase: "))
                        except ValueError:
                            print("Use correct number")
                        else:
                            if  int(dict1[code][3]) == 0:
                                print("Laptop Out of Stocks")
                            elif quantity<=0 or quantity>int((dict1[code][3])):
                                print("Error choose from above")
                            else:
                                quantity_loop=False
                        
                
                    dict2=operation.dict_working_quant_sell(code,quantity,dict1)
                    write.main_write(dict1)
                    list_for_store.append([code, quantity])
                loop_try =operation.loop_using_flag()
            if cancel:
                    random_int = random.randint(0,100)
                    ship = operation.ship_transction(loop_try)
                    write.bill_sell(name, address, phone, loop_try,list_for_store,random_int,ship,dict2)
                    write.bill_sell_text(name, address, phone, loop_try, list_for_store, random_int,ship,dict2)
            print("Thankyou for purchasing our laptops")
            print("\n")
        elif choice_for_details == 2:
            dict2 = read.laptop_file_for_read()
            while True:
                name = (input("Input your full name: "))
                try:
                    if name.isalpha():
                        break
                    else:
                        raise ValueError("This string contains non-alphabetical characters.")
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                address = (input("Input your address "))
                try:
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("This string contains non-alphabetical characters.")
                except ValueError as e:
                    print(f"Error: {e}")

            test_try = True
            while test_try:
                try:
                    phone = int(input("Input your phone number: "))
                except ValueError:
                    print("Please retry with a phone number in integer format, not as a string")
                else:
                    test_try = False
            loop_try_1 = True
            list_for_store = []
            while loop_try_1: #calling function 
                read.tabel_for_better_view()
                code_loop=True
                while code_loop:
                    try:
                        code = int(input("Input the product code of the laptop you wish to purchase: "))
                    except ValueError:
                        print("Use correct number")
                    else:
                        if code<=0 or code>len(dict2):
                            print("Error choose from above")
                        else:
                            code_loop=False
                quantity_loop=True
                while quantity_loop:
                        try:
                            quantity= int(input("Input the qutatity of the laptop you want to purchase: "))
                        except ValueError:
                            print("Use correct number")
                        else:
                            if quantity<=0:
                                print("Enter proper value")
                            else:
                                quantity_loop=False
                
                operation.dict_working_quant_buy(code, quantity, dict2)
                write.main_write(dict2)
                list_for_store.append([code,quantity])
                loop_try_1 = operation.loop_using_flag()
                random_int= random.randint(0, 100)
                write.bill_purchhase(name, address,phone,loop_try_1, list_for_store, random_int,dict2)
                write.bill_purchase_text(name, address, phone, loop_try_1, list_for_store, random_int, dict2)
            print("Thankyou for your purchase.")
            print("\n")
        elif choice_for_details == 3:
            loop = False
            print("We appreciate you using our system, Thankyou.")
            print("\n")
        else:
            print("Your option",choice_for_details,
              "appears to be opposing with our requirements")
            print("\n")
main()
