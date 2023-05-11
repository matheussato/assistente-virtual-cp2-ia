import datetime
import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import wikipedia
import requests
import os
from random import randint
import cv2

fala = pyttsx3.init()


def escuta():
    recon = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Fale agora.")
        audio = recon.listen(mic)
        print("Reconhecendo...")
        try:
            comando = recon.recognize_google(audio, language='pt-br')
            print(comando)
            return comando
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            return ""
        except sr.RequestError as e:
            print("Não foi possível conectar-se ao serviço de reconhecimento de fala; {0}".format(e))
            return ""

def Speaker(saida):
    fala.setProperty('voice',b'brasil')
    fala.setProperty('rate',160)
    fala.setProperty('volume',1)
    fala.say(saida)
    fala.runAndWait()

def clima():
    global temperatura
    global descricao
    API_KEY = "Colocar a KEY da API aqui"
    cidade = "são paulo"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp']
    Speaker("A temperatura é " + str(temperatura) + " graus, com " + str(descricao) )

def conta(fala):
    

        fala = fala.replace("quanto é", "")
        n1, l, n2 = fala.split()

        print("Resultado: ")

        if l == 'x':
            resultado = int(n1) * int(n2)
            Speaker(str(resultado))
            print(resultado)

        elif l == '+':
            resultado = int(n1) + int(n2)
            Speaker(str(resultado))
            print(resultado)

        elif l == '-':
            resultado = int(n1) - int(n2)
            Speaker(str(resultado))
            print(resultado)

        elif l == '/':
            resultado = int(n1) / int(n2)
            Speaker(str(resultado))
            print(resultado)
    
def hora():
    hora = datetime.datetime.now().strftime("%I:%M")
    Speaker("Agora são: " + str(hora))

def data():
    ano = int(datetime.datetime.now().year)
    mes = int(datetime.datetime.now().month)
    dia = int(datetime.datetime.now().day)
    Speaker("Hoje é, " + str(dia) + " de " + str(mes) + " de " + str(ano))

def abertura():
    Speaker("O que eu devo fazer meu mestre?")

def tocar(resultado):
    result = pywhatkit.playonyt(resultado)
    Speaker("Tudo certo")

def buscar(result):
    try:
        pesquisa = result.replace("procure por", "")
        peeq = ("https://www.google.com.br/search?q=")
        peq_final = (peeq + pesquisa)
        feito = webbrowser.open(peq_final)
        Speaker("Aqui está o que encontrei")
    except Exception as ex:
        Speaker("Não encontrei resultados")

def wiki(rs):
    try:
        wikipedia.set_lang("pt")
        resultado = wikipedia.summary(rs,2)
        print(resultado)
        Speaker(resultado)
    except Exception as ex:
        Speaker("Não encontrei resultados")

def bom_dia():
    hora  = datetime.datetime.now().hour
    ano = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day

    if hora >= 6 and hora < 12:
        Speaker(f"Olá, bom dia, hoje é dia {str(dia)} de {str(mes)} de {str(ano)}, agora são {str(hora)} horas")

    elif hora >= 12 and hora < 18:
        Speaker(f"Agora são {hora} horas o correto seria, Boa Tarde")

    elif hora >= 18 and hora < 24:
        Speaker(f"Agora são {hora} horas o correto seria, Boa Noite")

    else: Speaker("Está de madrugada, vá dormir")

def boa_tarde():
    hora = datetime.datetime.now().hour
    ano = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day

    if hora >= 6 and hora < 12:
        Speaker(f"Agora são {hora} horas o correto seria, Bom dia")

    elif hora >= 12 and hora < 18:
        Speaker(f"Olá, tarde, hoje é dia {str(dia)} de {str(mes)} de {str(ano)}, agora são {str(hora)} horas")

    elif hora >= 18 and hora < 24:
        Speaker(f"Agora são {hora} horas o correto seria, Boa Noite")

    else:
        Speaker("Está de madrugada, vá dormir")

def boa_noite():
    hora = datetime.datetime.now().hour
    ano = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day

    if hora >= 6 and hora < 12:
        Speaker(f"Agora são {hora} horas o correto seria, Bom Dia")

    elif hora >= 12 and hora < 18:
        Speaker(f"Agora são {hora} horas o correto seria, Boa Tarde")

    elif hora >= 18 and hora < 24:
        Speaker(f"Olá, boa noite, hoje é dia {str(dia)} de {str(mes)} de {str(ano)}, agora são {str(hora)} horas")

    else:
        Speaker("Está de madrugada, vá dormir")
        
