list = ['apples', 'bananas', 'tofu', 'cats', 'chickens']

#list is empty
if (not list):
    print('Empty list, my man.')
elif (len(list) == 1): #list has just one item

    commaList = 'Just ' + list[0]
    print(commaList)

else: #list has more than one item
    commaList = ''
    for i in range(len(list)):
        if i == (len(list) - 1):
            commaList = commaList + "and " + list[i]
        else:
            commaList = commaList + list[i] + ', '

    print(commaList)