catatan = {}
item = input("Beli apa? ")
biaya = int(input("Harganya? "))
catatan[item] = biaya
for k, v in catatan.items():
    print(f"- {k}: Rp{v}")