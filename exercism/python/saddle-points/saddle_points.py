def saddle_points(matrix):
    try:
        columns = [column(matrix, i) for i in range(len(matrix[0]))]
    except:
        raise ValueError('You have provided an invalid Matrix')
    result = []
    for y, row in enumerate(matrix):
        for x, i in enumerate(row):
            if min(columns[x]) >= i and max(row) <= i:
                entry = dict(column=x+1, row=y+1)
                result.append(entry)

    return result

def column(matrix, index):
        return [row[index] for row in matrix]