even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    # Or squares.append(value**2)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

one_twenty = [value for value in range(1,21)]
print(one_twenty)

one_twenty = []
for value in range(1, 21):
    one_twenty.append(value)
print(one_twenty)

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

print(cubes)

cubes2 = [value**3 for value in range(1,11)]
print(cubes2)

quads = ['4', '16', '256', '512']
for quad in quads[0:3]:
    print(quad)