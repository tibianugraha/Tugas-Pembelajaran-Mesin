# List
contoh_list = [1,3,3,5,5,5,7,7,9]
print(contoh_list)
print(len(contoh_list))

contoh_list = set([1,3,3,5,5,5,7,7,9])
print(contoh_list)
print(len(contoh_list))

angka = [13,7,24,5,96,84,71,11,38]

print(min(angka))
print(max(angka))

# Menghitung kemunculan angka:
genap = [2,4,4,6,6,6,8,10,10]

print(genap.count(6))

# Sorting List
# Ascending
kendaraan = ['motor','mobil','helikopter','pesawat']
kendaraan.sort()
print(kendaraan)

# Descending
kendaraan.sort(reverse=True)
print(kendaraan)