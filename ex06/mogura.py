import pygame as pg
import sys
from pygame.locals import *
from pygame.time import Clock
from random import randint

#結果のウィンドウを表示する
def result():
          
    pg.init()
    font4 = pg.font.SysFont("hg正楷書体pro", 40)  
    pg.display.set_mode((700, 400))
    screen2 = pg.display.get_surface()
    pg.display.set_caption("結果")
    
    
   
    while(1):
        screen2.fill((255,255,255))
        
        #何回たたいたのかを表示する
        text4 = font4.render('点数 : {}点'.format(score), True, (0, 0, 0))
        screen2.blit(text4, [200, 100] )
        
        
        
        #10回以上たたいた時とそうでないときでクリアしたかどうかを条件分岐させる
        if score < 10:
            #クリアしなかったときの表示
            text5 = font4.render('ゲームオーバー', True, (0, 0, 0))
            screen2.blit(text5, [200, 200] )
        else :
            #クリアしたときの表示
            button = pg.Rect(200, 300, 240, 40) 
            text7 = font4.render('次のレベルへ', True, (0, 0, 0))
            pg.draw.rect(screen2, (0, 255, 0), button)
            text6 = font4.render('ゲームクリア', True, (0, 0, 0))
            screen2.blit(text6, [200, 200] )
            screen2.blit(text7, [200, 300])
            
            
        for event in pg.event.get():
            #閉じるのイベントが実行されたとき
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            #次のレベルへのbuttonが押されたとき
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    #print("button was pressed")
                    return
        pg.display.update()
        
def create(level):
    pg.init()
    pg.display.set_mode((1500, 800))
    screen = pg.display.get_surface()
    pg.display.set_caption("もぐらたたき")
    
    #プログラム内の時間管理に役立つオブジェクトを作成します
    #Clockオブジェクトを使用すれば、ゲームのフレームレート制御など様々な処理を行うことができます。
    cl = pg.time.Clock()
    
    #モグラの画像を描写
    img1 = pg.image.load("data/mogura.png")
    rect_img1 = img1.get_rect() 
    rect_img1.center = (750, 400)
    
    #フォントの用意をする
    #pygame.font.SysFont(引数1, 引数2), 引数1はフォント名、引数2はサイズ
    #フォント名をNoneにするとデフォルトフォントになる
    #日本語描画は「hg正楷書体pro」
    font1 = pg.font.SysFont(None, 78)
    font2 = pg.font.SysFont(None, 45)
    font3 = pg.font.SysFont(None, 30)
    
    
    #テキストオブジェクトの作成
    #（テキストオブジェクト）＝ （フォントオブジェクト）.render("文字列", （滑らかにするか？T/F）, (文字色RGB))
    text1 = font1.render("Click!", True, (204, 102, 112))
    text2 = font2.render("+1", True, (0, 0, 0)) #スコアしたときに表示するテキスト
    
    #画像の初期位置
    imgx = 750
    imgy = 400
    
    #画像の移動する速さ
    vx = randint(-level, level)
    vy = randint(-level, level)
    
    #押されたときに+1と表示するためのフレーム数
    display = 0
    n_frames = 0
    #制限時間
    TIME_END = 10
    #得点
    global score
    score = 0
    
    while (1):
        screen.fill((0, 255, 0)) 
        screen.blit(img1, (imgx, imgy))
        
        #四角形のオブジェクトを生成
        #当たったかどうかの判定に用いる
        img1_Rect = pg.Rect((imgx, imgy), rect_img1.size)
        
        #テキストを描画
        #第一引数はテキストオブジェクト、第二引数は表示位置（左上からのピクセル値）
        screen.blit(text1, [170, 30])

        #残り時間を計測
        rest = TIME_END - (n_frames / 30)
        #テキストオブジェクトの作成
        #（テキストオブジェクト）＝ （フォントオブジェクト）.render("文字列", （滑らかにするか？T/F）, (文字色RGB))
        #残り時間は小数第一位まで表示する
        text4 = font3.render('time: {}'.format(round(rest,1)), True, (0, 0, 0))
        #テキストを描画            
        screen.blit(text4,[350,60])
        
        for event in pg.event.get():
            #閉じるのイベントが実行されたとき
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            #マウスボタンが押されるかつ左クリック（ボタン番号１）
            if (n_frames < 30 * TIME_END) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                #押されたところの点座標が画像の描写範囲内にあったら
                if img1_Rect.collidepoint(event.pos):
                    
                    #押されたら9フレーム表示する
                    display = 9
                    #得点を一点加える
                    score += 1
                    
        #テキストオブジェクトの作成
        #（テキストオブジェクト）＝ （フォントオブジェクト）.render("文字列", （滑らかにするか？T/F）, (文字色RGB))
        #得点を表示する
        text3 = font3.render('score : {}'.format(score), True, (0, 0, 0))
        #テキストを描画
        screen.blit(text3, [350, 40] )
        
        if display > 0:
            #マウスカーソルの位置情報を取得する
            pos = pg.mouse.get_pos()
            #マウスカーソルの位置に表示
            screen.blit(text2, pos)
            display -= 1
        
        pg.display.update()
        
        if n_frames < 30 * TIME_END:
             n_frames += 1

        
        #モグラを移動させウィンドウから飛び出さないよう制御する
        imgx += vx
        imgy += vy
        
        if imgy <= 200:
            vy *= -1
        
        if imgx >= 1000:
            vx *= -1
            
        if imgy >= 600:
            vy *= -1
        
        if imgx <= 300:
            vx *= -1
            
        
        #プログラムは一秒毎に30フレームを超える速度で実行されないようにする
        cl.tick(30)
        
        #残り時間が0になったら終了する
        if rest == 0:
            break
        


def main():
    #難易度を表す変数levelの初期化
    level = 1
    while(1):
        create(level)
        result()
        #以下はクリアしたときにのみ実行される
        level += 1
        
        
        
    
    
if __name__ == "__main__":
    main()
