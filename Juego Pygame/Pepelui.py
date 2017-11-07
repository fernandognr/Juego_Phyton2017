# -*- coding: utf-8 -*-


# M?dulos
import sys, pygame, random
from pygame.locals import *
import random
"""variables globales"""
ancho = 800
alto = 600
listaMeteors=[]

# Constantes
WIDTH = 800
HEIGHT = 600

# ---------------------------------------------------------------------

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

#Importa imagenes de controles
def control():
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    fondocontrol=pygame.image.load("imagenes/controles.jpg")
    screen.blit(fondocontrol, (0,0))
    pygame.display.flip()
    while 1:
        e=pygame.event.wait()
        if e.type == KEYDOWN:
            main()

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
        tnfacil, rtfacil = texto("Iniciar Batalla Espacial", WIDTH / 2, HEIGHT / 1.3 - 20, (255, 255, 255))
        tnvolver2, rtvolver2 = texto("Volver Menu Principal", WIDTH / 2, HEIGHT / 1.28 + 20)
        pygame.time.delay(100)
    if select3 == 2:
        tnfacil, rtfacil = texto("Iniciar Batalla Espacial", WIDTH / 2, HEIGHT / 1.3 - 20,)
        tnvolver2, rtvolver2 = texto("Volver Menu Principal", WIDTH / 2, HEIGHT / 1.28 + 20, (255, 255, 255))

    screen.blit(tnfacil,rtfacil)
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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Batalla Espacial")
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
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    fondo=pygame.image.load("imagenes/fondo1.jpg")


    select3 =1
    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        if keys[K_UP] and select3 != 1:
            select3 -= 1
        elif keys[K_DOWN] and select3 != 2:
            select3 += 1
        elif keys[K_RETURN]:
            if select3 == 1:
                historia()
            elif select3 == 2:
                main()
        screen.blit(fondo, (0, 0))
        menu3(screen, select3)
        pygame.display.flip()
        pygame.time.delay(10)


def historia():
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
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
class Player(pygame.sprite.Sprite):
    def __init__(self): #esto se ejecuta cada vez que creamos un objeto
        self.imagen1=pygame.image.load("spaceship.png")
        self.imagen2=pygame.image.load("spaceshipleft.png")
        self.imagen3=pygame.image.load("spaceshipright.png")

        "lista de imagenes"
        self.imagenes=[self.imagen1,self.imagen2,self.imagen3]
        self.imagen=self.imagenes[0]

        """sonidos"""
        self.sonidoDisparo=pygame.mixer.Sound("lasersound.wav")
        self.sonidoDisparo.set_volume(0.7)

        self.listaDisparo=[]
        self.rect=self.imagen.get_rect()
        self.rect.top=alto-(alto/5)
        self.rect.left=ancho/2
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        """limitaciones de movimiento a la ventana"""
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=alto:
            self.rect.bottom=alto
        if self.rect.left<=0:
            self.rect.left=0
        if self.rect.right>=ancho:
            self.rect.right=ancho

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

    def disparar(self,x,y):
        miProyectil = Proyectil(x, y)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

class Proyectil(pygame.sprite.Sprite):
    """clase para proyectil de la nave"""
    def __init__(self, posx, posy):
        self.imagen = pygame.image.load("proyectil2.png")
        self.rect = self.imagen.get_rect()
        self.velocidad = 50
        self.rect.top = posy
        self.rect.left = posx
    """metodo para el movimiento de meteoritos"""
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen = pygame.image.load("meteorito.png")
        self.rect = self.imagen.get_rect()
        self.velocidad = 1
        self.rect.top = random.randrange(-400,-50)
        self.rect.left = random.randrange(0, ancho-40)

    def trayectoria(self):
        self.rect.top = self.rect.top + self.velocidad

    def dibujar(self,superficie):
        superficie.blit(self.imagen, self.rect)

"""funcion para cargar meteoritos"""
def cargarMeteoros(cantidadinicial):

    for x in range(cantidadinicial):
        meteor=Meteoritos()
        listaMeteors.append(meteor)

