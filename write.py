import random 
import datetime #bill 


def main_write(dict2):
    file = open("/Users/diyabasnet/Desktop/22068105 Diya Basnet /elo.txt", "w")
    for i in dict2.values(): #loop in which dict2 values are separeted 
        file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(
            i[5])) 
        file.write("\n")
    file.close()


def bill_sell(name, address, phone, loop_1, list2, random, ship, dict2):
    print("\n")
    print("\n")
    print("\t \t \t \t \t Diya Electronics")
    print("\n")
    print("\t \t \t \t  Sinamangal,Kathmandu,| 014110585")
    print("\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("\t \t \t \tThank you for shopping. Our sincere hope is that you are pleased with your purchase!")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n")
    if loop_1 != True: #condition
        print("Bill no: ", random) 
        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
              datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("Name: ", name)
        print("Address: ", address)
        print("Phone: ", phone)
        total = 0
        for i in list2:
            lap_nam = dict2[i[0]][0]
            brand = dict2[i[0]][1]
            price = dict2[i[0]][2].replace("$", "") #easy in multiplication
            qunt = i[1] #op ko quatity lai call
            
            print("price: ", price)
            print("Laptop name: ", lap_nam)
            print("Quantity: ", qunt)
            print("Brand: ", brand)
            tprice = int(price) * int(qunt)
            print("Total price", tprice)
            total = total + int(tprice)
        if ship.lower() == "y":
            total = total + 250
            print("The total price with sphipping cost: ", total)
        elif ship.lower() == "n":
            print("The total price without sphipping cost:", total)
        else:
            print("Enter appropriate value")
        print("The total cost: ", total)


def bill_sell_text(name, address, phone, loop_1, list2, random, ship, dict2):
    with open(f"bill_{random}.txt", "w") as file:
        file.write("\n")
        file.write("\n")
        file.write("\t \t \t \t \t Diya Electronics")
        file.write("\n")
        file.write("\t \t \t \t  Sinamangal ,Kathmandu,| 014110585")
        file.write("\n")

        file.write(
            "----------------------------------------------------------------------------------------------------------")
        file.write("\t Thank you for choosing to shop with us! We hope you're happy with your purchase !!")
        file.write(
            "----------------------------------------------------------------------------------------------------------")
        file.write("\n")

        if loop_1 != True:
            file.write(f"Bill no: {random}\n")
            file.write(
                f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}\t\tDate: {datetime.datetime.now().strftime('%d/%m/%Y')}\n\n")
            file.write(f"Name: {name}")
            file.write(f"Address: {address}\nPhone: {phone}")
            total = 0
            for i in list2:
                lap_nam = dict2[i[0]][0] #calling index name 
                brand = dict2[i[0]][1]
                price = dict2[i[0]][2].replace("$", "")
                qunt = i[1]
                file.write(f"Total Price:{price}")
                file.write(f"Laptop Name:{lap_nam}")
                file.write(f"Quantity:{qunt}\n")
                file.write(f"Brand: {brand}")
                tprice = int(price) * int(qunt)
                file.write(f"Total Price:{tprice}")
                total = total + int(tprice)
            if ship.lower() == "y":
                total = total + 250
                file.write(f"Total price with sphipping cost:{total}")
            elif ship.lower() == "n":
                file.write(f"Total price without sphipping cost: {total}")
            else:
                file.write("enter appropriate value")
            file.write(f"Total Cost: {total}")


def bill_purchhase(name, address, phone, loop_1, list2, random, dict2):
    print("\n")
    print("\n")
    print("\t \t \t \t \t Diya Electronics")
    print("\n")
    print("\t \t \t \t  Sinamangal ,Kathmandu ,|014110585 ")
    print("\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("\t \t \t \Thank you for shopping. Our sincere hope is that you are pleased with your purchase!!")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n")
    if loop_1 != True:
        print("Bill no: ", random)

        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
              datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("Name: ", name)
        print("Address: ", address, "\nPhone: ", phone)
        total = 0
        for i in list2:
            lap_nam = dict2[i[0]][0]
            brand = dict2[i[0]][1]
            price = dict2[i[0]][2].replace("$", "")
            qunt = i[1]
            print("Price :", price)
            print("Laptop name:", lap_nam)
            print("Quantity: ", qunt)
            print("Brand: ", brand)
            tprice = int(price) * int(qunt)
            print("Total price: ", tprice)
            total = total + int(tprice)

        print("Total Cost: ", total)
        vat = total * (13 / 100)
        print("Vat Amount: ", vat)
        with_vat = total + vat
        print("Total Cost with Vat amount: ", with_vat)


def bill_purchase_text(name, address, phone, loop_1, list2, random, dict2):
    with open(f"bill_{random}.txt", "w") as file:
        file.write("\n")
        file.write("\n")
        file.write("\t \t \t \t \t Diya Electronics")
        file.write("\n")
        file.write("\t \t \t \t  Sinamangal ,Kathmandu,| 014110585")
        file.write("\n")

        file.write(
            "----------------------------------------------------------------------------------------------------------")
        file.write("\t Thank you for shopping. Our sincere hope is that you are pleased with your purchase!")
        file.write(
            "----------------------------------------------------------------------------------------------------------")
        file.write("\n")
        if loop_1 != True:
            file.write("Bill no: " + str(random) + "\n")
            file.write("Time: " + datetime.datetime.now().strftime("%H:%M:%S") + "\t\tDate: " +
                       datetime.datetime.now().strftime(" %d/%m/%Y") + "\n\n")
            file.write("Name: " + str(name) + "\n")
            file.write("Address: " + str(address) + "\nPhone: " + str(phone) + "\n")
            total = 0
            for i in list2:
                lap_nam = dict2[i[0]][0]
                brand = dict2[i[0]][1]
                price = dict2[i[0]][2].replace("$", "")
                qunt = i[1]
                file.write("Price: " + price + "\n")
                file.write("Laptop name: " + lap_nam + "\n")
                file.write("Quantity: " + str(qunt) + "\n")
                file.write("Brand: " + brand + "\n")
                tprice = int(price) * int(qunt)
                file.write("Total price: " + str(tprice) + "\n")
                total = total + int(tprice)
            file.write("Total Cost: " + str(total) + "\n")
            vat = total * (13 / 100)
            file.write("Vat Amount: " + str(vat) + "\n")
            with_vat = total + vat
            file.write("Total Cost with Vat amount: " + str(with_vat) + "\n")
