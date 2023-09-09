import math
ai, h, = 'x', 'o'
scores = {
    'x': 10,
    'o': -10,
    'tie': 0
}
def f(board, n, radek, sloupec):
    open_spots = 0
    for i in range(radek, n + radek):
        for j in range(sloupec, sloupec + n):
            if board[i][j] == "_": open_spots += 1
    return open_spots
def print_board(d):
    print('   1 2 3 4 5 6 7 8')
    for i in range(len(d)):
        print(i+1, end='| ')
        for j in range(len(d)):
            print(d[i][j], end=' ')
        print()
def poddoska(radek, sloupec, doska):
    rozmer = len(doska)-1
    sp = {}
    if radek + 2 <= rozmer and sloupec + 2 <= rozmer:
        sp[f(board, 3, radek, sloupec)] = (radek, sloupec)

    if radek+2 <= rozmer and sloupec + 1 <= rozmer and sloupec - 1 >= 0:
        sp[f(board, 3, radek, sloupec-1)] = (radek, sloupec-1)

    if radek + 2 <= rozmer and sloupec-2 >= 0:
        sp[f(board, 3, radek, sloupec-2)] = (radek, sloupec-2)

    if radek-1>= 0 and radek+1<=rozmer and sloupec+2 <= rozmer:
        sp[f(board, 3, radek-1, sloupec)] = (radek-1, sloupec)

    if radek-1>= 0 and radek+1<=rozmer and sloupec + 1 <= rozmer and sloupec - 1 >= 0:
        sp[f(board, 3, radek-1, sloupec-1)] = (radek-1, sloupec-1)

    if radek-1>= 0 and radek+1<=rozmer and sloupec-2 >= 0:
        sp[f(board, 3, radek-1, sloupec-2)] = (radek-1, sloupec-2)

    if radek-2>=0 and sloupec+2<=rozmer:
        sp[f(board, 3, radek-2, sloupec)] = (radek-2, sloupec)

    if radek - 2 >= 0 and sloupec + 1 <= rozmer and sloupec - 1 >= 0:
        sp[f(board, 3, radek-2, sloupec-1)] = (radek-2, sloupec-1)

    if radek - 2 >= 0 and sloupec - 2 >= 0:
        sp[f(board, 3, radek-2, sloupec-2)] = (radek-2, sloupec-2)
    if 0 in sp: sp.pop(0, None)
    if sp: return sp[min(sp)]
    return None, None
def check_win_3(board, n, radek, sloupec):
    first = board[radek][sloupec]
    diagonal = first != "_"
    for i in range(n):
        if board[radek+i][sloupec+i] != first:
            diagonal = False
            break
    if diagonal:
        return (first, radek+i, sloupec+i, 'diag1')

    first = board[radek+n-1][sloupec]
    back_diag = first != "_"
    for i in range(n):
        if board[radek+n-1-i][sloupec + i] != first:
            back_diag = False
            break
    if back_diag:
        return (first, radek+n-1-i, sloupec+i, 'diag2')

    for i in range(radek, n + radek):
        first = board[i][sloupec]
        sideways = first != "_"
        for j in range(sloupec, sloupec + n):
            if board[i][j] != first:
                sideways = False
        if sideways:
            return (first, i, j, 'radek')

    for i in range(sloupec, n + sloupec):
        first = board[radek][i]
        sideways = first != "_"
        for j in range(radek, radek + n):
            if board[j][i] != first:
                sideways = False
        if sideways:
            return (first, j, i, 'sloupec')

    open_spots = 0
    for i in range(radek, n + radek):
        for j in range(sloupec, sloupec + n):
            if board[i][j] == "_":
                open_spots += 1
    if open_spots == 0:
        return ("tie", 0)
    return
def minimax(board, depth, is_max, n, radek, sloupec, alpha=-math.inf, beta=math.inf):
    winner = check_win_3(board, 3, radek, sloupec)  
    if winner:

        return scores[winner[0]]
    if is_max:
        best_score = -math.inf
        for i in range(radek, radek+n):
            for j in range(sloupec, sloupec+n):
                if board[i][j] == "_":
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False, n, radek, sloupec, alpha, beta)
                    board[i][j] = "_"
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(radek, radek+n):
            for j in range(sloupec, sloupec+n):
                if board[i][j] == "_":
                    board[i][j] = h
                    score = minimax(board, depth + 1, True, n, radek, sloupec, alpha, beta)
                    board[i][j] = "_"
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score
def best_move(board, n, radek, sloupec):
    #print(radek, sloupec)
    best_score = -math.inf
    move = (-1, -1)
    for i in range(radek, n+radek):
        for j in range(sloupec, sloupec+n):
            if board[i][j] == "_":
                board[i][j] = ai
                score = minimax(board, 0, False, n, radek, sloupec)
                board[i][j] = "_"
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = ai
    return board
