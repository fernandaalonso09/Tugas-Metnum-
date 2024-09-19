import math

# Fungsi f(x) = x - e^(-x)
def f(x):
    return x - math.exp(-x)

# Turunan dari f(x), f'(x) = 1 + e^(-x)
def f_prime(x):
    return 1 + math.exp(-x)

# Metode Newton-Raphson untuk menemukan akar f(x)
def newton_raphson(x0, tolerance=1e-7, max_iterations=100):
    x = x0
    for iteration in range(max_iterations):
        fx = f(x)
        dfx = f_prime(x)
        
        # Jika turunan nol, metode gagal
        if dfx == 0:
            raise ValueError("Turunan f'(x) adalah nol. Tidak dapat melanjutkan.")
        
        # Hitung nilai baru untuk x
        x_new = x - fx / dfx
        
        # Periksa apakah hasil sudah cukup dekat dengan akar
        if abs(x_new - x) < tolerance:
            return x_new
        
        # Update nilai x untuk iterasi berikutnya
        x = x_new
    
    # Jika tidak konvergen dalam iterasi maksimum, lemparkan error
    raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")

# Nilai awal
x0 = 0

# Memanggil metode Newton-Raphson dengan nilai awal x0
try:
    akar = newton_raphson(x0)
    print(f"Akar yang ditemukan adalah: {akar}")
except ValueError as e:
    print(e)
