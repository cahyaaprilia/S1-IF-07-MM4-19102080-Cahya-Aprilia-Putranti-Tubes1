#NAMA : CAHYA APRILIA PUTRANTI
#KELAS : S1 IF 07 MM4
#NIM : 19102080

# Import Library

# library time fungsi process_time digunakan untuk mengukur kecepatan eksekusi dari algoritma
from time import process_time
# library numpy digunakan untuk memproduksi array number secara random
import numpy as np
# library sys digunakan untuk mengatur limit batasan aksi rekursif
import sys
# merubah batasan rekursif menjadi 10000 aksi rekursif
sys.setrecursionlimit(10000)

"""# Produksi Array Number secara Random Sebanyak 1000 buah"""

# menciptakan random array menggunakan numpy (angka awal, angka akhir, jumlah data)
randomNumber = np.random.randint(1, 1000, 1000)

# memasukkan random array ke variabel variabel dituju
selectionArr = randomNumber
quickArr = randomNumber

# menghitung jumlah data yang ada dalam array
nSelection = len(selectionArr)
nQuick = len(quickArr)

"""## Export data"""

# membuka file sample-data.txt apabila belum tersedia maka membuat file
file = open("sample-data.txt", "w")

# memasukkan tiap item array kedalam file
for i in randomNumber:
  file.write(str(i) + "\n")

# menutup atau menyimpan file dengan perubahan terbaru
file.close()

"""# Quick Sort"""

# fungsi partition berfungsi untuk mencari indeks tengah dari suatu array 
def partition(array, low, high):
  # pivot adalah array pembanding dari array terakhir
  pivot = array[high]
  # i memulai dari dari -1 supaya dapat membandingkan indeks 0 dengan pivot
  i = low - 1

  # perulangan dari nilai variable low hingga variable high
  for j in range(low, high):

    # apabila nilai array indeks j kurang dari sama dengan nilai pivot
    if array[j] <= pivot: # 0 <= 0
      # tambahkan i dengan 1
      i = i + 1
      # tukar nilai array[i] dengan array[j]
      (array[i], array[j]) = (array[j], array[i])

  # tukar array[i + 1] dengan array[high] atau pivot
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # mengembalikan indeks tengah sebagai pembagi antara sisi kiri dan kanan
  return i + 1

# fungsi untuk melakukan quick sort dengan rekursif
def quick_sort(array, low, high):

  # untuk membandingkan apakah index low kurang dari index high
  if low < high:
    # apabila ya

    # cari indeks tengah dari array
    pi = partition(array, low, high)

    # melakukan pengurutan rekursif pada bagian kiri dari indeks tengah
    quick_sort(array, low, pi - 1)

    # melakukan pengurutan rekursif pada baigan kanan dari indeks tengah
    quick_sort(array, pi + 1, high)

"""# Running Algoritma"""

start_time_quick_sort = process_time()
quick_sort(quickArr, 0, nQuick - 1)
end_time_quick_sort = process_time()

"""# Hasil Running"""

print(f'Sorted array: {quickArr}')
print('start_time: ', start_time_quick_sort)
print('end_time: ', end_time_quick_sort)
print('executing_time: ', (end_time_quick_sort - start_time_quick_sort), 'seconds')

"""# Reset Rekursif Limit"""

sys.setrecursionlimit(1000)