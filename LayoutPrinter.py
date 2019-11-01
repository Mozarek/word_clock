from LayoutCreator import *

def printLayout(layout):
    for row in layout :
        for col in row :
            print(col , " " , end = '')
        print("\n" , end = '')

def printCompressedLayout(layout):
    for row in layout:
        row_num = 0
        for col in row:
            row_num = row_num*2 + col
        print(row_num , " " , end = '')

def printAllLayouts():
    print(SIZE_Y , SIZE_X , SIZE_LAST_ROW)
    for h in range(0,12):
        for m in range(0,60):
            layout = createLayout(h,m)
            printCompressedLayout(layout)
            print("")