def continuar(resp):
    if resp == 'sim':
        return True
    return False

def jogar():
    print("Abrindo")
    Speaker("Abrindo")
    Speaker("Vamos matar uns pratinhas")
    os.startfile("D:\Riot Games\Riot Client\RiotClientServices.exe")

def corno():
    items = [
        "Abelha: O que vai para rua fazer cera e volta cheio de mel.",
        "Ateu: Aquele que leva chifre mas não acredita.",
        "Atleta - É aquele que descobre que leva chifre sai correndo para casa.",
        "Atrevido: Aquele que se mete na conversa da mulher com o Ricardão.",
        "Xuxa: O que não larga a mulher por causa dos baixinhos.",
        "Banana: A mulher vai embora e deixa uma penca de filhos.",
        "Brahma: O que pensa que é o número 1.",
        "Bravo: Aquele que quando é chamado de corno, quer brigar.",
        "Brincalhão: Aquele que leva chifre o ano inteiro e no carnaval sai fantasiado de côrno.",
        "Bateria: O que vive dizendo, 'Vou tomar uma solução'.",
        "Burro - é aquele que segue a mulher o tempo todo e quando flagra exclama: 'Eu não entendo!!!'.",
        "Camarada: Aquele que ainda empresta dinheiro para o Ricardão.",
        "Vingativo: Aquele que descobre que é corno e vai para a rua dar para qualquer um.",
        "Cebola: Quando vê a mulher com outro só chora.",
        "Vidente: Aquele que diz 'eu já sabia'.",
        "Churrasco: Aquele que mete a mão no fogo pela mulher.",
        "Cigano: Aquele que toda vez que leva chifre, muda de bairro.",
        "Crente: Aquele que sempre crê que sua mulher é honesta.",
        "Teimoso: O que leva chifre da mulher e da amante.",
        "Denorex: Aquele que não parece, mas é.",
        "Descarado: Aquele que leva chifre e ainda sai desfilando com a mulher.",
        "Desconfiado: Aquele que quando chega em casa procura o Ricardão até atrás dos quadros.",
        "Detetive: Aquele que segue a mulher dos cornos e esquece da dele.",
        "Dinossauro: Quando chega em casa grita, 'Querida cheguei'.",
        "Educado: Aquele que aprendeu com o pai e nunca deixa de cumprimentar o Ricardão.",
        "Recado: Aquele que ainda leva bilhete da mulher para o Ricardão.",
        "Familiar: Aquele que leva chifre de parente.",
        "Famoso: Aquele que por onde passa é reconhecido como tal.",
        "Fofoqueiro: Aquele que leva chifre e sai contando para todo mundo.",
        "Preguiça: O que só chega atrasado, 'Eu ainda te pego'.",
        "Frio: O que leva chifre e não esquenta.",
        "Político: Aquele que só faz promessa para resolver este problema.",
        "Granja: O que dá casa e os outros comem.",
        "Inflação: A cada dia que passa o chifre"]
    
    i = randint(0, 39)
    
    Speaker("corno" + items[i])    

def piada():
    Speaker("Vou fazer uma piada para alegrar seu dia, Toque Toque")

def buscar_filme():
    link = 'https://imdb-api.com/en/API/Top250Movies/k_hd9q4amm'
    i = randint(0, 249)
    
    requisicao = requests.get(link).json()
    filme = requisicao['items'][i]
    titulo = filme['title']
    ano = filme['year']
    diretor = filme['crew'].split("(")[0]
    print(titulo)
    Speaker("Eu recomendo o filme: " + titulo + " lançado em " + ano + " Do diretor: " + diretor)
    
def escreva():
    tarefa = ''
    Speaker("Por favor descreva a tarefa")
    tarefa = escuta()
    file = open("Tarefas.txt", "a", encoding='utf-8')
    file.write('\n-' + tarefa)
    file.close()
    
def listar_tarefas():
    arq = open("Tarefas.txt", "r", encoding='utf-8')
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)
        Speaker(linha)

def tirar_foto():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    while True:
        key = cv2.waitKey(1) # espera por 1 milissegundo
        
        if key & 0xFF == ord('s'):
            break

        if key & 0xFF == ord('t'):
            cv2.imwrite('img/foto.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()

import os
from PIL import Image

def abrir_fotos(diretorio, extensao=".jpg"):
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith(extensao):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            imagem = Image.open(caminho_arquivo)
            imagem.show()