user_input = input()
lines = user_input.split(',')

# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
# 2D lists are accessed using double index list[i1][i2] (i1 row, i2 element in i1)

mult_table = [[int(num) for num in line.split()] for line in lines]  # code converts to 2D list like a matrix
for rows in mult_table:  # accessing each row (each row is a list)
    x = list(map(str, rows))  # map(function, iterables) is used to change type of elements in list
    new_x = ' | '.join(x)
    print(new_x)
    for elements in rows:  # accessing elements in each row, they are int by input
        pass






