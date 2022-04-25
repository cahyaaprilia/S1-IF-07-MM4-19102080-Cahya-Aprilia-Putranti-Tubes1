#NAMA : CAHYA APRILIA PUTRANTI
#KELAS : S1 IF 07 MM4
#NIM ; 19102080

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

"""# Selection Sort """

# fungsi minIndex digunakan untuk mencari nilai terkecil diantara array
def cariIndeksTerkecil(array, i , j ):
    # apabila pencarian sudah di ujung array maka kembalikan index i
    if i == j:
        return i

    # melakukan pencarian indeks nilai terkecil menggunakan metode rekursif
    k = cariIndeksTerkecil(array, i + 1, j)

    if(array[i] < array[k]):
    # kembalikan nilai i apabila nilai array[i] kurang dari array[k]
      return i
    else:
    # kembalikan nilai k apabila nilai array[i] lebih besar dari array[k]
      return k

def selectionSort(array, n_data, index = 0):
    # kalo index sama dengan jumlah data di array maka berhenti
    if index == n_data:
        return -1

    # mencari index dengan nilai terkecil
    k = cariIndeksTerkecil(array, index, n_data-1)

    # apabila indeks k tidak sama dengan nilai variable index
    if k != index:
        # tukar array[k] menjadi array[index]
        # tukar arra[index] menjadi array[k]
        temp = array[index]
        array[index] = array[k]
        array[k] = temp

    # melanjutkan sorting menggunakan metode rekursif
    selectionSort(array, n_data, index + 1)

"""# Running Algoritma"""

start_time_selection_sort = process_time()
selectionSort(selectionArr, nSelection)
end_time_selection_sort = process_time()

"""# Hasil Running"""

print(f'Sorted array: {selectionArr}')
print('start_time: ', start_time_selection_sort)
print('end_time: ', end_time_selection_sort)
print('executing_time: ', (end_time_selection_sort - start_time_selection_sort), 'seconds')

"""# Reset Rekursif Limit"""

sys.setrecursionlimit(1000)