import os
os.system('cls')

# Harga Buah
price_apple = 10_000
price_orange = 15_000
price_grape = 20_000

# Menu Input QTY
qty_apple = int(input("Masukan Jumlah Apel: "))
qty_orange = int(input("Masukan Jumlah Jeruk: ")) 
qty_grape = int(input("Masukan Jumla Anggur: "))

#Perhitungan
total_apple = qty_apple*price_apple
total_orange = qty_orange*price_orange
total_grape = qty_grape*price_grape
grand_total = total_apple + total_orange + total_grape

# Menu Detail Belanja
print("\nDetail Belanja\n")
print (f"Apel   : {qty_apple} x Rp.{price_apple:,} = Rp.{total_apple:,}")
print (f"Jeruk  : {qty_orange} x Rp.{price_orange:,} = Rp.{total_orange:,}")
print (f"Anggur : {qty_grape} x Rp.{price_grape:,} = Rp.{total_grape:,}")
print (f"\nTotal  : Rp.{grand_total:,}\n")

#Payment Feature 
print ("-"*10)
payment = int(input("Masukan Jumlah Uang: "))
selisih = payment - grand_total

if(selisih < 0):
    print("\n[X] Tansaksi dibatalkan !")
    print(f"Uang kurang sebesar Rp.{abs(selisih):,}")
else:
    print("\nTerima Kasih !")
    if (selisih):
        print(f"\nUang kembalian anda: Rp.{selisih:,}")