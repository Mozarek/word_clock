def parseLayoutsCompressed(file_name):
    layouts = []
    with open(file_name , "r") as f:
        rows, cols , lastCols = [int(x) for x in next(f).split()]
        for line in f: # read rest of lines
            layouts.append([int(x) for x in line.split()])
    
    return (layouts , rows , cols , lastCols)

def parseLayoutLetters(file_name):
    layout = []
    with open(file_name , "r") as f:
        for line in f: # read rest of lines
            layout.append([x for x in line.split()])
    
    return layout

def decompressLayout(layout):
    decLayout = [[0 for x in range(11)] for y in range(12)]
    for r in range(12):
        i=0
        while layout[r]>0:
            decLayout[r][11-i-1] = layout[r]%2
            layout[r]//=2
            i+=1
    
    return decLayout
