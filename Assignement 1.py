## Assignment 1:
# The objective is to create a Pascal's trigle and print its first 15 lines

# I will start with a loop

def print_pascal_triangle(n):
    triangle = [[1]]

    for i in range(1,n):
        row = [1]
        for j in range (1,i):
            row.append(triangle[i-1][j-1] +triangle[i-1][j])

        row.append(1)
        triangle.append(row)
    
    #Print the triangle
    max_width = len(''.join(map(str,triangle[-1])))
    for row in triangle:
        print(''.join(map(str, row)).center(max_width))

    print_pascal_triangle(15)