def historia4():

    pygame.init()

    """resolucion de la ventana"""
    pantalla=pygame.display.set_mode((ancho,alto))

    """imagen de fondo"""
    imagenfondo=pygame.image.load("cielo.png")

    """musica y sonidos"""
    pygame.mixer.music.load("bgmusic.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    sonidoImpacto = pygame.mixer.Sound("impact2.wav")
    sonidoImpacto.set_volume(1)

    """objetos"""
    player1=Player() #creamos un objeto de clase player

    """llamada a metodo"""
    cargarMeteoros(5) #llamamos a la funcion cargarEnemigos




    """fuentes y textos"""
    fuente1=pygame.font.SysFont("Verdana", 30, False, False)
    texto1=fuente1.render("Flechas: mover",1,(100,200,255))
    texto2=fuente1.render("D: disparar",1,(100,200,255))
    texto3=fuente1.render("Se aproxima otra oleada",1,(255,254,50))

    txtgameover=fuente1.render("GAME OVER",1,(0,50,255))


    """variables"""
    velocidad=10
    vx,vy=0,0
    leftapretada,rightapretada,upapretada,downapretada=False,False,False,False
    segundos=0
    perdio=False
    salir=False
    reloj1=pygame.time.Clock()


    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if perdio == False:
				"""EVENTOS AL PRESIONAR TECLAS"""
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						leftapretada=True
						vx=-velocidad
						player1.imagen=player1.imagenes[1]
					if event.key ==  pygame.K_RIGHT:
						rightapretada=True
						vx=velocidad
						player1.imagen=player1.imagenes[2]
					if event.key == pygame.K_UP:
						upapretada=True
						vy=-velocidad
					if event.key == pygame.K_DOWN:
						downapretada=True
						vy=velocidad
					if event.key == pygame.K_d:   #tecla de disparar proyectil
						x,y = player1.rect.center
						player1.disparar(x,y)
					if event.key == pygame.K_ESCAPE:
                                                        sys.exit()
				"""EVENTOS AL SOLTAR TECLAS"""
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						leftapretada=False
						player1.imagen=player1.imagenes[0]
						if rightapretada:
							vx=velocidad
							player1.imagen=player1.imagenes[2]
						else:
							vx=0
					if event.key ==  pygame.K_RIGHT:
						rightapretada=False
						player1.imagen=player1.imagenes[0]
						if leftapretada:
							vx=-velocidad
							player1.imagen=player1.imagenes[1]
						else:
							vx=0
					if event.key == pygame.K_UP:
						upapretada=False
						if downapretada:
							vy=velocidad
						else:
							vy=0
					if event.key == pygame.K_DOWN:
						downapretada=False
						if upapretada:
							vy=-velocidad
						else:
							vy=0


        """relojes"""
        reloj1.tick(60) #esto define los maximos FPS del juego
        if perdio!=True:
                                segundos=pygame.time.get_ticks()/1000
                                segundos= str(segundos)
                                cronometro=fuente1.render(segundos,1,(200,200,200))
                                txttimer=fuente1.render("Defendiste el Planeta por:"+str(segundos),1,(200,200,200)) #esto es un texto que muestra el tiempo
                                player1.mover(vx, vy)

        """se dibujan la pantalla y la nave"""
        pantalla.blit(imagenfondo,(0,0))
        player1.dibujar(pantalla)

        """se dibujan los TEXTOS"""
        if (pygame.time.get_ticks()/1000)<5:
            pantalla.blit(texto1,(180,300))
            pantalla.blit(texto2,(470,300))

        """dificultar meteoritos"""
        for x in listaMeteors:
            if pygame.time.get_ticks()/1000>=20:
                x.velocidad=1.5
                velocidad=12
                if pygame.time.get_ticks()/1000<=22:
                    pantalla.blit(texto3,(ancho/3,150))
            if pygame.time.get_ticks()/1000>=27:
                x.velocidad=2
                velocidad=13
                if pygame.time.get_ticks()/1000<=29:
                    pantalla.blit(texto3,(ancho/3,150))
            if pygame.time.get_ticks()/1000>=35:
                x.velocidad=2.5
                velocidad=14
                if pygame.time.get_ticks()/1000<=37:
                    pantalla.blit(texto3,(ancho/3,150))
            if pygame.time.get_ticks()/1000>=50:
                x.velocidad=3.5
                velocidad=14
                if pygame.time.get_ticks()/1000<=52:
                    pantalla.blit(texto3,(ancho/3,150))
            if pygame.time.get_ticks()/1000>=60:
                x.velocidad=4.5
                velocidad=15
                if pygame.time.get_ticks()/1000<=62:
                    pantalla.blit(texto3,(ancho/3,150))

        """dibujar meteoritos y borrarlos cuando salen de la pantalla"""
        if len(listaMeteors)>0:
            for x in listaMeteors:
                x.dibujar(pantalla)
                x.trayectoria()
                if x.rect.top>alto+50:
                    perdio=True
                    listaMeteors.remove(x)
                if len(listaMeteors)<5: #esto carga mas meteoritos a medida que van desapareciendo
					if perdio != True:
						cargarMeteoros(5-len(listaMeteors))
                """eventos de colisiones"""
                for y in player1.listaDisparo:
                    if x.rect.colliderect(y.rect):
                        listaMeteors.remove(x)
                        player1.listaDisparo.remove(y)
                        sonidoImpacto.play()
                if x.rect.colliderect(player1.rect):
                    perdio=True

        """dibujar proyectiles y borrarlos cuando salen de la pantalla"""
        if len (player1.listaDisparo)>0:
            for x in player1.listaDisparo:
                x.dibujar(pantalla)
                x.trayectoria()
                if x.rect.top<-100:
                    player1.listaDisparo.remove(x)
        if perdio==True:
                                vx=0
                                vy=0
                                segundos=0

        if perdio!=True:
            pantalla.blit(cronometro,(750,550))
        else:
            pantalla.blit(txtgameover,(315,100))
            pantalla.blit(txttimer,(130,200))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        pygame.display.update()
if __name__ == '__main__':
    pygame.init()
    main()