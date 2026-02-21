#JOHN
import os
from colorama import Fore, Style
import time


texto_vihtools = r"""
 ██▒   █▓ ██▓ ██░ ██ ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░   █▒▓██▒▓██░ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ▒██    ▒ 
 ▓██  █▒░▒██▒▒██▀▀██░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░     ░ ▓██▄   
  ▒██ █░░░██░░▓█ ░██ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ▒   ██▒
   ▒▀█░  ░██░░▓█▒░██▓  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
   ░ ▐░  ░▓   ▒ ░░▒░▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
   ░ ░░   ▒ ░ ▒ ░▒░ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
     ░░   ▒ ░ ░  ░░ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
      ░   ░   ░  ░  ░             ░ ░      ░ ░      ░  ░      ░  
""" 

def john():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: QUEBRA DE SENHAS - JOHN" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do John:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Gerar o Hash da Senha" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Ataque de Senha Zipada" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Ataque de Senha PDF" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Voltar" + Style.RESET_ALL)

    user_john = input(Fore.RED + "Selecione um recurso pelo número correspondente: " + Style.RESET_ALL)

    def gerar_hash_senha():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        user_gerar_hash_senha = input(Fore.RED + "Digite a senha escolhida: " + Style.RESET_ALL)
        os.system(f'echo -n "{user_gerar_hash_senha}" | md5sum')

        user_menu = input(Fore.RED + "Deseja voltar para o menu de recursos do John? (s/n): " + Style.RESET_ALL)
        if user_menu == 's':
            john()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def Ataque_de_Senha_Zipada():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)

        user_senha_zipada = input(Fore.RED + "Digite o caminho do arquivo .zip: " + Style.RESET_ALL)
        user_wordlist = input(Fore.RED + "Digite o caminho da sua wordlist: " + Style.RESET_ALL)
        os.system(f'zip2john "{user_senha_zipada}" > ziphash.txt')
        os.system(f'john --wordlist="{user_wordlist}" ziphash.txt')
        user_menu = input(Fore.RED + "Deseja voltar para o menu de recursos do John? (s/n): " + Style.RESET_ALL)
        if user_menu == 's':
            john()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)

    def ataque_de_senha_pdf():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)

        user_senha_pdf = input(Fore.RED + "Digite o caminho do arquivo .pdf: " + Style.RESET_ALL)
        user_wordlist = input(Fore.RED + "Digite o caminho da sua wordlist: " + Style.RESET_ALL)
        os.system(f'pdf2john.pl "{user_senha_pdf}" > pdfhash.txt')
        os.system(f'john --wordlist="{user_wordlist}" pdfhash.txt')
        user_menu = input(Fore.RED + "Deseja voltar para o menu de recursos do John? (s/n): " + Style.RESET_ALL)
        if user_menu == 's':
            john()
        else:
            print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
            time.sleep(1)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
            time.sleep(1)


        



    if user_john == "1":
        gerar_hash_senha()
    elif user_john == "2":
        Ataque_de_Senha_Zipada()
    elif user_john == "3":
        ataque_de_senha_pdf()
    elif user_john == "4":
        print(Fore.RED + "Voltando para o menu principal..." + Style.RESET_ALL)
        time.sleep(1)
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        john()

john()