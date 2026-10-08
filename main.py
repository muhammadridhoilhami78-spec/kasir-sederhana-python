print("=== KASIR SEDERHANA ===")

nama_barang = input("Nama Barang  : ")
harga = int(input("Harga Barang  : "))
jumlah = int(input("Jumlah Barang  : "))

subtotal = harga * jumlah

# Diskon otomatis
if subtotal >= 100000:
    diskon = 10
elif subtotal >= 50000:
    diskon = 5
else:
    diskon = 0

potongan = subtotal * diskon / 100
total_bayar = subtotal - potongan

uang_bayar = int(input("Uang Bayar : "))

if uang_bayar < total_bayar:
    print("\n Uang tidak cukup!")
else:
    kembalian = uang_bayar - total_bayar

    print("\n=== STRUK BELANJA ===")
    print("Nama Barang :", nama_barang)
    print("Harga       : Rp", harga)
    print("Jumlah      :", jumlah)
    print("Subtotal    : Rp", subtotal)
    print("Diskon      :", diskon, "%")
    print("potongan    : Rp", potongan)
    print("Total Bayar : Rp", total_bayar)
    print("Uang Bayar  : Rp", uang_bayar)
    print("Kembalian   : RP", kembalian)