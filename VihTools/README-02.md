# VihTools

VihTools é uma coleção de scripts em Python para automação de tarefas de segurança ofensiva/educacional (reconhecimento, varredura, avaliação e exploração, cracking, análise de tráfego e engenharia social). O launcher principal é o menu da ferramenta.

Principais recursos
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

Instalação rápida
- Scripts de instalação: [recursos/Instalação/instalação.py](recursos/Instalação/instalação.py)
- Scripts de desinstalação: [recursos/desinstalação/desisntalação.py](recursos/desinstalação/desisntalação.py)

Como usar
1. Executar o launcher:
   - `bash vihtool.sh` ou `python3 recursos/ferramenta/MENU\ PRINCIPAL/menuprincipal.py`
2. Navegar pelo menu e escolher categorias e ferramentas.

Observações
- Muitos módulos chamam ferramentas do sistema (nmap, sqlmap, john, tcpdump, aircrack, wifite, msfconsole, etc.). Execute com permissões adequadas (às vezes sudo).
- Este repositório fornece wrappers para ferramentas existentes — leia a documentação de cada ferramenta antes de usar.

Estrutura principal (selecionada)
- [recursos/ferramenta/MENU PRINCIPAL/menuprincipal.py](recursos/ferramenta/MENU PRINCIPAL/menuprincipal.py)
- [recursos/ferramenta/CATEGORIAS/INJEÇÃO EM BANCO DE DADOS/sqlmapt.py](recursos/ferramenta/CATEGORIAS/INJEÇÃO EM BANCO DE DADOS/sqlmapt.py)
- [recursos/ferramenta/CATEGORIAS/QUEBRA DE SENHAS/johnt.py](recursos/ferramenta/CATEGORIAS/QUEBRA DE SENHAS/johnt.py)
- [recursos/ferramenta/CATEGORIAS/WORDLISTS/WORDLIST.txt](recursos/ferramenta/CATEGORIAS/WORDLISTS/WORDLIST.txt)


Autor
- Criado por: Davi Moreira Pereira (metadados no próprio menu principal).
- GitHub: https://github.com/davimoreira0
- Instagram: https://www.instagram.com/dmoreirap_/
