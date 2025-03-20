import pygame
import os

pygame.init()

playlist = []
songs_folder = r"C:\Users\Nurai\pp2\labworks\lab7\songs"
allsongs = os.listdir(songs_folder)
for song in allsongs:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(songs_folder, song))

screen = pygame.display.set_mode((1083, 609))
pygame.display.set_caption("Eminem")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(r"C:\Users\Nurai\pp2\labworks\lab7\elements\eminem.png"))
background = pygame.transform.scale(background, (1083, 609))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))
font1 = pygame.font.SysFont(None, 35)

playb = pygame.image.load(os.path.join(r"C:\Users\Nurai\pp2\labworks\lab7\elements\play.png"))
pausb = pygame.image.load(os.path.join(r"C:\Users\Nurai\pp2\labworks\lab7\elements\pause.png"))
nextb = pygame.image.load(os.path.join(r"C:\Users\Nurai\pp2\labworks\lab7\elements\next.png"))
prevb = pygame.image.load(os.path.join(r"C:\Users\Nurai\pp2\labworks\lab7\elements\back.png"))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
aplay = True
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    text = font1.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(background, (0, 0))
    screen.blit(bg, (291, 400))
    screen.blit(text,text.get_rect(center=(541, 450)).topleft)
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (506, 515))
    else: 
        screen.blit(playb, (506, 515))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (691, 515))
    prevb = pygame.transform.scale(prevb, (70, 70))
    screen.blit(prevb, (321, 515))  

    clock.tick(24)
    pygame.display.update()
