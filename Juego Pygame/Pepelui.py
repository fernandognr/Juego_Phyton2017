# -*- coding: utf-8 -*-


# M?dulos
import sys, pygame, random
from pygame.locals import *

# Constantes
WIDTH = 800
HEIGHT = 600

# Clases
# ---------------------------------------------------------------------





# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------




def appstart(lista, elemento):
    nueva = [elemento]
    nueva += lista
    return nueva

def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image


#####------------------------------------------------------------------------
#Font Del menu


def texto(texto, posx, posy, color=(150, 150, 150), tam=35):
    fuente = pygame.font.Font("imagenes/kindergarten.ttf", tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
#####------------------------------------------------------------------------
#Opcion de Salir
def salir(keys):
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
        if keys[K_ESCAPE]:
            sys.exit(0)

#----------------------------PAUSAR-------------------------------------

#http://www.lawebdelprogramador.com/foros/Python/1477283-Pausa-en-Juego.html

def pausa():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondop=pygame.image.load("imagenes/controles.jpg")
    if keys[K_RIGHT]:
        screen.blit(fondop,(0, 0))
        pygame.display.update()
        while 1:
            e=pygame.event.wait()
            if e.type in (pygame.QUIT, pygame.KEYDOWN):
                return 0
#-----------------------------------------------------------------------

#Importa imagenes de controles
def control():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondocontrol=pygame.image.load("imagenes/controles.jpg")
    screen.blit(fondocontrol, (0,0))
    pygame.display.flip()
    while 1:
        e=pygame.event.wait()
        if e.type == KEYDOWN:
            return

#------------------------PRESENTACION-----------------------------------------



#------------------------NUEVO JUEGO------------------------------------------

#Opcion que te devuelve al menu
def nuevo_juego(keys):
    pygame.init()

    fondo = pygame.image.load("imagenes/historia1.jpg").convert_alpha()
    auxCont = 1
    auxImg1 = ""
    auxImg2 = ""
    auxImg3 = ""
    auxImg3=""
    screen.blit(fondo, (0, 0))
    pygame.display.flip()
    if keys[pygame.K_RIGHT]:
        auxCont = auxCont + 1
        if auxCont > 4:
            auxCont = 1
        auxImg1 = "imagenes/historia"
        auxImg2 = ".jpg"
        auxImg3 = str(auxCont)
        auxImg4 = auxImg1 + auxImg3 + auxImg2
        fondo = pygame.image.load(auxImg4).convert_alpha()







#--------------------------------------JUEGO----------------------------------
def juego(screen,fondo,):
    clock = pygame.time.Clock()

    while True:
        time = clock.tick(10)
        keys = pygame.key.get_pressed()
        salir(keys)
        screen.blit(fondo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1)


#--------------------------------MENU PRINCIPAL-------------------------------------------
#Texto en pantalla de menu
def menu(screen, select):
    if select == 1:
        tnjuego, rtnjuego = texto("Jugar", WIDTH / 2, HEIGHT / 1.3 - 20, (255, 255, 255))
        tnopciones, rtnopciones = texto ("Opciones", WIDTH/ 2, HEIGHT / 1.28+ 20)
        tcontrol, rtcontrol = texto("Controles", WIDTH / 2, HEIGHT / 1.27 + 60)
        tsalir, rtsalir = texto("Salir", WIDTH / 2, HEIGHT / 1.22 + 80)
        pygame.time.delay(100)
    if select == 2:
        tnjuego, rtnjuego = texto("Jugar", WIDTH / 2, HEIGHT / 1.3 - 20,)
        tnopciones, rtnopciones = texto ("Opciones", WIDTH/ 2, HEIGHT / 1.28+ 20, (255, 255, 255))
        tcontrol, rtcontrol = texto("Controles", WIDTH / 2, HEIGHT / 1.27 + 60)
        tsalir, rtsalir = texto("Salir", WIDTH / 2, HEIGHT / 1.22 + 80)
        pygame.time.delay(100)
    if select == 3:
        tnjuego, rtnjuego = texto("Jugar", WIDTH / 2, HEIGHT / 1.3 - 20)
        tnopciones, rtnopciones = texto ("Opciones", WIDTH/ 2, HEIGHT / 1.28+ 20)
        tcontrol, rtcontrol = texto("Controles", WIDTH/2, HEIGHT/1.27 + 60, (255, 255, 255))
        tsalir, rtsalir = texto("Salir", WIDTH / 2, HEIGHT / 1.22 + 80)
    if select == 4:
        pygame.time.delay(100)
        tnjuego, rtnjuego = texto("Jugar", WIDTH / 2, HEIGHT / 1.3 - 20)
        tnopciones, rtnopciones = texto ("Opciones", WIDTH/ 2, HEIGHT / 1.28+ 20)
        tcontrol, rtcontrol = texto("Controles", WIDTH/2, HEIGHT/ 1.27 + 60)
        tsalir, rtsalir = texto("Salir", WIDTH / 2, HEIGHT / 1.22 + 80, (255, 255, 255))

    screen.blit(tnjuego, rtnjuego)
    screen.blit(tnopciones, rtnopciones)
    screen.blit(tcontrol, rtcontrol)
    screen.blit(tsalir, rtsalir)


#-------------------------------MENU DIFICILTAD----------------------------------------------------------------
def menu3(screen, select3):

    if select3 == 1:
        tnfacil, rtfacil = texto("Modo noob (Facil)", WIDTH / 2, HEIGHT / 1.3 - 20, (255, 255, 255))
        tndificil, rtdificil = texto("Modo Dios (Dificil)", WIDTH / 2, HEIGHT / 1.28 + 20)
        tnvolver2, rtvolver2 = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40)
        pygame.time.delay(100)
    if select3 == 2:
        tnfacil, rtfacil = texto("Modo noob (Facil)", WIDTH / 2, HEIGHT / 1.3 - 20,)
        tndificil, rtdificil = texto("Modo Dios (Dificil)", WIDTH / 2, HEIGHT / 1.28 + 20,(255, 255, 255))
        tnvolver2, rtvolver2 = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40)
        pygame.time.delay(100)
    if select3 == 3:
        tnfacil, rtfacil = texto("Modo noob (Facil)", WIDTH / 2, HEIGHT / 1.3 - 20,)
        tndificil, rtdificil = texto("Modo Dios (Dificil)", WIDTH / 2, HEIGHT / 1.28 + 20)
        tnvolver2, rtvolver2 = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40,(255, 255, 255))

    screen.blit(tnfacil,rtfacil)
    screen.blit(tndificil, rtdificil)
    screen.blit(tnvolver2,rtvolver2)

