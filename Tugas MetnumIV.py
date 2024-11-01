# Muhammad Fernanda Alonso Meilandri
#2309076031
# Fungsi untuk mencetak matriks augmented
def print_matriks(A, B):
    for i in range(len(A)):
        row = ["{:.2f}".format(A[i][j]) for j in range(len(A[0]))]
        print(" | ".join(row) + " | " + "{:.2f}".format(B[i]))
    print("\n")

# Fungsi untuk melakukan eliminasi Gauss
def eliminasi_gauss(A, B):
    n = len(B)
    
    # Tahap eliminasi maju (membuat segitiga atas)
    for i in range(n):
        # Membagi baris dengan elemen diagonal (normalisasi)
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot
        
        # Eliminasi elemen di bawah pivot
        for k in range(i+1, n):
            faktor = A[k][i]
            for j in range(i, n):
                A[k][j] -= faktor * A[i][j]
            B[k] -= faktor * B[i]
    
    print("Matriks setelah eliminasi maju:")
    print_matriks(A, B)
    
    # Tahap substitusi balik untuk mendapatkan solusi
    X = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        X[i] = B[i]
        for j in range(i+1, n):
            X[i] -= A[i][j] * X[j]
    
    return X

# Matriks koefisien
A = [
    [1, 1, 1],
    [1, 2, -1],
    [2, 1, 2]
]

# Vektor konstanta
B = [6, 2, 10]

print("Matriks awal:")
print_matriks(A, B)

# Panggil fungsi eliminasi Gauss
solusi = eliminasi_gauss(A, B)

# Tampilkan hasil
print("Solusi dari sistem persamaan adalah:")
for i in range(len(solusi)):
    print(f"x{i+1} = {solusi[i]:.2f}")
