import os
os.system('cls')

#Data Buah
products = [
    {
        "name": "Apel",
        "price": 10000,
        "stock": 10
    },
    {
        "name": "Jeruk",
        "price": 15000,
        "stock": 10
    },
    {
        "name": "Anggur",
        "price": 20000,
        "stock": 10
    }
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
            print(f"{i:<7}| {products[i]['name']:<10}| Rp.{products[i]['price']:<15,}| {products[i]['stock']}")
        input()
        os.system('cls')
    elif selected == 2:
        print("\nMenambah Buah\n")
        nama = input("Masukan Nama Buah: ")
        harga = int(input("Masukan Harga Buah: "))
        stok = int(input("Masukan Stok Buah: "))
        products.append({"name": nama, "price": harga, "stock": stok})
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<18}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i]['name']:<10}| Rp.{products[i]['price']:<15,}| {products[i]['stock']}")
        input()
        os.system('cls')
    elif selected == 3:
        print("\nMenghapus Buah\n")
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<18}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i]['name']:<10}| Rp.{products[i]['price']:<15,}| {products[i]['stock']}")
        index = int(input("Masukan index buah yang ingin dihapus: "))
        while index > len(products)-1:
            print("Index tidak tersedia !")
            index = int(input("Masukan index buah yang ingin dihapus: "))
        products.pop(index)
        print("\nDaftar Buah\n")
        print(f"{"Index":<7}| {"Nama":<10}| {"Harga":<18}| {"Stok"}")
        for i in range(len(products)):
            print(f"{i:<7}| {products[i]['name']:<10}| Rp.{products[i]['price']:<15,}| {products[i]['stock']}")
        input()
        os.system('cls')
    elif selected == 4:
        price_per_product = []
        qty_per_product = []
        grand_total = 0

        for i in products:
            qty = int(input(f"Masukan Jumlah {i['name']}: "))
            while qty > i['stock']:
                print(f"Jumlah yang dimasukkan terlalu banyak !")
                print(f"Stock {i['name']} Tinggal: {i['stock']}")
                qty = int(input(f"Masukan Jumlah {i['name']}: "))
            price  = qty * i['price']

            price_per_product.append(price)
            qty_per_product.append(qty)
            grand_total += price

        for i in range(len(products)):
            print(f"{products[i]['name']} : {qty_per_product[i]} x Rp.{products[i]['price']:,} = Rp.{price_per_product[i]:,}")
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
                products[i]['stock'] -= qty_per_product[i]
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