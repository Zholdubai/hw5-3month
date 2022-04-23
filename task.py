h = int(input())


def arenda_mashin(days):
    arenda = days * 50
    if days >= 3 and days < 7:
        print(((arenda * 100) - (arenda * 10)) / 100, '10%')
    elif days >= 7:
        print(((arenda * 100) - (arenda * 30)) / 100, '30%')
    else:
        print(arenda)



arenda_mashin(h)