def read_input():
    d_x, d_y, k = map(int, input().split())
    winds = []
    for _ in range(k):
        line = input().split()
        w_x, w_y = map(int, line[:2])
        b = int(line[2])
        boundaries = [tuple(map(int, line[i:i+2])) for i in range(3, len(line), 2)]
        winds.append((w_x, w_y, b, boundaries))
    return d_x, d_y, k, winds

def generate_structure(d_x, d_y, winds):
    structure_min = [['.' for _ in range(d_x)] for _ in range(d_y)]
    structure_max = [['.' for _ in range(d_x)] for _ in range(d_y)]
    
    for w_x, w_y, _, boundaries in winds:
        for x, y in boundaries:
            structure_min[y-1][x-1] = '#'
            structure_max[y-1][x-1] = '#'
    
    return structure_min, structure_max

def print_structure(structure):
    for row in structure:
        print(''.join(row))

d_x, d_y, k, winds = read_input()
structure_min, structure_max = generate_structure(d_x, d_y, winds)

print("d_x:", d_x)
print("d_y:", d_y)
print("k:", k)
print("Winds:")
for w_x, w_y, b, boundaries in winds:
    print("Direction:", w_x, w_y)
    print("Number of boundaries:", b)
    print("Boundaries:", boundaries)


print("Minimum structure:")
print_structure(structure_min)

print("\nMaximum structure:")
print_structure(structure_max)






















