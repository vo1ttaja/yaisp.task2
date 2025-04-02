def read_from_file(file_path):
    try:
        matrix = []
        with open(file_path, "r") as file:
            for line in file:
                row = line.strip().split(" ")
                matrix.append(row)
            return matrix
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Произошла ошибка " + e)


def get_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result_matrix = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            count = 0
            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    if i == r and j == c:
                        continue
                    if matrix[i][j] == matrix[r][c]:
                        count += 1
            result_matrix[r][c] = count
    return result_matrix


def write_in_file(matrix):
    delimiter = " "
    try:
        with open("outputFile.txt", "w") as file:
            for row in matrix:
                line = delimiter.join(map(str, row))
                file.write(line + '\n')
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


matrix = read_from_file("tests/testInputFile1.txt")
result_matrix = get_matrix(matrix)
write_in_file(result_matrix)
