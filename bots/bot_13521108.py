from game import Board

class Bot13521108(object):
    """
    Bot player 13521108
    """
    # Ide solusi yang dibangun terinspirasi dari solusi bot Galaxio
    # Thanks to my team, 2B1Reuni!

    def __init__(self):
        self.player = None
        self.NIM = "13521108"

    def set_player_ind(self, p):
        self.player = p
        self.mult = 0

    def get_action(self, board):
        location = self.get_input(board)
        try:
            if isinstance(location, str):  # for python3
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            move = self.get_action(board)
        return move

    def __str__(self):
        return "Bot {}".format(self.NIM)
    
    # Melakukan kalkulasi nilai papan setelah meletakkan sebuah simbol
    def board_score(self, row, col, playerval, board: Board) -> int:
        # Pemeriksaan 4 arah, horizontal, vertikal, diagonal, dan reverse diagonal
        values = [0, 0, 0, 0]
        
        # Definisikan beberapa makro
        sign = 0
        panjang = int(board.width)
        lebar = int(board.height)
        if (self.player == 1):
            if (playerval == 1) : sign = 1
            else : sign = 2
        else :
            if (playerval == 1) : sign = 2
            else : sign = 1
        
        # Pemeriksaan horizontal
        # Cek kiri
        for i in range(col - 1, -1, -1):
            if board.states.get(row * panjang + i) == sign:
                values[0] += playerval if (self.player == 1) else -1 * playerval
            else: break
        
        # Cek kanan
        for j in range(col + 1, panjang):
            if board.states.get(row * panjang + j) == sign:
                values[0] += playerval if (self.player == 1) else -1 * playerval
            else: break
            
        # Pemeriksaan vertikal
        # Cek bawah
        for i in range(row - 1, -1, -1):
            if board.states.get(i * panjang + col) == sign:
                values[1] += playerval if (self.player == 1) else -1 * playerval
            else: break
        
        # Cek atas
        for j in range(row + 1, lebar):
            if board.states.get(j * panjang + col) == sign:
                values[1] += playerval if (self.player == 1) else -1 * playerval
            else: break
            
        # Pemeriksaan diagonal
        # Cek diagonal kanan bawah
        i = 1
        while row - i >= 0 and col + i < panjang:
            if board.states.get((row - i) * panjang + (col + i)) == sign:
                values[2] += playerval if (self.player == 1) else -1 * playerval
            else: break
            i += 1

        # Cek diagonal kiri atas
        i = 1
        while row + i < lebar and col - i >= 0:
            if board.states.get((row + i) * panjang + (col - i)) == sign:
                values[2] += playerval if (self.player == 1) else -1 * playerval
            else: break
            i += 1
            
        # Pemeriksaan reverse diagonal
        # Cek diagonal kiri bawah
        j = 1
        while row - j >= 0 and col - j >= 0:
            if board.states.get((row - j) * panjang + (col - j)) == sign:
                values[3] += playerval if (self.player == 1) else -1 * playerval
            else: break
            j += 1

        # Cek diagonal kanan atas
        i = 1
        while row + i < lebar and col + i < panjang:
            if board.states.get((row + i) * panjang + (col + i)) == sign:
                values[3] += playerval if (self.player == 1) else -1 * playerval
            else: break
            i += 1
            
        # Pemeriksaan kondisi final, memperoleh nilai kembalian
        if sign == 1:
            return max(values[0], values[1], values[2], values[3]) + 1
        else:
            return min(values[0], values[1], values[2], values[3]) - 1
        
    # Melakukan pengecekan apakah area mungkin diagapai
    def isPassable (self, row, col) -> bool:
        return (row >= 0 and row <= 7 and col >= 0 and col <= 7)
    
    # Melakukan pengecekan apakah ada 4 disekitar karakter yang tergapai untuk dapat diblock
    def is4arround (self, row, col, board: Board) -> bool:
        if (self.isPassable(row + 4, col)):
            if (abs(self.board_score(row + 4, col, self.mult, board)) == 4) : return True
        if (self.isPassable(row - 4, col)):
            if (abs(self.board_score(row - 4, col, self.mult, board)) == 4) : return True
        if (self.isPassable(row, col + 4)):
            if (abs(self.board_score(row, col + 4, self.mult, board)) == 4) : return True
        if (self.isPassable(row, col - 4)):
            if (abs(self.board_score(row, col - 4, self.mult, board)) == 4) : return True
        if (self.isPassable(row + 4, col + 4)):
            if (abs(self.board_score(row + 4, col + 4, self.mult, board)) == 4) : return True
        if (self.isPassable(row + 4, col - 4)):
            if (abs(self.board_score(row + 4, col - 4, self.mult, board)) == 4) : return True
        if (self.isPassable(row - 4, col + 4)):
            if (abs(self.board_score(row - 4, col + 4, self.mult, board)) == 4) : return True
        if (self.isPassable(row - 4, col - 4)):
            if (abs(self.board_score(row - 4, col - 4, self.mult, board)) == 4) : return True
        return False
    
    # Mengecek apakah kemungkinan maksimum musuh galak (bisa 2 row barengan)
    def is3arroundmatres (self, row, col, matr) -> bool:
        if (self.isPassable(row + 3, col - 3) and self.isPassable(row + 3, col + 3)):
            if (matr[row + 3][col - 3] == 3 and matr[row + 3][col + 3] == 3) : return True
        if (self.isPassable(row + 3, col) and self.isPassable(row, col + 3)):
            if (matr[row + 3][col] == 3 and matr[row][col + 3] == 3) : return True
        if (self.isPassable(row + 3, col + 3) and self.isPassable(row - 3, col + 3)):
            if (matr[row + 3][col + 3] == 3 and matr[row - 3][col + 3] == 3) : return True
        if (self.isPassable(row, col + 3) and self.isPassable(row - 3, col)):
            if (matr[row][col + 3] == 3 and matr[row - 3][col] == 3) : return True
        if (self.isPassable(row - 3, col + 3) and self.isPassable(row - 3, col - 3)):
            if (matr[row - 3][col + 3] == 3 and matr[row - 3][col - 3] == 3) : return True
        if (self.isPassable(row - 3, col) and self.isPassable(row, col - 3)):
            if (matr[row - 3][col] == 3 and matr[row][col - 3] == 3) : return True
        if (self.isPassable(row - 3, col - 3) and self.isPassable(row + 3, col - 3)):
            if (matr[row - 3][col - 3] == 3 and matr[row + 3][col - 3] == 3) : return True
        if (self.isPassable(row, col - 3) and self.isPassable(row + 3, col)):
            if (matr[row][col - 3] == 3 and matr[row + 3][col] == 3) : return True
        return False

    # Proses pemilihan jalur - program utama
    def get_input(self, board: Board) -> str:
        """
            Parameter board merepresentasikan papan permainan. Objek board memiliki beberapa
            atribut penting yang dapat menjadi acuan strategi.
            - board.height : int (x) -> panjang papan
            - board.width : int (y) -> lebar papan
            Koordinat 0,0 terletak pada kiri bawah

            [x,0] [x,1] [x,2] . . . [x,y]                               
            . . . . . . . . . . . . . . .  namun perlu diketahui        Contoh 4x4: 
            . . . . . . . . . . . . . . .  bahwa secara internal        11 12 13 14 15
            . . . . . . . . . . . . . . .  sel-sel disimpan dengan  =>  10 11 12 13 14
            [2,0] [2,1] [2,2] . . . [2,y]  barisan interger dimana      5  6  7  8  9
            [1,0] [1,1] [1,2] . . . [1,y]  kiri bawah adalah nol        0  1  2  3  4
            [0,0] [0,1] [0,2] . . . [0,y]          

            - board.states : dict -> Kondisi papan. 
            Key dari states adalah integer sel (0,1,..., x*y)
            Value adalah integer 1 atau 2:
            -> 1 artinya sudah diisi player 1
            -> 2 artinya sudah diisi player 2
        """
        # 0. Deklarasi variabel
        mid_row = int(board.height / 2)
        mid_col = int(board.width / 2)
        # Koordinat solusi
        x = -1
        y = -1
        
        # 1. Menentukan apakah bot bermain duluan atau kedua
        # Kalo duluan ambil tengah - Greedy by centerpoint
        if (self.mult == 0):
            if (board.last_move == -1):
                x = mid_row
                y = mid_col
                self.mult = 1
                return f"{x},{y}"
            else : self.mult = -1
                
        matres1 = [[0 for i in range (board.width)] for j in range (board.height)]
        matres2 = [[0 for i in range (board.width)] for j in range (board.height)]
        
        # 2. Melakukan proses kalkulasi nilai dari masing-masing pemain
        # Nilai diri sendiri
        maxBotScore = -1
        count1 = 0
        for i in range (board.height - 1, -1, -1):
            for j in range (board.width):
                # Sudah terisi, lewati
                if board.states.get(i * board.width + j) is not None: continue
                # Ambil nilai
                curBotScore = self.board_score(i, j, self.mult, board)
                # Ubah jika negatif
                if ((self.mult == 1 and self.player == 2) or (self.mult == -1 and self.player == 1)) : curBotScore = -1 * curBotScore
                # Masukkan ke matres untuk dianalisis
                matres1[i][j] = curBotScore
                # Pemrosesan terhadap nilai max
                if (curBotScore > maxBotScore):
                    x = i
                    y = j
                    maxBotScore = curBotScore
                    count1 = 0
                elif (curBotScore == maxBotScore):
                    maxOppScore = self.board_score(x, y, -1 * self.mult, board)
                    curOppScore = self.board_score(i, j, -1 * self.mult, board)
                    if (abs(curOppScore) > abs(maxOppScore)):
                        x = i
                        y = j
                        maxBotScore = curBotScore
                        count1 = 0
                    count1 += 1
        
        # Nilai lawan
        koord_x = 0
        koord_y = 0
        maxOppScore = -1
        count2 = 0
        for i in range (board.height - 1, -1, -1):
            for j in range (board.width):
                # Sudah terisi, lewati
                if board.states.get(i * board.width + j) is not None: continue
                # Ambil nilai
                oppScore = abs(self.board_score(i, j, -1 * self.mult, board))
                # Masukkan ke matres untuk dianalisis
                matres2[i][j] = oppScore
                # Pemrosesan terhadap nilai max
                if (oppScore > maxOppScore):
                    koord_x = i
                    koord_y = j
                    maxOppScore = oppScore
                    count2 = 0
                elif (oppScore == maxOppScore):
                    maxObotScore = self.board_score(x, y, self.mult, board)
                    curObotScore = self.board_score(i, j, self.mult, board)
                    if (abs(curObotScore) <= abs(maxObotScore)):
                        koord_x = i
                        koord_y = j
                        maxOppScore = oppScore
                        count2 = 0
                    count2 += 1

        # Trigger points, turning position -> attack vs defense
        # 1. Kalo 2 2 nya lima, pilih based on turn biar cepetan menang
        if ((maxBotScore == 5) and (maxOppScore == 5)):
            if (self.player == 1):
                if (self.mult == 1):
                    x = koord_x
                    y = koord_y
                    return f"{x},{y}"
                else :
                    return f"{x},{y}"
            else:
                if (self.mult == 1):
                    return f"{x},{y}"
                else :
                    x = koord_x
                    y = koord_y
                    return f"{x},{y}"
        # 2. Kalo nilai botnya doang, gasin juga
        elif (maxBotScore == 5):
            return f"{x},{y}"
        # 3. Kalo nilai oppnya doang, larang keras
        elif (maxOppScore == 5):
            x = koord_x
            y = koord_y
            return f"{x},{y}"
        
        # 4. Cek kemungkinan 3 keserobot, cek dalam next if
        if (maxBotScore == 3):
            for i in range (board.height - 1, -1, -1):
                for j in range (board.width):
                    if (matres1[i][j] == 3):
                        if (self.is3arroundmatres(i, j, matres1)):
                            return f"{i},{j}"
        # 5. Kalo 2 2 nya 4, liat selisihnya, utamain yang lebih bisa diperjuangkan
        elif ((maxBotScore == 4) and (maxOppScore == 4)):
            if (self.is4arround(x, y, board)):
                return f"{x},{y}"
            else :
                if (abs(count1 - count2) <= 2):
                    x = koord_x
                    y = koord_y
                    return f"{x},{y}"
                else :
                    return f"{x},{y}"
        # 6. Kalo cuma botnya doang, gasin dulu
        elif (maxBotScore >= 4 and self.mult == -1):
            return f"{x},{y}"
        # 7. Hal yang sama cuma ini kalo dari sudut lain
        elif (maxOppScore >= 4 and self.mult == 1):
            x = koord_x
            y = koord_y
            return f"{x},{y}"
            
        # 8. Hasil eksekusi terakhir -- normal
        return f"{x},{y}"
    