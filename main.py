import os
os.system('cls')

#Data Buah
products = [
    #name, price, stock
    ["Apel", 10_000, 10], 
    ["Jeruk", 15_000, 10], 
    ["Anggur", 20_000, 10]
]

selected = None

while selected != 5:
    print("Selamat Datang di Pasar Buah")
    print("\nList Menu")
    print("1. Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    selected = int(input("Masukan angka Menu yang ingin dijalankan: "))

    if selected == 1:
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<18}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i][0]:<10}| Rp.{products[i][1]:<15,}| {products[i][2]}")
        input()
        os.system('cls')
    elif selected == 2:
        print("\nMenambah Buah\n")
        nama = input("Masukan Nama Buah: ")
        harga = int(input("Masukan Harga Buah: "))
        stok = int(input("Masukan Stok Buah: "))
        products.append([nama, harga, stok])
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<15}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i][0]:<10}| {products[i][1]:<15,}| {products[i][2]}")
        input()
        os.system('cls')
    elif selected == 3:
        print("\nMenghapus Buah\n")
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<15}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i][0]:<10}| {products[i][1]:<15,}| {products[i][2]}")
        index = int(input("Masukan index buah yang ingin dihapus: "))
        while index > len(products)-1:
            print("Index tidak tersedia !")
            index = int(input("Masukan index buah yang ingin dihapus: "))
        products.pop(index)
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<15}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i][0]:<10}| {products[i][1]:<15,}| {products[i][2]}")
        input()
        os.system('cls')
    elif selected == 4:
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
            for i in range(len(products)):
                products[i][2] -= qty_per_product[i]
            print("\nTerima Kasih !")
            if (selisih):
                print(f"\nUang kembalian anda: Rp.{selisih:,}")

        input()
        os.system('cls')
    elif selected == 5:
        print("Terima Kasih !")
        break
    else:
        print("Pilihan tidak tersedia !")