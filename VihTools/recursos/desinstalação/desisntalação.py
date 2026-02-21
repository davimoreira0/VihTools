#desisntalação das ferramentas
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
print(Fore.WHITE + "- GitHub: https://github.com/davimoreira0" + Style.RESET_ALL)
print(Fore.WHITE + "- Instagram: https://www.instagram.com/dmoreirap_/" + Style.RESET_ALL)

def desinstalar():
    print(Fore.WHITE + "Desinstalando a ferramenta..." + Style.RESET_ALL)
    time.sleep(1)
    
    #desinstalando as ferramentas)
    os.system("sudo apt remove nmap -y")
    os.system("sudo apt remove theharvester -y")
    os.system("sudo apt remove whois -y")
    os.system("sudo apt remove nikto -y")
    os.system("sudo apt remove metasploit-framework -y")
    os.system("sudo apt remove john -y")
    os.system("sudo apt remove tcpdump -y")
    os.system("sudo apt remove aircrack-ng -y")
    os.system("sudo apt remove wifite -y")
    os.system("sudo apt remove sqlmap -y")
    os.system("rm -rf zphisher")

user = input(Fore.RED + "Deseja desinstalar a ferramenta? (s/n): " + Style.RESET_ALL)

if user.lower() == "s":
    desinstalar()
