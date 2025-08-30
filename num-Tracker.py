import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import init, Fore, Style
import pyfiglet
import os
import time
import sys

init()

def limpar_tela():
    os.system("cls" if sys.platform == "win32" else "clear")

def nome_da_ferramenta():
    lg = pyfiglet.figlet_format("TN-LOC")
    print(Fore.YELLOW + f"{lg}" + Style.RESET_ALL)

def Tracker():
    numero = input(Fore.CYAN + "Digite um número de telefone (com +código do país): " + Style.RESET_ALL)
    if not numero:
        print(Fore.YELLOW + "Nenhum número digitado" + Style.RESET_ALL)
        exit()

    num = phonenumbers.parse(numero)
    time.sleep(2)

    print(Fore.RED + "\nInformações do telefone:" + Style.RESET_ALL)
    
    estado = geocoder.description_for_number(num, "pt")
    pais = phonenumbers.region_code_for_number(num)
    
    codigo_postal = num.country_code
    validacao_num = phonenumbers.is_valid_number(num)
    
    validacao_CodigoPostal = phonenumbers.is_possible_number(num)
    formatacao = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    operadora = carrier.name_for_number(num, "pt")
    
    print(Fore.BLUE+"\nEstado/Região:", estado, "País:", pais, f"\nOperadora: {operadora}", "\nCodigo postal:", codigo_postal, "\nNumero valido: ", validacao_num, "\nCodigo postal valido:", validacao_CodigoPostal, "\nFormato:", formatacao)

if __name__ == "__main__":
    limpar_tela()
    nome_da_ferramenta()
    Tracker()
			
