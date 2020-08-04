def matrix(r, c):
    return [[0 for _ in range(c)] for _ in range(r)]


def shape(mat):
    r = len(mat)
    c = len(mat[0])

    return r, c


def main_diagonal(mat):
    dia = []
    col = 0
    for row in mat:
        dia.append(row[col])
        col += 1
    return dia


def anti_diagonal(mat):
    dia = []
    col = len(mat[0]) - 1
    for row in mat:
        dia.append(row[col])
        col -= 1
    return dia


def windows(mat, r, c):
    max_row, max_col = shape(mat)

    i = 0
    j = 0

    while True:
        window = matrix(r, c)
        for row in range(r):
            for col in range(c):
                cur_row = row + i
                cur_col = col + j

                if cur_row >= max_row or cur_col >= max_col:
                    continue

                window[row][col] = mat[cur_row][cur_col]

        yield window

        if j + c < max_col:
            j += 1
            continue

        if i + r < max_row:
            j = 0
            i += 1
            continue

        break


def clockwise_rotate(mat):
    r, c = shape(mat)
    tmp = matrix(r, c)

    for i in range(r):
        for j in reversed(range(c)):
            tmp[i][c - j - 1] = mat[j][i]

    return tmp


def flip(mat):
    tmp = []

    for row in mat:
        tmp.append(list(reversed(row)))

    return tmp


def orientations(mat):
    tmp = mat
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp

    tmp = flip(mat)
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp
    tmp = clockwise_rotate(tmp)
    yield tmp


def compare(mat1, mat2):
    r, c = shape(mat1)

    for i in range(r):
        for j in range(c):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True


def inclusion(mat1, mat2):
    r, c = shape(mat1)

    for i in range(r):
        for j in range(c):
            if mat1[i][j] == 0:
                continue
            if mat1[i][j] != mat2[i][j]:
                return False
    return True
