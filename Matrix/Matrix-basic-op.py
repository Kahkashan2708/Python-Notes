# Matrix OperationsSheet in Python

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Number of rows
rows = len(matrix)

# 2. Number of columns
cols = len(matrix[0]) if matrix else 0

# 3. Access a whole row
row_i = matrix[1]  # 2nd row

# 4. Access a whole column
col_j = [row[2] for row in matrix]  # 3rd column

# 5. Access a particular element
value = matrix[2][1]  # element at row 3, col 2

# 6. Last element of a row
last_val = matrix[0][-1]

# 7. First element of a row
first_val = matrix[0][0]

# 8. Flatten matrix into a single list
flat = [elem for row in matrix for elem in row]

# 9. Transpose of a matrix
transpose = list(map(list, zip(*matrix)))

# 10. Sum of all elements
total_sum = sum(sum(row) for row in matrix)

# 11. Max element
max_val = max(max(row) for row in matrix)

# 12. Min element
min_val = min(min(row) for row in matrix)

# 13. Iterate over all elements (row, col, value)
for i in range(rows):
    for j in range(cols):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# 14. Diagonal elements
main_diag = [matrix[i][i] for i in range(min(rows, cols))]
anti_diag = [matrix[i][cols - i - 1] for i in range(min(rows, cols))]

# Print results
print("Rows:", rows)
print("Cols:", cols)
print("2nd Row:", row_i)
print("3rd Col:", col_j)
print("Element (3,2):", value)
print("Last element of row 1:", last_val)
print("First element of row 1:", first_val)
print("Flattened:", flat)
print("Transpose:", transpose)
print("Sum:", total_sum)
print("Max:", max_val)
print("Min:", min_val)
print("Main Diagonal:", main_diag)
print("Anti Diagonal:", anti_diag)
