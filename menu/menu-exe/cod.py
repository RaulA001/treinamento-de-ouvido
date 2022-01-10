from playsound import playsound
from random import randint


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
    def __init__(self, nota='Erro-Nota', casa='Erro-Cassa', instrumento='ERRO_instrumento', str='Erro', vol=1, pasta="notas/"):
        Nomear_nota(self, nota)
        self.Casa = casa
        self.Instr = instrumento
        self.Vol = vol
        self.Pasta = pasta
        if str == 'Erro':
            str = f'{self.Pasta}{self.NotaG}/{self.NomeG}{self.Casa}_{self.Instr}.wav'
        self.Str = str


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

    def Rep(self):
        playsound(self.Str)

#                   Pergunta
class Pergunta():
    #OBS: notaT é a resposta certa e res é a resposta do usuario
    def __init__(self, notas='Erro-Notas', res='', notaT=''):
        self.NotaT = notaT
        #self.Som = posisão do som da notaT
        self.Res = res 
        self.Notas = notas
        #nota não jogadas
        Notas = []
        for n in notas:
            Notas.append(n.NomeG)
        self.NotasL = Notas
        
    def SetRes(self, res):
        self.Res = res
    
    def Status(self):
        print(self.NotaT, self.Notas, self.Res.NomeG)

    def Apresentar(self):
        print('/ ', end='')
        for n in self.NotasL:
            print(n, end=' ')
        print('/')

    def init(self):
        #difinir nota certa
        n = len(self.Notas) - 1
        nt = randint(0, n)
        self.NotaT = self.Notas[nt]
        self.NNotaT = n

    def Confirir(self, re):
        r = 0

        if re.C:
            if re.NotaC == self.NotaT.NotaC and (re.Instr == self.NotaT.Instr or True):
                r = 1
        else:
            if re.NotaG == self.NotaT.NotaG and (re.Instr == self.NotaT.Instr or True):
                r = 1
        if re.NotaG == 'Erro-Nota':
            r = -1
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

    def init(self):
        for c in range(0, 1):
            p = Pergunta(notas)
            p.init()
            p.Apresentar()
            resp = p.Confirir()
            if resp == 1:
                print(1)
            elif resp == 2:
                print(0)
            elif resp == -1:
                c += 1

#p
a = Notas('a', '', 'violao')
b = Notas('b', '', 'violao')
d = Notas('d', '', 'violao')
e = Notas('e', '', 'violao')
g = Notas('g', '', 'violao')
notas = [a, b, d, e, g]

for c in range(0, 10):
    p = Pergunta(notas)
    p.init()
    p.NotaT.Rep()


    certo = False
    while not certo:

        p.Apresentar()
        perg = True
        while perg:
            resposta = str(input('Qual é a nota: '))
            if resposta == '':
                p.NotaT.Rep()
            else:
                break
            
        p.SetRes(resposta)
        re = Notas(p.Res)
        resp = p.Confirir(re)

        if resp == 1:
            print(1)
            certo = True
        elif resp == 0:
            pos = p.NotasL.index(re.NomeG)
            p.NotasL.insert(pos, '')
            p.NotasL.pop(pos + 1)
            print(0)
        elif resp == -1:
            print('Resposta invalida')
