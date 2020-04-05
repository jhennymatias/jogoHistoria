# -*- coding: utf-8 -*- 
import sys
from unicodedata import normalize
from PIL import Image 

def procura_resposta(number):
    number = str(number)
    with open("resposta.txt") as file:
        for line in file:
            if number in line:
                txt = line.split(number)
                aux = txt[1].split('\n')
                return aux[0]

def remover_acentos(txt):
    aux = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')   
    return aux.lower()

def main():
    print("---------------------------------------------------")
    print("|                                                 |")
    print("|         Bem-vindo ao jogo                       |")
    print("|                                                 |")
    print("---------------------------------------------------")
    print("Se você chegou até aqui uma jornada irá começar \npara cada etapa uma resposta vai ter que me dar. \n\nLEMBRE-SE NENHUMA RESPOSTA SERÁ EM VÃO!")
    resposta = input("Pronto? (S/N) ")
    if resposta == 'S' or resposta == 's':
        primeira()
        
    else:
        print("Resposta errada! Você deverá começar do zero")
        sys.exit(0)
        
def primeira():
    print("\nResolva 3x = 42 + 1461 + 2x ")
    print(" + ")
    print("Leonardo da Vinci")
    resposta1 = input("Já consegui chegar na primeira resposta? ")
    valida = procura_resposta(1)
    if(remover_acentos(resposta1) == valida):
        segunda()
    else:
        print("Resposta errada!")
        sys.exit(0)

def segunda():
    print("\nVocê sabe onde está a monalisa atualmente?")
    print("As letras abaixo formam o nome de um artista, que tem uma obra no mesmo lugar")
    print('''
          ______________________________________________
          |    x      n      a       a       t       e  |
          |  d   r       d       i       o       i      |
          | l        a       e       u       i       n  |
          |      o               q          e       a   |
          |_____________________________________________|
          ''')
    print("Sabe qual é a obra? ")
    resposta2 = input("A resposta que deve me entreguer é qual o país que essa obra \n foi feita: ")
    valida = procura_resposta(2)
    
    if(remover_acentos(resposta2) == valida):
        terceira()
    else:
        print("Resposta errada!")
        sys.exit(0)

def terceira():
    texto= '''
        Agora já estamos na Grécia, lá iniciou muitas coisas,
        uma dessas coisas foi a filosofia. Bem a filosofia estuda sobre 
        muitas coisas, uma delas são os mitos.
        
        Os mitos eram utilizados explicar fenomenos, os quais eles
        não conseguiam utilizar a razão para compreender, assim ele 
        usavam muitas vezes deuses e herois como figuras centrais 
        destas histórias.
        
        Hoje então deveremos encontrar eles e aqui vão as dicas:
                
        * Wald
        * hav
        * nani
        * maitasun
        * saĝo
        * Ay
        * doodmaak minotaur
        
        A primeira letra irá te ajudar a achar a próxima resposta
    '''
    print(texto)
    resposta3 = input("Já chegou na sua resposta? ")
    valida = procura_resposta(3)
    
    if(remover_acentos(resposta3) == valida):
        quarta()
    else:
        print("Resposta errada!")
        sys.exit(0)

def quarta():
    texto = '''
        THIS IS SPARTA
        
        Espero que você tenha entendido, você sabe onde isso aconteceu?
        Sabia que há um memorial lá?  Vá até lá.
        Já chegou?
        
        Latitude: 41°53′30″ ?
        Longitude: 12°30′40″ ?
        
        A imagem é uma dica não se assuste ;)
    '''
    print(texto)
    im = Image.open(r"fase4.png")
    im.show()
    
    resposta4 = input("Já chegou? ")
    valida = procura_resposta(4)
    
    if(remover_acentos(resposta4) == valida):
        quinta()
    else:
        print("Resposta errada!")
        sys.exit(0)

def quinta():
    texto = '''
        Olha chegamos em Roma e temos muitos lugares pra visitar,
        assim aqui vai a dica de lugares que você deve ir:
        
        1 - É uma das principais estradas da antiga Roma. Recebeu 
        este nome em memória do político romano Ápio Cláudio Cego.
        
        2 - Foi encomendado pelo Senado Romano para comemorar os dez 
        anos do reinado de Constantino.
        
        3 - Ele foi construído pelo imperador Domiciano Logo depois
        da morte de seu irmão mais velho, Tito.
        
        4 - Foram encomendadas por Maximiano em honra ao co-imperador 
        Diocleciano, no ano que ele retornou da África.
        
        5- Devido às suas origens obscuras, era considerada pelos Romanos 
        como um posto de mau presságio.
        
        6- Conhecido também por Amphitheatrum Flavium
        
        7- Localizada abaixo da Basílica de São Pedro

        8- 41° 53′ 6.36″ N, 12° 28′ 49.44″ E (inglês) 
        
        USE A PRIMEIRA LETRA DE CADA RESPOSTA E ENCONTRA A PRÓXIMA CHAVE.
    '''
    print(texto)
    resposta5 = input("Já chegou na sua resposta? ")
    valida = procura_resposta(5)
    if(remover_acentos(resposta5) == valida):
        sexto()
    else:
        print("Resposta errada!")
        sys.exit(0)
        
def sexto():
    im = Image.open(r"fase6.jpg")
    im.show()
    resposta6 = input("Já chegou na sua resposta? ")
    valida = procura_resposta(6)
    if(remover_acentos(resposta6) == valida):
        print("Continua ...")
    else:
        print("Resposta errada!")
        sys.exit(0)
        
        
if __name__ == '__main__':
    main()
    