def check_win_5(board, n, x=None, y=None, pod=False):
    rs = []
    slh = {}
    if not pod: rs = [[0, 0], [1, 0], [0, 1],[2, 0], [0, 2], [3, 0], [0, 3]]

    if pod and -3<=y-x<=3:
        if y-x<=0:
            rs = [[abs(y-x), 0]]
        else: rs = [[0, y-x]]

    for para in rs:
        radek, sloupec = para[0], para[1]
        for k in range(radek, n-sloupec-2):
            count = 0
            if board[k][sloupec+k-radek] in 'xo':
                first = board[k][sloupec+k-radek]
                for i in range(k, n-sloupec):
                    if board[i][sloupec+i-radek] != first: break
                    else: count += 1
            if pod and count >= 2:
                x1, y1 = i, sloupec+i- radek
                if first == h and (board[x1][y1] == '_' or board[x1-count][y1-count]=='_' or board[x1-count-1][y1-count-1]=='_'): slh[count] = ('diag1', i, sloupec+i-radek, count, first)
            if not pod and count >= 5: return first

    if not pod: rs = [[7, 0], [7, 1], [7, 2], [7, 3], [6, 0], [5, 0], [4, 0]]
    if pod and 4<=y+x<=10:
        if x+y > 7: rs = [[x+y-(y+x)%7, (y+x)%7]]
        else: rs = [[x+y, 0]]
    for para in rs:
        radek, sloupec = para[0], para[1]
        for k in range(radek, sloupec-1, -1):
            count = 0
            if board[k][sloupec+radek-k] in 'xo':
                first = board[k][sloupec+radek-k]
                for i in range(k, sloupec-1, -1):
                    if board[i][sloupec+radek-i] != first: break
                    else: count += 1
            if pod and count >= 2:
                x1, y1 = i, sloupec+radek-i
                if first == h and (board[x1][y1] == '_' or board[x1+count][y1-count]=='_' or (x1+count+1<8 and  board[x1+count+1][y1-count-1]=='_')): slh[count] = ('diag2', i, sloupec - i + radek, count, first)
            if not pod and count >= 5: return first

    radek, sloupec = 0, 0
    for i in range(radek, n+radek):   #RADKY spravne
        if pod: i = x
        for j in range(sloupec, sloupec + n-2):
            count = 0
            if board[i][j] in 'xo':
                first = board[i][j]
                for k in range(j, sloupec+n):
                    if board[i][k] != first: break
                    else: count += 1
                if pod and count >= 2:
                    x1, y1 = i, k
                    if first == h and (board[x1][y1] == '_' or board[x1][y1-count]=='_' or board[x1][y1-count-1]=='_'): slh[count] = ('radek', i, k, count, first)
                if not pod and count >= 5: return first


    radek, sloupec = 0, 0
    for i in range(sloupec, sloupec+n):   #SLOUPCE spravne
        if pod: i = y
        for j in range(radek, radek+n-2):
            count = 0
            if board[j][i] in 'xo':
                first = board[j][i]
                for k in range(j, radek+n):
                    if board[k][i] != first: break
                    else: count += 1
                if pod and count >= 2:
                    x1, y1 = k, i
                    if first == h and (board[x1][y1] == '_' or board[x1-count][y1]=='_' or board[x1-count-1][y1]=='_'): slh[count] = ('sloupec', k, i, count, first)
                if not pod and count >= 5: return first

    if f(board, 8, 0, 0) == 0:
        return 'tie'

    if pod and slh:
        return slh[max(slh)]
    return
