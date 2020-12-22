class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_rows_lists = [[int(string) for string in row.split(' ')] for row in matrix_string.split('\n')]
        
    def row(self, index):
        return self.matrix_rows_lists[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix_rows_lists]