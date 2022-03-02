import csv
import matplotlib.pyplot as plt
from datetime import date 

tipoResposta = '0' 

def mediaAritmetica(lista): 

    somaValores = 0
    if len(lista) == 0:
        return 0 

    for valor in lista: 
        somaValores += valor
    return somaValores / len(lista) 

def imprimeLinhas(): #Linhas L6
    print("Digite o nome de um país:")
    nomePais = input()
    print("Digite o nome de um esporte:")
    nomeEsporte = input()
    print("Digite o ano inicial:")
    anoInicial = int(input())
    print("Digite o final:")
    anoFinal = int(input())
    print("Digite o tipo de olimpíada:")
    tipoOlimpiada = input()

    bronzeY = [0] * (anoFinal - anoInicial) 

    prataY = [0] * (anoFinal - anoInicial)
    ouroY = [0] * (anoFinal - anoInicial)

    x = list(range(anoInicial, anoFinal)) 

    with open('./data/athlete_events.csv') as f: 

        reader = csv.reader(f) 

        for linha in reader:
            if linha[7] == nomePais and linha[12] == nomeEsporte and anoInicial <= int(linha[9]) <= anoFinal and tipoOlimpiada == linha[10] and linha[14] != 'NA':
                if linha[14] == 'Bronze':
                    bronzeY[int(linha[9]) - anoInicial] += 1
                elif linha[14] == 'Silver':
                    prataY[int(linha[9]) - anoInicial] += 1
                else:
                    ouroY[int(linha[9]) - anoInicial] += 1

    plt.plot(x, ouroY, label='Ouro', color='gold', marker='o')
    plt.plot(x, prataY, color='silver', marker='o', label='Prata')
    plt.plot(x, bronzeY, color='orange', marker='o', label='Bronze')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de medalhas')
    plt.title('Quantidades de medalhas no período')
    plt.legend()
    plt.show() 


def imprimeBarras(): #Barras B6
    print("Quantidades de olimpiadas a serem analisadas (ordem cronológica decrescente):")
    ultimasOlimpiadas = int(input())
    print("Digite o tipo de olimpíada:")
    tipoOlimpiada = input()
    masculinoY = []
    femininoY = []
    mediaMasculinaY = []
    mediaFemininaY = []

    ultimaEdicao = int(date.today().year / 4) 

    xMasculina = []
    xFeminina = []

    for i in range(0, ultimasOlimpiadas):
        xMasculina.append((ultimaEdicao - i) * 4 - 0.1) 

        xFeminina.append((ultimaEdicao - i) * 4 + 0.1)

        masculinoY.append([]) 

        femininoY.append([]) 

    with open('./data/athlete_events.csv') as f: 

        reader = csv.reader(f) 
        next(reader) 

        for linha in reader:

            edicaoDaLinha = int(int(linha[9]) / 4) 

            if tipoOlimpiada == linha[10] and edicaoDaLinha > ultimaEdicao - ultimasOlimpiadas and linha[14] != 'NA' and linha[3] != 'NA': 
                if linha[2] == 'F':
                    femininoY[ultimaEdicao - edicaoDaLinha].append(int(linha[3]))
                   
                else:
                    masculinoY[ultimaEdicao - edicaoDaLinha].append(int(linha[3]))

    for i in range(0, ultimasOlimpiadas):
        mediaMasculinaY.append(mediaAritmetica(masculinoY[i])) 
    
        mediaFemininaY.append(mediaAritmetica(femininoY[i]))

    plt.bar(xMasculina, mediaMasculinaY, color='silver', label='Masculino', width=0.2)
    plt.bar(xFeminina, mediaFemininaY, color='gold', label='Feminino', width=0.2)
    plt.legend()
    plt.show() 


def imprimeBoxplot(): #Boxplot X9

  print("Quantidades de olimpiadas a serem analisadas (ordem cronológica decrescente):")
  ultimasOlimpiadas = int(input())
  print("Digite o tipo de olimpíada:")
  tipoOlimpiada = input()
  anoFinal = date.today().year 
  anoInicial = anoFinal - (ultimasOlimpiadas * 4) 
  ultimaEdicao = int(anoFinal / 4)
  esportes = []
  quantidadeAtleta = {} 
  
  with open('./data/athlete_events.csv') as f: 

    reader = csv.reader(f) 
    next(reader)

    for linha in reader:
      edicaoDaLinha = int(int(linha[9]) / 4)
      if tipoOlimpiada == linha[10] and edicaoDaLinha > ultimaEdicao - ultimasOlimpiadas:
        esportes.append(linha[12]) if linha[12] not in esportes else esportes 
  
  for esporte in esportes: 

    quantidadeAtleta[esporte] = [] 

    for i in range(0, anoFinal - anoInicial):
      quantidadeAtleta[esporte].append(0)
  
  with open('./data/athlete_events.csv') as f:
    reader = csv.reader(f)

    next(reader) 

    for linha in reader:
      edicaoDaLinha = int(int(linha[9]) / 4)
      if tipoOlimpiada == linha[10] and edicaoDaLinha > ultimaEdicao - ultimasOlimpiadas:
          quantidadeAtleta[linha[12]][int(linha[9]) - anoFinal] += 1 
  

  fig2, ax2 = plt.subplots()
  for esporte in esportes:
    ax2.set_title(esporte)
    ax2.boxplot(quantidadeAtleta[esporte]);
    
  plt.show() 


def imprimeTextual(): # Textual - T4

  print("Digite o tipo de medalha que será analisado:")
  tipoMedalha = input() 

  medalhas = dict() 

  maiorMedalhista = 0 

  with open('./data/athlete_events.csv') as f:
    reader = csv.reader(f)
    next(reader)

    for linha in reader:

      quantidadeMedalhas = medalhas.get(linha[1]+ ' - ' + linha[8]) or 0 

      if tipoMedalha == linha[14]: 

        medalhas[linha[1] + ' - ' + linha[8]] = quantidadeMedalhas + 1 #Se positivo, soma 1

        if quantidadeMedalhas + 1 > maiorMedalhista: 

          maiorMedalhista = quantidadeMedalhas + 1

  print("O(s) maior(es) medalhista(s): ")
  for medalha in medalhas:
    if medalhas[medalha] == maiorMedalhista:
      print (medalha + " com " + str(maiorMedalhista) + " medalha(s) de " + tipoMedalha+".") 


#MENU INTERAÇÃO COM O USUÁRIO

while (tipoResposta not in ('1', '2', '3', '4')):
    print("Por favor escolha uma das opções abaixo:")
    print("1 - Gráfico de linhas")
    print("2 - Gráfico de barras")
    print("3 - Gráfico de boxplot")
    print("4 - Resposta textual")

    tipoResposta = input()

    if tipoResposta == '1':
        imprimeLinhas()
        break
    elif tipoResposta == '2':
        imprimeBarras()
        break
    elif tipoResposta == '3':
        imprimeBoxplot()
        break
    elif tipoResposta == '4':
        imprimeTextual()
        break
    else:
        print("Resposta inválida, tente novamente")
