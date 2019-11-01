SIZE_Y = 12
SIZE_X = 11
SIZE_LAST_ROW = 4

def setLetters(row , left , length , layout):
    layout[row][left:left+length] = [1 for i in range(length)]

def createLayout(h, m):
    new_layout = [[0 for x in range(SIZE_X)] for y in range(SIZE_Y)]

    setLetters(0,0,4,new_layout)

    if 0 <= m < 5:
        setLetters(10 , 3 , 7 , new_layout)
    elif m < 35:
        setLetters(4,5,4 , new_layout)
    else:
        setLetters(4,8,2 , new_layout)

    if 5 <= m < 10:
        setLetters(1,7,4,new_layout)
    elif 10 <= m < 15:
        setLetters(0,5,3,new_layout)
    elif 15 <= m < 20:
        setLetters(2,3,7,new_layout)
    elif 20 <= m < 30:
        setLetters(1,0,6,new_layout)
        if 25 <= m:
            setLetters(1,7,4,new_layout)
    elif 30 <= m < 35:
        setLetters(3,0,4,new_layout)
    elif 35 <= m < 45:
        setLetters(1,0,6,new_layout)
        if  m < 40:
            setLetters(1,7,4,new_layout)
    elif 45 <= m < 50:
        setLetters(2,3,7,new_layout)
    elif 50 <= m < 55:
        setLetters(0,5,3,new_layout)
    elif 55 <= m < 60:
        setLetters(1,7,4,new_layout)

    for i in range(0,m%5):
        setLetters(11 , i , 1 , new_layout)

    if m > 30:
        h = (h+1)%12
    
    if h==0:
        setLetters(8,0,6, new_layout)
    elif h==1:
        setLetters(7,5,3,new_layout)
    elif h==2:
        setLetters(7,3,3,new_layout)
    elif h==3:
        setLetters(5,0,5,new_layout)
    elif h==4:
        setLetters(5,5,4,new_layout)
    elif h==5:
        setLetters(9,6,4,new_layout)
    elif h==6:
        setLetters(7,0,3,new_layout)
    elif h==7:
        setLetters(9,0,5,new_layout)
    elif h==8:
        setLetters(8,5,5,new_layout)
    elif h==9:
        setLetters(6,6,4,new_layout)
    elif h==10:
        setLetters(7,8,3,new_layout)
    elif h==11:
        setLetters(6,1,6,new_layout)

    return new_layout