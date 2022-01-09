from playsound import playsound
from random import choice


def Nomear_nota(self, nota, obj=True):
    '''resposavel nomear notas na notção grega e germanica e separalas do seu complemento'''
    
    #notas principais
    nota = nota.capitalize()
    c = False

    if 'Do' in nota or 'C' in nota or 'Dó' in nota:
        if nota[:1] in 'DoDó':
            c = True
        if obj:
            self.NotaC = 'Dó'
            self.NotaG = 'C'
    elif 'Re' in nota or 'D' in nota or 'Ré' in nota:
        if nota[:1] in 'ReRé':
            c = True
        if obj:
            self.NotaC = 'Ré'
            self.NotaG = 'D'
    elif 'Mi' in nota or 'E' in nota:
        if nota[:1] in 'MiMí':
            c = True
        if obj:
            self.NotaC = 'Mi'
            self.NotaG = 'E'
    elif 'Fá' in nota or 'F' in nota or 'Fa' in nota:
        if nota[:1] in 'FaFá':
            c = True
        if obj:
            self.NotaC = 'Fá'
            self.NotaG = 'F'
    elif 'Sol' in nota or 'G' in nota:
        if nota[:2] in 'Sol':
            c = True
        if obj:
            self.NotaC = 'Sol'
            self.NotaG = 'G'
    elif 'La' in nota or 'A' in nota or 'Lá' in nota:
        if nota[:1] in 'LaLá':
            c = True
        if obj:
            self.NotaC = 'Lá'
            self.NotaG = 'A'
    elif 'Si' in nota or 'B' in nota:
        if nota[:1] in 'SiSí':
            c = True
        if obj:
            self.NotaC = 'Si'
            self.NotaG = 'B'
    else:
        if obj:
            self.NotaC = 'Erro-Nota'
            self.NotaG = 'Erro-Nota'
        else:
            print('Não é uma nota')


    #variaçoes/Complemento
    self.C = c
    if c:
        if not 'Sol' in nota:
            comp = nota[2:]
        else:
            comp = nota[3:]
    else:
        comp = nota[1:]

    if obj:
        self.Comp = comp

        #nome completo
        self.NomeC = f'{self.NotaC}{self.Comp}'
        self.NomeG = f'{self.NotaG}{self.Comp}'
    else:
        return c

#                   Notas
class Notas():
    def __init__(self, nota='Erro-Nota', casa='Erro-Cassa', str='Erro', vol=1):
        self.Str = str
        Nomear_nota(self, nota)
        self.Casa = casa
        self.Vol = vol

    #OBS: str é a localisação do som
    def SetMain(self, str='val', nota='val', casa='val'):
        if str == 'val':
            str = self.Str

        if nota == 'val':
            'nu'
            nota = self.Nota

        if casa == 'val':
            casa = self.Casa

        self.Str = str
        Nomear_nota(self, nota)
        self.Casa = casa

    def SetVol(self, vol=1):
        self.Vol = vol

    def GetAll(self):
        print(self.Str, self.NotaC, self.NotaG, self.Casa, self.Vol, self.NomeC, self.NomeG)

#                   Pergunta
class Pergunta():
    #OBS: notaT é a resposta certa e res é a resposta do usuario
    def __init__(self, notas='Erro-Notas', res='', notaT=''):
        self.NotaT = notaT
        #self.Som = posisão do som da notaT
        self.Res = res
        self.Notas = notas
        
    def SetRes(self, res):
        self.Res = res
    
    def Status(self):
        print(self.NotaT, self.Notas, self.Res.NomeG)

    def Apresentar(self):
        print('/ ', end='')
        for n in self.Notas:
            print(n.NomeG, end=' ')
        print('/')

    def init(self):
        #difinir nota certa
        self.NotaT = choice(self.Notas)

    def Confirir(self):
        r = False

        re = Notas(self.Res)
        if re.C:
            if re.NotaC == self.NotaT.NotaC:
                r = True
            return r
        else:
            if re.NotaG == self.NotaT.NotaG:
                r = True
            return r

class Questionario():
    def __init__(self, nome, notas, volume, n_perguntas):
        self.Nome = nome
        self.Notas = notas
        self.Vol = volume
        self.Np = n_perguntas
        self.N_acertos = 0

    def rep(self, nota):
        playsound(nota.str)

    #def init(self):

#p
a = Notas('a')
b = Notas('b')
c = Notas('c')
d = Notas('d')
notas = (a, b, c, d)

#for c in range(0, 4):
#    p = Pergunta(notas)
#    p.init()
#    p.Apresentar()
#    p.SetRes(str(input('Qual é a nota: ')))
#    if p.Confirir():
#        print(1)
#    else:
#        print(0)

#'cartoon.wav'
import pygame

playsound('cartoon.wav')