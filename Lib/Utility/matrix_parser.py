def parse_matrix(s):
    ###make a 2d list
    try:
        rows = s.strip("[]").split(":")
        matrix = [list(map(int, row.split(","))) for row in rows]
        return matrix
    except Exception:
        return None