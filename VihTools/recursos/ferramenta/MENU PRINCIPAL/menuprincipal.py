#MENU PRINCIPAL DA FERRAMENTA VihTools
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

def menu_principal():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "Versão: 26.1!" + Style.RESET_ALL)
    print(Fore.WHITE + "Criado por: Davi Moreira Pereira" + Style.RESET_ALL)
    print(Fore.RED + "- GitHub: https://github.com/davimoreira0" + Style.RESET_ALL)
    print(Fore.RED + "- Instagram: https://www.instagram.com/dmoreirap_/" + Style.RESET_ALL)

    print(Fore.WHITE + "CATEGORIAS:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Reconhecimento (Reconnaissance)" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Varredura de Rede (Network Scanning)" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Avaliação de Vulnerabilidades (Vulnerability Assessment)" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Teste de Aplicações Web (Web Application Testing)" + Style.RESET_ALL)
    print(Fore.WHITE + "[5] Exploração de Vulnerabilidades (Exploitation)" + Style.RESET_ALL)
    print(Fore.WHITE + "[6] Quebra de Senhas (Password Cracking)" + Style.RESET_ALL)
    print(Fore.WHITE + "[7] Análise de Tráfego de Rede (Sniffing/Network Analysis)" + Style.RESET_ALL)
    print(Fore.WHITE + "[8] Hacking Wireless" + Style.RESET_ALL)
    print(Fore.WHITE + "[9] Engenharia Social (Social Engineering)" + Style.RESET_ALL)
    print(Fore.WHITE + "[10] Injeção em Bancos de Dados (Database Exploitation)" + Style.RESET_ALL)
    print(Fore.WHITE + "[0] Sair" + Style.RESET_ALL)
menu_principal()

user = input(Fore.RED + "Selecione uma categoria pelo número correspondente: " + Style.RESET_ALL)


#categoria 1
def reconhecimento():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: RECONHECIMENTO (RECONNAISSANCE)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] TheHarvester" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Whois" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Voltar" + Style.RESET_ALL)

    user_reconhecimento = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)

    if user_reconhecimento == "1":
        os.system('clear')
        os.system('python3 recursos/ferramenta/CATEGORIAS/RECONHECIMENTO/theharvestert.py')
    elif user_reconhecimento == "2":
        os.system('clear')
        os.system('python3 recursos/ferramenta/CATEGORIAS/RECONHECIMENTO/whoist.py')
    elif user_reconhecimento == "3":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        reconhecimento()
        time.sleep(1)

#categoria 2
def varredura_de_rede():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: VARREDURA DE REDE (NETWORK SCANNING)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Nmap" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_varredura_de_rede = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_varredura_de_rede == "1":
        os.system('clear')
        os.system('python3 recursos/ferramenta/CATEGORIAS/VARREDURA\ DE\ REDE/nmapt.py')
    elif user_varredura_de_rede == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        varredura_de_rede()
        time.sleep(1)

#categiria 3
def avaliacao_de_vulnerabilidades():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: AVALIAÇÃO DE VULNERABILIDADES (VULNERABILITY ASSESSMENT)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Nikto" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_avaliacao_de_vulnerabilidades = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    
    if user_avaliacao_de_vulnerabilidades == "1":
        os.system('clear')
        os.system('python3 recursos/ferramenta/CATEGORIAS/AVALIAÇÃO\ DE\ VULNERABILIDADES/niktot.py')
    elif user_avaliacao_de_vulnerabilidades == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        avaliacao_de_vulnerabilidades()
        time.sleep(1)

#categoria 4
def teste_de_aplicacoes_web():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: TESTE DE APLICAÇÕES WEB (WEB APPLICATION TESTING)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Wpscan" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_teste_de_aplicacoes_web = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    
    if user_teste_de_aplicacoes_web == "1":
        os.system('clear')
        os.system('python3 recursos/ferramenta/CATEGORIAS/TESTES\ DE\ APLICAÇÃO\ WEB/wpscant.py')
    elif user_teste_de_aplicacoes_web == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        teste_de_aplicacoes_web()
        time.sleep(1)

