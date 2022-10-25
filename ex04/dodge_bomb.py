from pygame.locals import *
import pygame as pg
import sys
def main():
    pg.init()
    scrn_sfc = pg.display.set_mode((1600, 900))
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.get_surface()
    
    tori_sfc = pg.image.load("pg_bg.jpg")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 700, 400
    while(1):
        pg.display.update()
        pg.time.wait(30)
        scrn_sfc.blit(tori_sfc, tori_rct)

        
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
                    
    
    
if __name__ == "__main__":
    main()
