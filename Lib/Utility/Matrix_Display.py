def display_matrix(matrix):
    for row in matrix:
        print("| " + "  ".join(str(x) for x in row) + " |")
if __name__=="__main__":
    display_matrix(matrix)