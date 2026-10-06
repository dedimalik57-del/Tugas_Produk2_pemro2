from produk2 import produk


jumlah_produk = int(input("Masukan jumlah produk: "))

total_seluruh_pembelian = 0

for i in range(jumlah_produk):

    nama_produk = input("Masukan nama produk: ")
    harga_produk = float(input("Masukan harga produk: "))
    jumlah_beli = int(input("Masukan jumlah beli: "))

    produk_baru = produk(nama_produk, harga_produk)

    total_pembelian = produk_baru.hitung_total(jumlah_beli)

    print("Total pembelian", produk_baru.nama, ": Rp", total_pembelian)

    total_seluruh_pembelian += total_pembelian


diskon = produk_baru.hitung_diskon(total_seluruh_pembelian)

total_bayar = total_seluruh_pembelian - diskon

print("\n=== HASIL PEMBELIAN ===")
print("Total Pembelian : Rp", total_seluruh_pembelian)
print("Diskon 5%       : Rp", diskon)
print("Total Bayar     : Rp", total_bayar)