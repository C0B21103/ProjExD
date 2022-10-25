from pygame.locals import *
import pygame as pg
import sys
def main():
    pg.init()
    scrn_sfc = pg.display.set_mode((1500, 800))
    pg.display.set_caption("逃げろ!こうかとん")
    #screen = pg.display.get_surface()
    bg_sfc = pg.image.load("pg_bg.jpg")
    #bg_sfc = pg.transform.rotozoom(bg_sfc, 0, 1.0)
    bg_rct = bg_sfc.get_rect()
    #bg_rct.center = 700, 400
    
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    while(1):
        pg.display.update()
        pg.time.wait(30)
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        pressed = pg.key.get_pressed()
        
        if pressed[K_UP]:
            tori_rct.move_ip(0, -5)
        elif pressed[K_DOWN]:
            tori_rct.move_ip(0, 5)
        elif pressed[K_LEFT]:
            tori_rct.move_ip(-5, 0)
        elif pressed[K_RIGHT]:
            tori_rct.move_ip(5, 0)
        
        clock = pg.time.Clock()
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
    main()
