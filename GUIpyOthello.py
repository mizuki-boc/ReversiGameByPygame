import pygame
from pygame.locals import *
import sys
import numpy as np
import readchar
import os

def main():
    game = Othello()
    while True:
        game.display()


class Othello():
    def __init__(self):
        #変数初期化
        self.none = 0
        self.black = 1
        self.white = -1
        self.turn = self.black
        self.cells = np.zeros((8,8))
        self.cells[3][4] = self.cells[4][3] = self.black
        self.cells[3][3] = self.cells[4][4] = self.white
        self.cellsPosX = range(25,700,80)
        self.cellsPosY = range(25+2,700,80)
        #screenWidth,Height
        (swidth,sheight) = (680+300,680)#縁20,1マス80
        pygame.init()
        #イメージロード
        self.screen = pygame.display.set_mode((swidth,sheight))
        self.bg = pygame.image.load("pyOthelloImages/pyOthelloBoard2.png").convert_alpha()
        #self.cursor = pygame.image.load("pyOthelloImages/pyOthelloCursor.png").convert_alpha()
        self.blackImage = pygame.image.load("pyOthelloImages/pyOthelloB2G.png").convert_alpha()
        self.whiteImage = pygame.image.load("pyOthelloImages/pyOthelloW2G.png").convert_alpha()
        self.InfoImage = pygame.image.load("pyOthelloImages/pyOthelloInfo2.png").convert_alpha()
        self.CWImage = pygame.image.load("pyOthelloImages/pyOthelloCW.png").convert_alpha()
        self.CBImage = pygame.image.load("pyOthelloImages/pyOthelloCB.png").convert_alpha()
        self.n0Image = pygame.image.load("pyOthelloImages/pyOthello0.png").convert_alpha()
        self.n1Image = pygame.image.load("pyOthelloImages/pyOthello1.png").convert_alpha()
        self.n2Image = pygame.image.load("pyOthelloImages/pyOthello2.png").convert_alpha()
        self.n3Image = pygame.image.load("pyOthelloImages/pyOthello3.png").convert_alpha()
        self.n4Image = pygame.image.load("pyOthelloImages/pyOthello4.png").convert_alpha()
        self.n5Image = pygame.image.load("pyOthelloImages/pyOthello5.png").convert_alpha()
        self.n6Image = pygame.image.load("pyOthelloImages/pyOthello6.png").convert_alpha()
        self.n7Image = pygame.image.load("pyOthelloImages/pyOthello7.png").convert_alpha()
        self.n8Image = pygame.image.load("pyOthelloImages/pyOthello8.png").convert_alpha()
        self.n9Image = pygame.image.load("pyOthelloImages/pyOthello9.png").convert_alpha()
        self.WinImage = pygame.image.load("pyOthelloImages/pyOthelloWin.png").convert_alpha()
        self.GSImage = pygame.image.load("pyOthelloImages/pyOthelloGS.png").convert_alpha()
        pygame.display.set_caption("pyOthello")
        self.rect_bg = self.bg.get_rect()
        self.rect_black = self.blackImage.get_rect()
        self.rect_white = self.whiteImage.get_rect()
        #self.rect_info = self.InfoImage.get_rect()
        #self.rect_white.center = (self.sx,self.sy)
    def display(self):
        #盤面描画
        pygame.display.update()
        pygame.time.wait(30)
        self.screen.fill((150,150,150))#グレー
        self.screen.blit(self.bg,self.rect_bg)
        self.screen.blit(self.InfoImage,(690,100))
        if self.turn == self.black:
            self.screen.blit(self.CBImage,(720,127))
        elif self.turn == self.white:
            self.screen.blit(self.CWImage,(720,127))
        bnum = np.count_nonzero(self.cells == self.black)
        wnum = np.count_nonzero(self.cells == self.white)
        bnum10 = bnum // 10
        bnum1 = bnum - 10 * bnum10
        wnum10 = wnum // 10
        wnum1 = wnum - 10 * wnum10
        fn = "pyOthelloImages/pyOthello"
        #白は10のくらいは800,300,1のくらいは850,300
        #黒は10のくらいは800,240,1のくらいは850,240
        #if wnum1 == 1: self.screen.blit(pygame.image.load(fn+"0.png").convert_alpha(),(850,240))

        if bnum10 == 0: pass
        if bnum10 == 1: self.screen.blit(pygame.image.load(fn+"1.png").convert_alpha(),(800,240))
        if bnum10 == 2: self.screen.blit(pygame.image.load(fn+"2.png").convert_alpha(),(800,240))
        if bnum10 == 3: self.screen.blit(pygame.image.load(fn+"3.png").convert_alpha(),(800,240))
        if bnum10 == 4: self.screen.blit(pygame.image.load(fn+"4.png").convert_alpha(),(800,240))
        if bnum10 == 5: self.screen.blit(pygame.image.load(fn+"5.png").convert_alpha(),(800,240))
        if bnum10 == 6: self.screen.blit(pygame.image.load(fn+"6.png").convert_alpha(),(800,240))
        if bnum10 == 7: self.screen.blit(pygame.image.load(fn+"7.png").convert_alpha(),(800,240))
        if bnum10 == 8: self.screen.blit(pygame.image.load(fn+"8.png").convert_alpha(),(800,240))
        if bnum10 == 9: self.screen.blit(pygame.image.load(fn+"9.png").convert_alpha(),(800,240))
        if bnum1 == 0: self.screen.blit(pygame.image.load(fn+"0.png").convert_alpha(),(850,240))
        if bnum1 == 1: self.screen.blit(pygame.image.load(fn+"1.png").convert_alpha(),(850,240))
        if bnum1 == 2: self.screen.blit(pygame.image.load(fn+"2.png").convert_alpha(),(850,240))
        if bnum1 == 3: self.screen.blit(pygame.image.load(fn+"3.png").convert_alpha(),(850,240))
        if bnum1 == 4: self.screen.blit(pygame.image.load(fn+"4.png").convert_alpha(),(850,240))
        if bnum1 == 5: self.screen.blit(pygame.image.load(fn+"5.png").convert_alpha(),(850,240))
        if bnum1 == 6: self.screen.blit(pygame.image.load(fn+"6.png").convert_alpha(),(850,240))
        if bnum1 == 7: self.screen.blit(pygame.image.load(fn+"7.png").convert_alpha(),(850,240))
        if bnum1 == 8: self.screen.blit(pygame.image.load(fn+"8.png").convert_alpha(),(850,240))
        if bnum1 == 9: self.screen.blit(pygame.image.load(fn+"9.png").convert_alpha(),(850,240))
        if wnum10 == 0: pass
        if wnum10 == 1: self.screen.blit(pygame.image.load(fn+"1.png").convert_alpha(),(800,300))
        if wnum10 == 2: self.screen.blit(pygame.image.load(fn+"2.png").convert_alpha(),(800,300))
        if wnum10 == 3: self.screen.blit(pygame.image.load(fn+"3.png").convert_alpha(),(800,300))
        if wnum10 == 4: self.screen.blit(pygame.image.load(fn+"4.png").convert_alpha(),(800,300))
        if wnum10 == 5: self.screen.blit(pygame.image.load(fn+"5.png").convert_alpha(),(800,300))
        if wnum10 == 6: self.screen.blit(pygame.image.load(fn+"6.png").convert_alpha(),(800,300))
        if wnum10 == 7: self.screen.blit(pygame.image.load(fn+"7.png").convert_alpha(),(800,300))
        if wnum10 == 8: self.screen.blit(pygame.image.load(fn+"8.png").convert_alpha(),(800,300))
        if wnum10 == 9: self.screen.blit(pygame.image.load(fn+"9.png").convert_alpha(),(800,300))
        if wnum1 == 0: self.screen.blit(pygame.image.load(fn+"0.png").convert_alpha(),(850,300))
        if wnum1 == 1: self.screen.blit(pygame.image.load(fn+"1.png").convert_alpha(),(850,300))
        if wnum1 == 2: self.screen.blit(pygame.image.load(fn+"2.png").convert_alpha(),(850,300))
        if wnum1 == 3: self.screen.blit(pygame.image.load(fn+"3.png").convert_alpha(),(850,300))
        if wnum1 == 4: self.screen.blit(pygame.image.load(fn+"4.png").convert_alpha(),(850,300))
        if wnum1 == 5: self.screen.blit(pygame.image.load(fn+"5.png").convert_alpha(),(850,300))
        if wnum1 == 6: self.screen.blit(pygame.image.load(fn+"6.png").convert_alpha(),(850,300))
        if wnum1 == 7: self.screen.blit(pygame.image.load(fn+"7.png").convert_alpha(),(850,300))
        if wnum1 == 8: self.screen.blit(pygame.image.load(fn+"8.png").convert_alpha(),(850,300))
        if wnum1 == 9: self.screen.blit(pygame.image.load(fn+"9.png").convert_alpha(),(850,300))

        #cellsを元に石描画
        for i in range(8):
            for j in range(8):
                if self.cells[i][j] == self.black:
                    self.screen.blit(self.blackImage,(self.cellsPosX[i],self.cellsPosY[j]))
                elif self.cells[i][j] == self.white:
                    self.screen.blit(self.whiteImage,(self.cellsPosX[i],self.cellsPosY[j]))
                else:
                    pass

        #ゲーム終了判断
        gsblack = True
        gswhite = True
        gamesetflag = False
        for color in [self.black, self.white]:
            for i in range(8):
                for j in range(8):
                    gameflag = putcheck(self.cells,color,j,i,False)
                    if gameflag[0] == True:
                        #一箇所でも置けるところがある時,ゲームセットではない
                        if color == self.white:
                            gswhite = False
                        elif color == self.black:
                            gsblack = False
                        break
                else:
                    continue
                break
        #print("black->",gsblack)
        #print("white->",gswhite)
        if gsblack == True and gswhite == False:
            self.turn = self.white
        if gsblack == False and gswhite == True:
            self.turn = self.black
        if gswhite == True and gsblack == True:
            if bnum == wnum:
                print("Draw!")
            else:
                #print("Game Set!")
                self.screen.blit(pygame.image.load(fn+"GS.png").convert_alpha(),(850,400))
            gamesetflag = True
        for event in pygame.event.get():
            #クリックされた時
            if event.type == MOUSEBUTTONDOWN:
                posMX,posMY = pygame.mouse.get_pos()
                for i in range(8):
                    for j in range(8):
                        if self.cellsPosX[i] <= posMX and posMX <= self.cellsPosX[i+1] and self.cellsPosY[j] <= posMY and posMY <= self.cellsPosY[j+1]:
                            #置く処理
                            #self.cells[i][j] = self.turn
                            returncheck = putcheck(self.cells,self.turn,i,j,False)
                            if returncheck[0]:
                                putcheck(self.cells,self.turn,i,j,True)
                                self.turn = -self.turn
                            else:
                                print("cant put")
                                #置けない時
            #閉じるでquit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#チェック関数,Trueでひっくり返す．Falseはチェックのみ
