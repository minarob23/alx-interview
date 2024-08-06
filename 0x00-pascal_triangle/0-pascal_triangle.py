def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to the nth row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Each row starts with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with a 1
        triangle.append(row)

    return triangle
