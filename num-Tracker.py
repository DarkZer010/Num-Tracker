'''
ShadowByte

ALL FOR KNOWLEDGE
'''
# importa as bibliotecas
import phonenumbers
from phonenumbers import geocoder
from colorama import init, Fore, Style
import pyfiglet
import os
import time
import sys

# inicia o colorama
init()

# função limpar_tela
def limpar_tela():
    # apagar tudo no comeco e amostrar a logo num-Tracker
    os.system("cls")
    if sys.platform == "linux"":
       os.system("clear")
       
limpar_tela()

# criar uma função, e cria um texto grande "num-Tracker"
def nome_da_ferramenta():
    logo = "num-Tracker"
    resultado = pyfiglet.figlet_format(logo)
    print(resultado)
    
nome_da_ferramenta()

# função "numero"
def numero();
    # digitar um numero de telefone e se não tiver nada, imprime uma mensagem
    numero = input(Fore.CYAN + "digite um numero de telefone: " + Style.RESET_ALL)
    if not numero:
	    print(Fore.YELLOW + "nenhum número digitado" + Style.RESET_ALL)
	    exit()

    # parsear o numero
    num = phonenumbers.parse(numero)
    time.sleep(3)
    
numero()

# função "localizacao"
def localizacao():
    # imprime: localizaçao e diz a localização do numero
    print(Fore.RED+ "\nlocalização:" + Style.RESET_ALL)
    print(geocoder.description_for_number(num, 'pt', "en", "fr", "es"))
    
loalizacao()
