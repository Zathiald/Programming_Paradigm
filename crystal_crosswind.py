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

d_x, d_y, k, winds = read_input()
print("d_x:", d_x)
print("d_y:", d_y)
print("k:", k)
print("Winds:")
for w_x, w_y, b, boundaries in winds:
    print("Direction:", w_x, w_y)
    print("Number of boundaries:", b)
    print("Boundaries:", boundaries)






















