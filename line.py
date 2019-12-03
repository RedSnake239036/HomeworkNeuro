

def correct_input():
    while True:
        try:
            crds1 = (float(input()), float(input()), float(input()))
            crds2 = (float(input()), float(input()), float(input()))
            return (crds1, crds2)
        except:
            print('Что-то пошло не так')
            continue


#((x1, y1, z1), (x2, y2, z2))

#3 + макс лен - мин лен
def line(coord):
    x = coord[1][0] - coord[0][0]
    y = coord[1][1] - coord[0][1]
    z = coord[1][2] - coord[0][2]
    upperx = '{} - {}'.format(x, coord[0][0])
    lowerx = '{} - {}'.format(coord[1][0], coord[0][0])
    uppery = '{} - {}'.format(y, coord[0][1])
    lowery = '{} - {}'.format(coord[1][1], coord[0][1])
    upperz = '{} - {}'.format(z, coord[0][2])
    lowerz = '{} - {}'.format(coord[1][2], coord[0][2])

    upper = '{} - {}   {} - {}   {} - {}'.format(x, coord[0][0], y, coord[0][1], z, coord[0][2])
    lower = '{} - {}   {} - {}   {} - {}'.format(coord[1][0], coord[0][0], coord[1][1], coord[0][1],
                                                 coord[1][2], coord[0][2])
    print(upperx, ' ' * (3 + max(len(upperx), len(lowerx)) - min(len(upperx), len(lowerx))),
          uppery, ' ' * (3 + max(len(uppery), len(lowery)) - min(len(uppery), len(lowery))), upperz)
    print('̶' * max(len(upperx), len(lowerx)), ' = ', '̶' * max(len(uppery), len(lowery)), )
    print(lowerx, ' ' * (3 + max(len(upperx), len(lowerx)) - min(len(upperx), len(lowerx))),
          lowery, ' ' * (3 + max(len(uppery), len(lowery)) - min(len(uppery), len(lowery))))

line(correct_input())