def vyhra_35(board, radek, sloupec): 
    result = check_win_5(board, 8, radek, sloupec, True)
    kde, x, y, kolik, kdo = result
    if board[x][y] == '_':
        return x, y

    if kde == 'diag1':
        if 0<=x-kolik<=7 and 0<=y-kolik<=7 and board[x-kolik][y-kolik] == '_':   
            return x-kolik, y-kolik
        if 0<=x-kolik-1<=7 and 0<=y-kolik-1<=7 and board[x-kolik-1][y-kolik-1] == '_':
            return x-kolik-1, y-kolik-1

    if kde == 'diag2':
        if 0<=x+kolik<=7 and 0<=y-kolik<=7and board[x+kolik][y-kolik] == '_':
            return x+kolik, y-kolik
        if 0<=x+kolik+1<=7 and 0<=y-kolik-1<=7 and board[x+kolik+1][y-kolik-1] == '_':
            return x+kolik+1, y-kolik-1

    if kde == 'radek':
        if 0<=y-kolik<=7 and board[x][y-kolik] == '_':
            return x, y-kolik
        if 0<=y-kolik-1<=7 and board[x][y-kolik-1] == '_':
            return x, y-kolik-1

    if kde == 'sloupec':
        if 0<=x-kolik-1<=7 and board[x-kolik][y] == '_':
            return x-kolik, y
        if 0<=x-kolik-1<=7 and board[x-kolik-1][y] == '_':
            return x-kolik-1, y
    return 'nic'
def vyhra_ai(board, kdo):
    for i in range(8):
        for j in range(8):
            if board[i][j] == '_':
                board[i][j] = kdo
                if check_win_5(board, 8) == kdo:
                    return i, j
                board[i][j] = '_'
    return


def vvod():
    ls = []
    while len(ls) != 2 or board[ls[0]-1][ls[1]-1] != '_':
        line = input('napište souřadnice pozice\n')
        if line == 'q':
            return 'q', 'q'
        ls = []
        for i in line:
            if i in '12345678': ls.append(int(i))

        if len(ls) != 2: print('něco není správné, napište ještě jednou, \nmusí být dvě čísla, každé v rozmezí 1-8')
        elif board[ls[0]-1][ls[1]-1] != '_': print('Zkuste znovu, tohle políčko je obsaženo')
    return ls[0]-1, ls[1]-1
def exit():
    if x != 'q': return True
    elif x == 'q': return False
def end_(result):
    if result == h: return 'Vy jste vyhrali :)'
    if result == ai: return 'Vy jste prohrali :('
    if result == 'tie':
        return 'Remíza :o'


x = ''
r = 8
board = [['_' for _ in range(r)] for _ in range(r)]


print('\nPIŠKVORKY 8*8 na 5 symbolů v řadě. '
      '\nVyhrává hráč, který jako první vytvoří nepřerušenou řadu pěti svých značek\n'
      '\nVždycky pište souřadnice pozice, kam chcete dát o (první je číslo řádku,'
      '\ndruhé číslo je sloupec) a zmačkněte enter\n')


print('CHCETE-LI UKONČIT HRU, NAPIŠTE "q" A ZMAČKNĚTE ENTER')


def hra():
    while exit():
        print_board(board)
        end = check_win_5(board, 8)
        if end:
            print(end_(end))
            break

        x, y = vvod()
        if x == 'q':
            print('hra se skončila předčásně')
            break
        board[x][y] = h

        ###chody pocitace
        end_ai = vyhra_ai(board, ai)
        if end_ai:
            board[end_ai[0]][end_ai[1]] = ai

        end = check_win_5(board, 8)

        if end:
            print_board(board)
            print(end_(end))
            break

        rjad, stolb = poddoska(x, y, board)
        end1 = check_win_5(board, 8, x, y, True)

        temer = vyhra_ai(board, h)
        if temer:
            board[temer[0]][temer[1]] = ai

        elif end1:

            koor = vyhra_35(board, x, y)
            if koor != 'nic':
                board[koor[0]][koor[1]] = ai
            else:
                best_move(board, 3, rjad, stolb)
        else:
            if rjad != None and stolb != None:
                best_move(board, 3, rjad, stolb)
            else:
                for i in range(len(board)):
                    for j in range(len(board)):
                        if board[i][j] == '_':
                            board[i][j] = ai
                            break


while True:
    hra()
    a = input('POKUD CHCETE POKRAČOVAT A HRÁT ZNOVU, ZMAČKNĚTE ENTER,\nPOKUD CHCETE UKONČIT, ZMAČKNĚTE "q" a ENTER ')
    if a == 'q': break
    r = 8
    board = [['_' for _ in range(r)] for _ in range(r)]
