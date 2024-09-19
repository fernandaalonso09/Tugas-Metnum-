import numpy as np

# Mendefinisikan fungsi f(x) = x + e^x
def f(x):
    return x + np.exp(x)

# Metode Biseksi
def biseksi(f, a, b, toleransi=1e-6, max_iterasi=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar di interval tersebut.")
        return None
    
    iterasi_count = 0
    while (b - a) / 2 > toleransi and iterasi_count < max_iterasi:
        c = (a + b) / 2
        if f(c) == 0:  # Jika nilai tengah adalah akar
            print(f"Akar ditemukan pada iterasi ke-{iterasi_count}")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi_count += 1
    
    if iterasi_count == max_iterasi:
        print(f"Iterasi maksimum tercapai ({max_iterasi} iterasi).")
    
    return (a + b) / 2

# Metode Regula Falsi
def regulafalsi(f, a, b, toleransi=1e-6, max_iterasi=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar di interval tersebut.")
        return None
    
    iterasi_count = 0
    c = a
    while abs(f(c)) > toleransi and iterasi_count < max_iterasi:
        # Menghitung nilai c
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        if f(c) == 0:
            print(f"Akar ditemukan pada iterasi ke-{iterasi_count}")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi_count += 1
    
    if iterasi_count == max_iterasi:
        print(f"Iterasi maksimum tercapai ({max_iterasi} iterasi).")
    
    return c

# Menentukan interval dan mencari akar
a, b = -1, 0

root_bisection = biseksi(f, a, b)
print(f"Akar (Hasil Metode Biseksi): {root_bisection}")

root_regulafalsi = regulafalsi(f, a, b)
print(f"Akar (Hasil Metode Regula Falsi): {root_regulafalsi}")

