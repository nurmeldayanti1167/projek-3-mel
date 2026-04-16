catatan = {}
item = input("Beli apa? ")
biaya = int(input("Harganya? "))
catatan[item] = biaya
for k, v in catatan.items():
    print(f"- {k}: Rp{v}")
    total = sum(catatan.values())
print(f"Total Pengeluaran: Rp{total}")
# Logic: catatan.pop(item_terakhir)
print("Catatan berhasil diperbarui!")