#categoria 5
def exploracao_de_vulnerabilidades():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: EXPLORAÇÃO DE VULNERABILIDADES (EXPLOITATION)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Metasploit" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_exploracao_de_vulnerabilidades = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_exploracao_de_vulnerabilidades == '1':
        os.system('python3 recursos/ferramenta/CATEGORIAS/EXPLORAÇÃO\ DE\ VULNERABILIDADES/metasploitt.py')
    elif user_exploracao_de_vulnerabilidades == '2':
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        exploracao_de_vulnerabilidades()
        time.sleep(1)


#categoria 6
def quebra_de_senhas():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: QUEBRA DE SENHAS (PASSWORD CRACKING)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] John the Ripper" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_quebra_de_senhas = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_quebra_de_senhas == "1":
        os.system('python3 recursos/ferramenta/CATEGORIAS/QUEBRA\ DE\ SENHAS/johnt.py')
    elif user_quebra_de_senhas == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        quebra_de_senhas()
        time.sleep(1)



#categoria 7
def analise_de_trafego_de_rede():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: ANÁLISE DE TRÁFEGO DE REDE (SNIFFING/NETWORK ANALYSIS)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Tcpdump" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_analise_de_trafego_de_rede = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_analise_de_trafego_de_rede == "1":
        os.system('python3 recursos/ferramenta/CATEGORIAS/ANALISE\ DE\ TRÁFEGO\ DE\ REDE/tcpdumpt.py')
    elif user_analise_de_trafego_de_rede == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        analise_de_trafego_de_rede()
        time.sleep(1)

#categoria 8
def hacking_wireless():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: HACKING WIRELESS" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Aircrack-ng" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Wifite" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Voltar" + Style.RESET_ALL)

    user_hacking_wireless = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_hacking_wireless.lower() == "1":
        os.system('python3 recursos/ferramenta/CATEGORIAS/HACKING\ WINRELESS/aircrack-ngt.py')
    elif user_hacking_wireless.lower() == "2":
        os.system('python3 recursos/ferramenta/CATEGORIAS/HACKING\ WINRELESS/wifitet.py')
    elif user_hacking_wireless.lower() == "3":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
        hacking_wireless()
        time.sleep(1)


#categoria 9
def engenharia_social():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: ENGENHARIA SOCIAL (SOCIAL ENGINEERING)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Zphisher" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_engenharia_social = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_engenharia_social.lower() == "1":
        os.system('python3 recursos/ferramenta/CATEGORIAS/ENGENHARIA\ SOCIAL/zphishert.py')
    elif user_engenharia_social.lower() == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        engenharia_social()

#categoria 10
def injeção_em_bancos_de_dados():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)
    print(Fore.WHITE + "CATEGORIA: INJEÇÃO EM BANCOS DE DADOS (DATABASE EXPLOITATION)" + Style.RESET_ALL)
    print(Fore.WHITE + "Ferramentas disponíveis:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] SQLmap" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Voltar" + Style.RESET_ALL)

    user_injecao_em_bancos_de_dados = input(Fore.RED + "Selecione uma ferramenta pelo número correspondente: " + Style.RESET_ALL)
    if user_injecao_em_bancos_de_dados.lower() == "1":
        os.system('python3 recursos/ferramenta/CATEGORIAS/INJEÇÃO\ EM\ BANCO\ DE\ DADOS/sqlmapt.py')
    elif user_injecao_em_bancos_de_dados.lower() == "2":
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        injeção_em_bancos_de_dados()
        


#escolha do usuário

if user == "1":
    reconhecimento()
elif user == "2":
    varredura_de_rede()
elif user == "3":
    avaliacao_de_vulnerabilidades()
elif user == "4":
    teste_de_aplicacoes_web()
elif user == "5":
    exploracao_de_vulnerabilidades()
elif user == "6":
    quebra_de_senhas()
elif user == "7":
    analise_de_trafego_de_rede()
elif user == "8":
    hacking_wireless()
elif user == "9":
    engenharia_social()
elif user == "10":
    injeção_em_bancos_de_dados()
elif user == "0":
    print(Fore.RED + "Saindo..." + Style.RESET_ALL)
else:
    print(Fore.RED + "Opção inválida. Por favor, selecione um número válido." + Style.RESET_ALL)
    os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    time.sleep(1)

