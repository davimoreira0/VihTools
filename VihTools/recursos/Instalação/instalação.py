#Instalação da ferramenta
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
print(Fore.RED + texto_vihtools + Style.RESET_ALL)
print(Fore.WHITE + "Versão: 26.1!" + Style.RESET_ALL)
print(Fore.WHITE + "Criado por: Davi Moreira Pereira" + Style.RESET_ALL)
print(Fore.WHITE + "- GitHub: https://github.com/davimoreira0" + Style.RESET_ALL)
print(Fore.WHITE + "- Instagram: https://www.instagram.com/dmoreirap_/" + Style.RESET_ALL)

def instalar():
    print(Fore.WHITE + "Instalando a ferramenta..." + Style.RESET_ALL)
    time.sleep(1)
    
    #atualizando o sistema
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt install git -y")

    #Instalar: Reconhecimento (Reconnaissance): Fase inicial para coletar informações sobre o alvo, como domínios, IPs e dados públicos.
    os.system("sudo apt install theharvester -y")
    os.system("sudo apt install whois -y")

    #Varredura de Rede (Network Scanning): Identificação de hosts ativos, portas abertas e serviços em execução.
    os.system("sudo apt install nmap -y")

    #Avaliação de Vulnerabilidades (Vulnerability Assessment): Detecção de fraquezas conhecidas em sistemas e aplicativos..
    os.system("sudo apt install nikto -y")

    #Teste de Aplicações Web (Web Application Testing): Análise de vulnerabilidades em sites e apps web, como injeções e XSS.
    os.system("sudo apt install wpscan -y")

    #Exploração de Vulnerabilidades (Exploitation): Simulação de ataques para explorar falhas identificadas.
    os.system("sudo apt install metasploit-framework -y")

    #Quebra de Senhas (Password Cracking): Recuperação ou teste de força de senhas hashadas.
    os.system("sudo apt install john -y")

    #Análise de Tráfego de Rede (Sniffing/Network Analysis): Captura e inspeção de pacotes de dados na rede.
    os.system("sudo apt install tcpdump -y")

    #Hacking Wireless: Teste de segurança em redes Wi-Fi, incluindo criptografia e acessos não autorizados.
    os.system("sudo apt install aircrack-ng -y")
    os.system("sudo apt install wifite -y")

    #Engenharia Social (Social Engineering): Simulação de ataques baseados em manipulação humana.
    os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")

    #Injeção em Bancos de Dados (Database Exploitation): Teste de vulnerabilidades como SQL injection em bancos de dados.
    os.system("sudo apt install sqlmap -y")



user = input(Fore.RED + "Deseja instalar a ferramenta? (s/n): " + Style.RESET_ALL)
if user.lower() == "s":
    instalar()
    print(Fore.WHITE + "Instalação concluída!" + Style.RESET_ALL)
    user = input(Fore.RED + "Deseja abrir a ferramenta? (s/n): " + Style.RESET_ALL)
    if user.lower() == "s":
        os.system("bash start.sh")
    else:
        print(Fore.WHITE + "Saindo..." + Style.RESET_ALL)
else:
    print(Fore.WHITE + "Instalação cancelada." + Style.RESET_ALL)
