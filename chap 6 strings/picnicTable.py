def printPicnic(dict, lWidth, rWidth):
    print('PICNIC ITEMS'.center(lWidth + rWidth, '-'))
    for k, v in dict.items():
        print(k.ljust(lWidth, '.') + str(v).rjust(rWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)