def putcheck(_cells,_turn,_x,_y,_returnflag = False):
    black = 1
    white = -1
    none = 0
    board = 8
    dirX = [-1,0,1]
    dirY = [-1,0,1]
    returncheck = False
    #選択セルに自分の石もしくは相手の石があれば，checkしない
    if _cells[_x][_y] == 1 or _cells[_x][_y] == -1:
        pass
    else:
        #check開始
        for i in dirX:
            for j in dirY:
                if _x + i >= 0 and _x + i <= 7 and _y + j >= 0 and _y + j <= 7:
                    if _cells[_x + i][_y + j] == -_turn:
                        #隣に相手の石がある時->置ける可能性
                        for n in range(2,board):
                            if _x + i * n >= 0 and _x + i * n <= 7 and _y + j * n >= 0 and _y + j * n <= 7:
                                if _cells[_x + i * n][_y + j * n] == _turn:
                                    #２個以上先に自分の石->ひっくり返す
                                    if _returnflag:
                                        #ひっくり返し処理
                                        for n2 in range(n,0,-1):
                                            _cells[_x + i * n2][_y + j * n2] = _turn
                                        _cells[_x][_y] = _turn
                                    returncheck = True
                                    break
                                elif _cells[_x + i * n][_y + j * n] == none:
                                    #２個以上先に石無し
                                    break
                    else:
                        #隣に自分の石or石なし->置けない
                        pass
    #ひっくり返せる時はTrueを返す
    return returncheck,_cells


if __name__ == "__main__":
    main()
