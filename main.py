pole = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pole[1][1] = 105

novy_radek = [10, 11, 12]
novy_radek.append(13)
pole.append(novy_radek)

for radek in pole[:-1]:
    radek.append(0)

for radek in pole:
    print(radek)