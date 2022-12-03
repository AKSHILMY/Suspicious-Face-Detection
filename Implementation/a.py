N = int(input())

C = []
for n in range(N):
    x, y = map(int, input().strip().split(" "))
    C.append([x, y])

area_2 = 0
final_coordinates = [[], [], []]
for center in C:
    max_dist_v = 0
    max_dist_h = 0
    coordinates = [[], []]
    for each in C:
        if center != each:
            if each[1] == center[1]:  # horizontal
                h_length = center[0]-each[0]
                if h_length > max_dist_h:
                    max_dist_h = h_length
                    coordinates[0] = each
            if each[0] == center[0]:  # vertical
                v_length = center[1]-each[1]
                if v_length > max_dist_v:
                    max_dist_v = v_length
                    coordinates[0] = each
    a_value_2 = (max_dist_v*max_dist_h)
    print(coordinates)
    if a_value_2 > area_2:
        area_2 = a_value_2
print(area_2)
