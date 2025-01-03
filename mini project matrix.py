def input_matrix():
    print("Masukkan elemen-elemen matriks (maksimal ukuran 4x4):")
    rows = int(input("Masukkan jumlah baris (1-4): "))
    cols = int(input("Masukkan jumlah kolom (1-4): "))

    if rows > 4 or cols > 4:
        print("Ukuran matriks maksimal adalah 4x4.")
        return None

    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Masukkan elemen baris {i+1} dipisahkan dengan spasi: ").split()))
        if len(row) != cols:
            print("Jumlah elemen dalam baris tidak sesuai dengan jumlah kolom.")
            return None
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matriks harus memiliki ukuran yang sama untuk dijumlahkan.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row)

    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matriks harus memiliki ukuran yang sama untuk dikurangkan.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row)

    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)

    return result

def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = [matrix[i][j] for i in range(len(matrix))]
        result.append(row)

    return result

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Hanya matriks persegi yang memiliki determinan.")
        return None

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    elif n == 4:
        det = 0
        for col in range(4):
            sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
        return det
    else:
        print("Ukuran matriks tidak didukung untuk determinan.")
        return None

def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        print("Matriks tidak memiliki invers karena determinan bernilai 0.")
        return None

    n = len(matrix)
    if n == 1:
        return [[1 / matrix[0][0]]]

    adj = []
    for i in range(n):
        adj_row = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor = determinant(sub_matrix)
            adj_row.append(((-1) ** (i + j)) * cofactor)
        adj.append(adj_row)

    adj_transpose = transpose_matrix(adj)
    inv = [[adj_transpose[i][j] / det for j in range(n)] for i in range(n)]
    return inv

def main():
    print("Program Operasi Matriks 4x4")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinan Matriks")
    print("5. Inverse Matriks")
    choice = int(input("Pilih operasi (1-5): "))

    if choice == 1 or choice == 2:
        print("Input matriks pertama:")
        matrix1 = input_matrix()
        print("Input matriks kedua:")
        matrix2 = input_matrix()

        if matrix1 and matrix2:
            if choice == 1:
                result = add_matrices(matrix1, matrix2)
            else:
                result = subtract_matrices(matrix1, matrix2)

            if result:
                print("Hasil operasi:")
                print_matrix(result)

    elif choice == 3:
        print("Input matriks pertama:")
        matrix1 = input_matrix()
        print("Input matriks kedua:")
        matrix2 = input_matrix()

        if matrix1 and matrix2:
            result = multiply_matrices(matrix1, matrix2)
            if result:
                print("Hasil operasi:")
                print_matrix(result)

    elif choice == 4:
        print("Input matriks:")
        matrix = input_matrix()
        if matrix:
            result = determinant(matrix)
            print(f"Determinannya adalah: {result}")

    elif choice == 5:
        print("Input matriks:")
        matrix = input_matrix()
        if matrix:
            result = inverse_matrix(matrix)
            if result:
                print("Matriks invers adalah:")
                print_matrix(result)

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
