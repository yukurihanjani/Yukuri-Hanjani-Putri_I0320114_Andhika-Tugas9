import array

A = array.array ('i', [100, 200, 300, 400, 500])

print(A)

A[1] = -700 # Mengubah elemen kedua
A[4] = 800 # Mengubah elemen kelima
print(A)

# exercise 9.10
# Membalik urutan Array
A.reverse()

# Nilai akhir setelah dibalik
print(A)