import sqlite3

def func1(size, legal):
    sizes = {'r1': [0, 1000000], 'r': [0, 1000000000000]}
    with open("placemark", "r") as file:
        s = file.read()

    s1 = [""" .add(new ymaps.Placemark([""",
          """ ], {
                balloonContent: 'Организация: """,
          """ , телефон: """,
          """ '
            }, {
                iconColor: '#fffff'
            }))"""]

    t = ''

    con = sqlite3.connect("static//base//dump.db")
    cur = con.cursor()

    print(sizes[size], 1)

    s2 = "SELECT Coordinate, Responsible_Org, Telephone FROM dump"
    t1 =[]

    if not (size!='r' and legal!='все равно'):
        s2 += " WHERE "

    if not size!='r':
        t1.append(f'Area < {sizes[size][1]} AND Area < {sizes[size][1]}')

    if not legal!='все равно':
        t1.append(f'Legality = {legal}')

    s2 += ' AND '.join(t1)

    result = cur.execute(s2).fetchall()

    con.close()

    for elem in result:
        t += s1[0] + elem[0] + s1[1] + elem[1] + s1[2] + elem[2] + s1[3]

    s += t + "}"

    with open("static//js//placemark.js", "w", encoding='utf-8') as file:
        file.write(s)

func1('r1', 1)