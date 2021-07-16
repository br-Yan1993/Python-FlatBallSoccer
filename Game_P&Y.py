from lib2to3.fixes.fix_map import FixMap

import pygame
import random

#se bola bater na parede zera a pontuação, se bater na raquete velocidade aumenta +1, se chegar a 10 pontos vence.
# condições para melhoria

PRETO = 0,0,0
BRANCO= 255,255,255
VERDE = 0,150,0
AZUL = 0,0,150
VERMELHO = 255,0, 0

ImagemCampo = pygame.image.load("campo1.jpg")
BallImage = pygame.image.load("bola-15Px.png")

fim = False
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
tela_retangulo = tela.get_rect()
tempo = pygame.time.Clock()
pygame.display.set_caption("Game P&Y")

#Classe que define os parametros da raquete
class Raquete1:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERMELHO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15
        self.imagem_retangulo[0] = 795  # Met que determina onde o Objeto sera iniciado (no plano)
        self.imagem_retangulo[1] = 500

    #função que move a raquete pra cima e para baixo
    def mover(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

    #função que recebe os comandos das teclas para movimento da raquete
    def atualiza(self, tecla):
        if tecla[pygame.K_UP]:
            self.mover (0, -1)

        if tecla[pygame.K_DOWN]:
            self.mover (0, 1)

        if tecla[pygame.K_RIGHT]:
            self.mover (1, 0)

        if tecla[pygame.K_LEFT]:
            self.mover (-1, 0)

        #clmamp_ip = não ultrapassar o objeto
        self.imagem_retangulo.clamp_ip(tela_retangulo)


    #insere a raquete no plano
    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

class LeftRow:
    def __init__(self, tamanho):
        self.escopeSurface = pygame.Surface(tamanho)
        self.escopeSurface.fill(PRETO)
        self.escope = self.escopeSurface.get_rect()
        self.escope[1] = 231

    def InsertOnScreen(self):
        tela.blit(self.escopeSurface, self.escope)

class RightRow:
    def __init__(self, tamanho):
        self.escopeSurface = pygame.Surface(tamanho)
        self.escopeSurface.fill(PRETO)
        self.escope = self.escopeSurface.get_rect()
        self.escope[1] = 231
        self.escope[0] = 798

    def InsertOnScreen(self):
        tela.blit(self.escopeSurface, self.escope)

class Raquete2:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(AZUL)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15
        self.imagem_retangulo[0] = 0
        self.posicao = list(tela_retangulo.center)

    #função que move a raquete pra cima e para baixo
    def mover(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

    #função que recebe os comandos das teclas para movimento da raquete
    def atualiza(self, tecla):
        if tecla[pygame.K_w]:
            self.mover (0, -1)

        if tecla[pygame.K_s]:
            self.mover (0, 1)

        if tecla[pygame.K_d]:
            self.mover (1, 0)

        if tecla[pygame.K_a]:
            self.mover (-1, 0)

        #clmamp_ip = não ultrapassar o objeto
        self.imagem_retangulo.clamp_ip(tela_retangulo)


    #insere a raquete no plano
    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

#classe que define os parametros da bola
class Bola:
    def __init__(self, tamanho):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERMELHO)
        self.ball = self.imagem.get_rect()
        self.velocidade = 15
        self.set_bola()

    #para a bola nao pegar a mesma velocidade e direção
    def aleatorio(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -.5 and num < 0.5:
                continue
            else:
                return num

    #função que faz a bola tomar sentido no plano, saindo do centro da tela
    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.ball.x = tela_retangulo.centerx
        self.ball.y = tela_retangulo.centery
        self.velocidadebola = [x, y]
        self.posicao = list(tela_retangulo.center)


    #fuñção para quando tocar na parede a bolinha percorrer caminho contrário
    def colide_parede(self):
        if self.ball.y < 0 or self.ball.y > tela_retangulo.bottom - self.altura:
            self.velocidadebola[1] *= -1

        if self.ball.x < 0 or self.ball.x > tela_retangulo.right - self.largura:
            self.velocidadebola[0] *= -1

    def golScore(self):
        if self.ball.colliderect(rgtRow.escope):
            placar1.golRedTeam += 1
            x = self.aleatorio()
            y = self.aleatorio()
            self.ball.x = tela_retangulo.centerx
            self.ball.y = tela_retangulo.centery
            self.velocidadebola = [x, y]
            self.posicao = list(tela_retangulo.center)
            self.velocidade += 1
            print("GOL!" + str(placar1.golRedTeam))
            if placar1.golRedTeam == 2:
                fim = True


        elif self.ball.colliderect(lftRow.escope):
            placar1.golBlueTeam += 1
            x = self.aleatorio()
            y = self.aleatorio()
            self.ball.x = tela_retangulo.centerx
            self.ball.y = tela_retangulo.centery
            self.velocidadebola = [x, y]
            self.posicao = list(tela_retangulo.center)
            self.velocidade += 1
            print("GOL!" + str(placar1.golBlueTeam))
            if placar1.golBlueTeam == 1:
                fim = True


    #função pra quando a bolinha tocar na raquete
    def colide_raquete(self, raquete_rect):
        if self.ball.colliderect(raquete_rect):
            self.velocidadebola[0] *= -1
            print ("Boa, defendeu!!")



        # função que move a raquete pra cima e para baixo
    def mover(self):
        self.posicao[0] += self.velocidadebola[0] * self.velocidade
        self.posicao[1] += self.velocidadebola[1] * self.velocidade
        self.ball.center = self.posicao

    def atualiza(self, raquete_rect, raquete_rect1):
        self.golScore()
        self.colide_parede()
        self.colide_raquete(raquete_rect)
        self.colide_raquete(raquete_rect1)
        self.mover()


        # coloca a raquete no plano
    def realiza(self):
        tela.blit(self.imagem, self.ball)

class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 80)
        self.golRedTeam = 0
        self.golBlueTeam = 0

    def contagem(self):
        self.text1 = pygame.Surface(tamanho)
        self.text2 = pygame.Surface(tamanho)
        self.text1 = self.fonte.render(str(self.golRedTeam), 1, (180, 0, 0))
        self.text2 = self.fonte.render(str(self.golBlueTeam), 1, (0, 0, 180))
        self.textposition1 = self.text1.get_rect()
        self.textposition2 = self.text2.get_rect()
        self.textposition1[0] = 290
        self.textposition1[1] = 30
        self.textposition2[0] = 490
        self.textposition2[1] = 30
        tela.blit(self.text1, self.textposition1)
        tela.blit(self.text2, self.textposition2)
        tela.blit(tela, (0, 0))

#defin o tamanho da raquete, bola e placar.
raquete = Raquete1((10, 70))
raquete2 = Raquete2((10, 70))
lftRow = LeftRow((2, 140))
rgtRow = RightRow((2, 140))
bola = Bola((15, 15))
placar1 = Placar()

#faz com que a janela não feche
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True



    #chamada das funções
    if placar1.golBlueTeam == 1:
        fim = True
    elif placar1.golRedTeam == 1:
        fim = True
    tecla=pygame.key.get_pressed()
    tela.fill(PRETO)
    tela.blit(ImagemCampo, (0,0))
    raquete.realiza()
    raquete2.realiza()
    bola.realiza()
    raquete.atualiza(tecla)
    raquete2.atualiza(tecla)
    bola.atualiza(raquete.imagem_retangulo, raquete2.imagem_retangulo)
    lftRow.InsertOnScreen()
    rgtRow.InsertOnScreen()
    tempo.tick(30)
    placar1.contagem()
    pygame.display.update()