#---------------------------------MENU OPCIONES AUDIO---------------------------------------------------------

def menu2(screen, select2):

    if select2 == 1:
        tnsonido, rtnsonido = texto("Desactivar sonido", WIDTH / 2, HEIGHT / 1.3 - 20, (255, 255, 255))
        tnsonido2, rtnsonido2 = texto("Activar sonido", WIDTH / 2, HEIGHT / 1.28 + 20)
        tnvolver, rtnvolver = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40)

        pygame.time.delay(100)
    if select2 == 2:
        tnsonido, rtnsonido = texto("Desactivar sonido", WIDTH / 2, HEIGHT / 1.3 - 20)
        tnsonido2, rtnsonido2 = texto("Activar sonido", WIDTH / 2, HEIGHT / 1.28 + 20,(255, 255, 255))
        tnvolver, rtnvolver = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40)
        pygame.time.delay(100)
    if select2 == 3:
        tnsonido, rtnsonido = texto("Desactivar sonido", WIDTH / 2, HEIGHT / 1.3 - 20)
        tnsonido2, rtnsonido2 = texto("Activar sonido", WIDTH / 2, HEIGHT / 1.28 + 20)
        tnvolver, rtnvolver = texto("Volver menu principal", WIDTH / 2, HEIGHT / 1.23 + 40,(255, 255, 255))
    screen.blit(tnsonido, rtnsonido)
    screen.blit(tnsonido2, rtnsonido2)
    screen.blit(tnvolver, rtnvolver)
# ---------------------------------------------------------------------
#Bucle main, con fondo y nombre
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Ovagugul")
    fondo = load_image('imagenes/fondo.jpg')
    pygame.mixer.music.load('imagenes/misao.mp3')

    select = 1
    pause = 0

    if pause==0:
        pygame.mixer.music.play(10)
    elif pause == 1:
        pygame.mixer.music.stop()
    while True:
        keys = pygame.key.get_pressed()
        salir(keys)

## Control de  las opciones del menu
        if keys[K_UP] and select != 1:
            select -= 1
        elif keys[K_DOWN] and select != 4:
            select += 1
        elif keys[K_RETURN]:
            if select == 1:
                dificultad()
            elif select == 2:
                opciones()
                select = 1
            elif select == 3:
                control()
                select= 1
            elif select == 4:
                sys.exit()

        screen.blit(fondo, (0, 0))
        menu(screen, select)
        pygame.display.flip()
        pygame.time.delay(10)
    return 0


#------------------------------OPCIONES---------------------------------------
def opciones():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/fondo.jpg")


    select2 =1

    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_UP] and select2 != 1:
            select2 -= 1
        elif keys[K_DOWN] and select2 != 3:
            select2 += 1
        elif keys[K_RETURN]:
            if select2 == 1:
                pygame.mixer.music.stop()
                pause = 1
                return pause
                select2==3
            elif select2 == 2:
                pygame.mixer.music.play(10)
            elif select2==3:
                main()
        screen.blit(fondo, (0, 0))
        menu2(screen, select2)
        pygame.display.flip()
        pygame.time.delay(10)
    return 0

#---------------------------------DIFUCULTAD------------------------------------------

def dificultad():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/fondo1.jpg")


    select3 =1
    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_UP] and select3 != 1:
            select3 -= 1
        elif keys[K_DOWN] and select3 != 3:
            select3 += 1
        elif keys[K_RETURN]:
            if select3 == 1:
                historia()
            elif select3 == 2:
                opciones()
            elif select3 == 3:
                main()
        screen.blit(fondo, (0, 0))
        menu3(screen, select3)
        pygame.display.flip()
        pygame.time.delay(10)


def historia():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/historia1.jpg")

    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_RIGHT]:
            historia2()
        screen.blit(fondo, (0,0))
        pygame.display.flip()
        pygame.time.delay(10)

def historia2():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/historia2.jpg")

    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_LEFT]:
            historia()
        if keys[K_RIGHT]:
            historia3()

        screen.blit(fondo, (0,0))
        pygame.display.flip()
        pygame.time.delay(10)

def historia3():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/historia3.jpg")

    while True:

        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_LEFT]:
            historia2()
        if keys[K_RIGHT]:
            historia4()

        screen.blit(fondo, (0,0))
        pygame.display.flip()
        pygame.time.delay(10)


def historia4():
    screen=pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fondo=pygame.image.load("imagenes/historia4.jpg")

    while True:

        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_LEFT]:
            historia3()

        screen.blit(fondo, (0,0))
        pygame.display.flip()
        pygame.time.delay(10)
if __name__ == '__main__':
    pygame.init()
    main()