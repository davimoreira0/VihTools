# VihTools
VihTools é uma coleção de scripts em Python para automação de tarefas de segurança ofensiva/educacional (reconhecimento, varredura, avaliação e exploração, cracking, análise de tráfego e engenharia social). O launcher principal é o menu da ferramenta.
![Logo do Projeto](./VihTools/recursos/VihToolsImage.jpg)
# ⚠️ Aviso Legal (Disclaimer)

O uso deste programa para atacar alvos sem o consentimento prévio e mútuo é ilegal. É de inteira responsabilidade do usuário final obedecer a todas as leis locais, estaduais e federais aplicáveis. O desenvolvedor não assume nenhuma responsabilidade e não é responsável por qualquer uso indevido ou dano causado por este programa. Use apenas em ambientes controlados e autorizados.
🛠️ Categorias e Ferramentas

**O sistema está dividido em 10 módulos estratégicos, cada um focado em uma fase específica do pentest:
Principais recursos**
- Reconhecimento: [`theharvester`](recursos/ferramenta/CATEGORIAS/RECONHECIMENTO/theharvestert.py)
- Varredura de rede: [`menu_principal` -> Nmap](recursos/ferramenta/MENU PRINCIPAL/menuprincipal.py) / [`nmap`](recursos/ferramenta/CATEGORIAS/VARREDURA DE REDE/nmapt.py)
- Avaliação de vulnerabilidades: [`nikto`](recursos/ferramenta/CATEGORIAS/AVALIAÇÃO DE VULNERABILIDADES/niktot.py)
- Testes Web: [`wpscan`](recursos/ferramenta/CATEGORIAS/TESTES DE APLICAÇÃO WEB/wpscant.py)
- Exploração: [`metasploit`](recursos/ferramenta/CATEGORIAS/EXPLORAÇÃO DE VULNERABILIDADES/metasploitt.py)
- Quebra de senhas: [`john`](recursos/ferramenta/CATEGORIAS/QUEBRA DE SENHAS/johnt.py)
- Análise de tráfego: [`tcpdump`](recursos/ferramenta/CATEGORIAS/ANALISE DE TRÁFEGO DE REDE/tcpdumpt.py)
- Hacking Wireless: [`aircrack`](recursos/ferramenta/CATEGORIAS/HACKING WINRELESS/aircrack-ngt.py), [`wifite`](recursos/ferramenta/CATEGORIAS/HACKING WINRELESS/wifitet.py)
- Engenharia Social: [`zphisher`](recursos/ferramenta/CATEGORIAS/ENGENHARIA SOCIAL/zphishert.py)
- Wordlists integradas: [recursos/ferramenta/CATEGORIAS/WORDLISTS/WORDLIST.txt](recursos/ferramenta/CATEGORIAS/WORDLISTS/WORDLIST.txt)

# 🚀 Pré-requisitos

Para rodar a versão 26.1, você precisará ter o sistema operacional Kali Linux ou Parrot OS (recomendado), pois a maioria das ferramentas já vem pré-instalada. Caso use outra distribuição, garanta que possui os seguintes pacotes:
Bash

    sudo apt-get update
    sudo apt-get upgrade

# ⚙️ Instalação

Siga os passos abaixo para clonar e configurar o ambiente:
Bash

# 1. Clone o repositório
    git clone https://github.com/davimoreira0/VihTools.git

# 2. Acesse o diretório
    cd VihTools

# 3. Dê permissão de execução ao script principal
    chmod +x instalação.sh
    chmod +x vihtool.sh
# 4 Desisntalação
    chmod +x desinstalação.sh

# 💻 Como Usar

Para iniciar a interface de automação, execute o programa com privilégios de administrador (algumas ferramentas como Nmap em modo SYN e Aircrack requerem root):
Bash

    sudo bash vihtool.sh

# Desisntalar
    bash desinstalação.sh
