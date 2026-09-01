import os
os.system('cls')

#Data Buah
products = [
    #name, price, stock
    ["Apel", 10_000, 10], 
    ["Jeruk", 15_000, 10], 
    ["Anggur", 20_000, 10]
]

# Menu Input QTY
# qty_apple = int(input("Masukan Jumlah Apel: "))
# while qty_apple >products[0[2]]:
#     print(f"Jumlah yang dimasukkan terlalu banyak !")
#     print(f"Stock Apel Tinggal: {products[0][2]}")
#     qty_apple = int(input("Masukan Jumlah Apel: "))
# qty_orange = int(input("Masukan Jumlah Jeruk: ")) 
# while qty_orange > products[1][2]:
#     print(f"Jumlah yang dimasukkan terlalu banyak !")
#     print(f"Stock Jeruk Tinggal: {products[1][2]}")
#     qty_orange = int(input("Masukan Jumlah Jeruk: "))
# qty_grape = int(input("Masukan Jumla Anggur: "))
# while qty_grape > products[2][2]:
#     print(f"Jumlah yang dimasukkan terlalu banyak !")
#     print(f"Stock Anggur Tinggal: {products[2][2]}")
#     qty_grape = int(input("Masukan Jumlah Anggur: "))

# #Perhitungan
# total_apple = qty_apple*products[0][1]
# total_orange = qty_orange*products[2][1]
# total_grape = qty_grape*products[3][1]
# grand_total = total_apple + total_orange + total_grape

# # Menu Detail Belanja
# print("\nDetail Belanja\n")
# print (f"Apel   : {qty_apple} x Rp.{products[0][1]:,} = Rp.{total_apple:,}")
# print (f"Jeruk  : {qty_orange} x Rp.{products[1][1]:,} = Rp.{total_orange:,}")
# print (f"Anggur : {qty_grape} x Rp.{products[2][1]:,} = Rp.{total_grape:,}")
# print (f"\nTotal  : Rp.{grand_total:,}\n")

price_per_product = []
qty_per_product = []
grand_total = 0

for i in products:
    qty = int(input(f"Masukan Jumlah {i[0]}: "))
    while qty > i[2]:
        print(f"Jumlah yang dimasukkan terlalu banyak !")
        print(f"Stock {i[0]} Tinggal: {i[2]}")
        qty = int(input(f"Masukan Jumlah {i[0]}: "))
    price  = qty * i[1]

    price_per_product.append(price)
    qty_per_product.append(qty)
    grand_total += price

for i in range(len(products)):
    print(f"{products[i][0]} : {qty_per_product[i]} x Rp.{products[i][1]:,} = Rp.{price_per_product[i]:,}")
print(f"\nTotal : Rp.{grand_total:,}\n")   

#Payment Feature 
print ("-"*10)

payment = int(input("Masukan Jumlah Uang: "))
selisih = payment - grand_total
while selisih < 0:
    print("\n[X] Tansaksi dibatalkan !")
    print(f"Uang kurang sebesar Rp.{abs(selisih):,}")
    payment = int(input("\nMasukan Jumlah Uang: "))
    selisih = payment - grand_total
else:
    print("\nTerima Kasih !")
    if (selisih):
        print(f"\nUang kembalian anda: Rp.{selisih:,}")