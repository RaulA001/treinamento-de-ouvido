from pygame import mixer, init, event
from random import choice


def Nomear_nota(self, nota):
    '''resposavel nomear notas na notção grega e germanica e separalas do seu complemento'''
    
    #notas principais
    nota = nota.capitalize()
    c = False
    
    if 'Do' in nota or 'C' in nota or 'Dó' in nota:
        if nota[:1] in 'DoDó':
            print('erro')
            c = True
        self.NotaC = 'Dó'
        self.NotaG = 'C'
    elif 'Re' in nota or 'D' in nota or 'Ré' in nota:
        if nota[:1] in 'ReRé':
            c = True
        self.NotaC = 'Ré'
        self.NotaG = 'D'
    elif 'Mi' in nota or 'E' in nota:
        if nota[:1] in 'MiMí':
            c = True
        self.NotaC = 'Mi'
        self.NotaG = 'E'
    elif 'Fá' in nota or 'F' in nota or 'Fa' in nota:
        if nota[:1] in 'FaFá':
            c = True
        self.NotaC = 'Fá'
        self.NotaG = 'F'
    elif 'Sol' in nota or 'G' in nota:
        if nota[:2] in 'Sol':
            c = True
        self.NotaC = 'Sol'
        self.NotaG = 'G'
    elif 'La' in nota or 'A' in nota or 'Lá' in nota:
        if nota[:1] in 'LaLá':
            c = True
        self.NotaC = 'Lá'
        self.NotaG = 'A'
    elif 'Si' in nota or 'B' in nota:
        if nota[:1] in 'SiSí':
            c = True
        self.NotaC = 'Si'
        self.NotaG = 'B'
    else:
        self.NotaC = 'Erro-Nota'
        self.NotaG = 'Erro-Nota'

    #variaçoes/Complemento
    if c:
        if not 'Sol' in nota:
            comp = nota[2:]
        else:
            comp = nota[3:]
    else:
        comp = nota[1:]
    self.Comp = comp
    
    #nome completo
    self.NomeC = f'{self.NotaC}{self.Comp}'
    self.NomeG = f'{self.NotaG}{self.Comp}'

class Notas():
    def __init__(self, str='Erro', nota='Erro-Nota', casa='Erro-Cassa', vol=1):
        self.Str = str
        Nomear_nota(self, nota)
        self.Casa = casa
        self.Vol = vol

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

class Pergunta():
    def __init__(self, notaT='Erro-NotaT', res='', notas='Erro-Notas'):
        self.NotaT = notaT
        #self.Som = posisão do som da notaT
        self.Res = res
        self.Notas = notas

#p
n = Notas(2, 'g', 1, 2)
n.GetAll()
