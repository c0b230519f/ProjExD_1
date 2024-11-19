import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_x_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    tmr = 0
    a = 3
    bg_x = 0
    bg_width = bg_img.get_width()
    kk_rect = kk_img.get_rect()
    kk_rect.center = (300, 200)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        #print(key_lst[end=])
        screen.blit(bg_img, [-(tmr%1600), 0]) #スクリーンサーフェイスに背景画像を貼る
        screen.blit(bg_img2, [-((tmr+1600)%1600), 0])
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()