from pygame.locals import *
import pygame as pg
import sys
import random

def main():
    pg.init()
    scrn_sfc = pg.display.set_mode((1500, 800))
    scrn_rct = scrn_sfc.get_rect()
    pg.display.set_caption("逃げろ!こうかとん")
    #screen = pg.display.get_surface()
    bg_sfc = pg.image.load("pg_bg.jpg")
    #bg_sfc = pg.transform.rotozoom(bg_sfc, 0, 1.0)
    bg_rct = bg_sfc.get_rect()
    #bg_rct.center = 700, 400
    
    #こうかとんの描写
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    
    #爆弾の描写
    bomb_sfc = pg.Surface((100, 100))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    #2つ目の爆弾
    bomb2_sfc = pg.Surface((100, 100))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    clock = pg.time.Clock()
    
    vx1, vy1 = +1, +1
    vx2, vy2 = +1, +1
    
    count = 0
    
    while(1):
        pg.display.update()
        #pg.time.wait(30)
        
        
        #pg.display.update()
        
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        #爆弾の移動
        #画面外に出ないように制御
        if((bomb_rct.left < scrn_rct.left) or (scrn_rct.right < bomb_rct.right)):
            vx1 *= -1.05
        if((bomb_rct.top < scrn_rct.top) or (scrn_rct.bottom < bomb_rct.bottom)):
            vy1 *= -1.05
        bomb_rct.move_ip(vx1, vy1)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        #2つ目の爆弾の移動
        if(bomb2_rct.left < scrn_rct.left):
            bomb2_rct.centerx += 1500
        if (scrn_rct.right < bomb2_rct.right):
            bomb2_rct.centerx -=1500
        if(bomb2_rct.top < scrn_rct.top):
            bomb2_rct.centery += 800
        if(scrn_rct.bottom < bomb2_rct.bottom):
            bomb2_rct.centery -=800
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)
        
        if(count == 10):
            scrn_sfc.blit(bomb_sfc, bomb_rct)
            count = 0
        
        
        #矢印キーによるこうかとんの移動
        #こうかとんが画面外に出ないようにする
        pressed = pg.key.get_pressed()
        if ((pressed[K_UP]) and (tori_rct.centery > 50)):
            tori_rct.move_ip(0, -5)
        elif ((pressed[K_DOWN]) and (tori_rct.centery < 750)):
            tori_rct.move_ip(0, 5)
        elif ((pressed[K_LEFT]) and (tori_rct.centerx > 50)):
            tori_rct.move_ip(-5, 0)
        elif ((pressed[K_RIGHT]) and (tori_rct.centerx < 1450)):
            tori_rct.move_ip(5, 0)
        
        #爆弾とこうかとんの衝突    
        if ((tori_rct.colliderect(bomb_rct)) or tori_rct.colliderect(bomb2_rct)):
            return
        
        #終了時
        clock.tick(1000)
        pg.event.pump()
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
                    
    
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
