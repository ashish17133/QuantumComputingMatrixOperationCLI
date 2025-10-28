class MatrixOperations:
    #Class for basic matrix operations: add, subtract, multiply, divide

    #Before Using matrix let validate the matrix size
    @staticmethod
    def _validate_same_size(A, B):
        #check for dimensions
        if len(A) != len(B) or any(len(rowA) != len(rowB) for rowA, rowB in zip(A, B)):
            raise ValueError("Matrices must have the same dimensions")

    @staticmethod
    def add(A, B):
        #check dimension and add items
        MatrixOperations._validate_same_size(A, B)
        return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

    @staticmethod
    def subtract(A, B):
        #check dimesion and subtract
        MatrixOperations._validate_same_size(A, B)
        return [[a - b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

    @staticmethod
    def multiply(A, B):
        #check for validation and multiply matrices
        if len(A[0]) != len(B):
            raise ValueError("Number of columns of A must equal number of rows of B")
        result = []
        for row in A:
            new_row = []
            for col in range(len(B[0])):
                val = sum(row[i] * B[i][col] for i in range(len(B)))
                new_row.append(val)
            result.append(new_row)
        return result

    @staticmethod
    def divide(A, B):
        # check dim validation and divide if possible
        MatrixOperations._validate_same_size(A, B)
        result = []
        for rowA, rowB in zip(A, B):
            new_row = []
            for a, b in zip(rowA, rowB):
                if b == 0:
                    raise ZeroDivisionError("Division by zero in matrix element")
                new_row.append(a / b)
            result.append(new_row)
        return result
