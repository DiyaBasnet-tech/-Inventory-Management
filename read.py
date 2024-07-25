def title_for_welcome():
    print("\n")
    print("\n")
    print("\t \t \t \t \t Diya Electronics")
    print("\n")
    print("\t \t \t \t  Sinamangal,Kathmandu,| 4110585")
    print("\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t Welcome to our store, We are glad to you are here!!")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n")


def tabel_for_better_view():
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N\t\tName\t\t\tComapny Name\t\tPrice\t\tQuantity Processor\t\t Graphics")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    file = open('/Users/diyabasnet/Desktop/22068105 Diya Basnet /elo.txt','r')
    a = 1
    for line in file:
        print(a, "\t\t", line.replace(",", "\t\t")) 
        a=a+1 #increament 
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

def laptop_file_for_read(): 
    files = open('/Users/diyabasnet/Desktop/22068105 Diya Basnet /elo.txt', 'r') 
    laptop_dictionary ={} 
    lines = files.readlines() 
    for i in range(len(lines)):
        a = lines[i].strip().split(",")
        laptop_dictionary[i + 1] = a 
    return laptop_dictionary