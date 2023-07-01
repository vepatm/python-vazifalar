def print_spiral_matrix(n):
    matrix = [[0]*n for i in range(n)]  # Bo'sh massiv yaratish
    num = 1  # Massiv elementlarini sanash uchun o'zgaruvchi
    
    # Massivni chizish
    for layer in range((n + 1) // 2):
        # Ustunni chapdan o'ngga
        for i in range(layer, n - layer):
            matrix[layer][i] = num
            num += 1
        
        # Quyi qatorni yuqorga
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = num
            num += 1
        
        # O'ngdan chapga
        for i in range(n - layer - 2, layer - 1, -1):
            matrix[n - layer - 1][i] = num
            num += 1
        
        # Yuqoridan pastga
        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = num
            num += 1
    
    # Massivni chiqarish
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

# Test
n = int(input("n ni kiriting: "))
print_spiral_matrix(n)