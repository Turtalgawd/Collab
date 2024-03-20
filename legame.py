import pygame, random

wid = 800
high = 500

window = pygame.display.set_mode((wid, high))

white = (255,255,255)
balck = (0,0,0)
paddel_wid = 5
paddel_high = 50
ball_wid = ball_high = 10

ball_spee = 2
paddel_spee = 2

lef = pygame.USEREVENT + 1
right = pygame.USEREVENT + 2



def windraw(left, right, ball):
    window.fill(balck)
    pygame.draw.rect(window, white, left)
    pygame.draw.rect(window, white, right)
    pygame.draw.rect(window, white, ball)
    pygame.display.update()

def padd_moove(keys, left, right):
    if keys[pygame.K_w] and left.top > 0:
        left.y -= paddel_spee
    if keys[pygame.K_s] and left.bottom < high:
        left.y += paddel_spee
    if keys[pygame.K_UP] and right.top > 0:
        right.y -= paddel_spee
    if keys[pygame.K_w] and right.bottom < high:
        right.y += paddel_spee

def scoring(ball):
    if ball.x >= wid:
        pygame.event.post(pygame.event.Event(lef))
        pygame.time.delay(1000)
        main()
    if ball.x <= 0:
        pygame.event.post(pygame.event.Event(right))
        pygame.time.delay(1000)
        main()

def main():
    clock = pygame.time.Clock()

    left = pygame.Rect(50, (high/2 - paddel_high/2), paddel_wid, paddel_high)
    right = pygame.Rect(wid - 50, (high/2 - paddel_high/2), paddel_wid, paddel_high)
    ball = pygame.Rect((wid/2 - ball_wid/2), (high/2 - ball_high/2), ball_wid, ball_high)

    bxm = random.choice([-1,1]) * ball_spee
    bym = random.choice([-1,1]) * ball_spee
    run = True
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False
        
        ball.x += bxm
        ball.y += bym
        if ball.bottom >= high or ball.top <= 0:
            bym *= -1
        if ball.colliderect(left) or ball.colliderect(right):
            bxm *= -1
        
        windraw(left, right, ball)
        keys_pressed = pygame.key.get_pressed()
        padd_moove(keys_pressed, left, right)
        scoring(ball)
    
    pygame.quit()