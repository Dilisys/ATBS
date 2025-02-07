tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose'],
['beans', 'celery', 'carrots', 'artichokes']]

def findLongest (arr):
    longest = 0;
    for string in arr:
        if longest < len(string):
            longest = len(string)
    
    return longest

def printTable (arr):
    arrlength = len(arr);
    colWidths = [0] * arrlength 

    for i in range(len(colWidths)):
        colWidths[i] = findLongest(arr[i])

    for i in range(arrlength):
        noline = ' '
        for j in range(arrlength):
            if j == arrlength-1:
                noline = '\n'
            print(arr[j][i].rjust(colWidths[j]), end = noline)

printTable(tableData)