def printTable(tableData):
    colWidth = [0]* len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if(len(tableData[i][j])>colWidth[i]):
                colWidth[i]=len(tableData[i][j])

    #number of items in each inner list must be the same
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            data=tableData[j][i]
            print(data.rjust(colWidth[j]+1),end='')
        print()
    return None

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
