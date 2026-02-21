# VihTools
VihTools é uma coleção de scripts em Python para automação de tarefas de segurança ofensiva/educacional (reconhecimento, varredura, avaliação e exploração, cracking, análise de tráfego e engenharia social). O launcher principal é o menu da ferramenta.
🛡️ AutoPentest-Framework

    AutoPentest-Framework (v26.1) é uma ferramenta de automação desenvolvida para otimizar o fluxo de trabalho de profissionais de segurança da informação e hackers éticos. Ela centraliza e automatiza a execução de 10 ferramentas essenciais de testes de invasão.

⚠️ Aviso Legal (Disclaimer)

O uso deste programa para atacar alvos sem o consentimento prévio e mútuo é ilegal. É de inteira responsabilidade do usuário final obedecer a todas as leis locais, estaduais e federais aplicáveis. O desenvolvedor não assume nenhuma responsabilidade e não é responsável por qualquer uso indevido ou dano causado por este programa. Use apenas em ambientes controlados e autorizados.
🛠️ Categorias e Ferramentas

O sistema está dividido em 10 módulos estratégicos, cada um focado em uma fase específica do pentest:

    Reconhecimento de Rede * Ferramenta: Nmap - Automatiza varreduras de portas e identificação de serviços.

    Coleta de Informações (OSINT) * Ferramenta: theHarvester - Busca e-mails, subdomínios, hosts e nomes de funcionários em fontes públicas.

    Enumeração de Subdomínios * Ferramenta: Amass - Mapeamento profundo de superfície de ataque e descoberta de ativos externos.

    Fuzzing de Diretórios Web * Ferramenta: Gobuster - Descobre URIs ocultas (diretórios e arquivos) em servidores web de forma ultra-rápida.

    Varredura de Vulnerabilidades Web * Ferramenta: Nikto - Analisa servidores web em busca de arquivos perigosos, versões desatualizadas e problemas específicos.

    Injeção de Banco de Dados * Ferramenta: SQLmap - Detecta e explora automaticamente falhas de injeção de SQL (SQLi).

    Quebra de Senhas (Online Brute-force) * Ferramenta: Hydra - Ataques de dicionário e força bruta contra mais de 50 protocolos suportados (SSH, FTP, HTTP, etc).

    Análise de Redes Sem Fio (Wi-Fi) * Ferramenta: Aircrack-ng - Automação da captura de handshakes e quebra de chaves WEP/WPA/WPA2.

    Interceptação de Tráfego (Man-in-the-Middle) * Ferramenta: Bettercap - Framework completo para análise de rede e ataques de interceptação em tempo real.

    Engenharia Social * Ferramenta: Social-Engineer Toolkit (SET) - Automação de campanhas de phishing e clonagem de páginas web.

🚀 Pré-requisitos

Para rodar a versão 26.1, você precisará ter o sistema operacional Kali Linux ou Parrot OS (recomendado), pois a maioria das ferramentas já vem pré-instalada. Caso use outra distribuição, garanta que possui os seguintes pacotes:
Bash

sudo apt-get update
sudo apt-get install git python3 python3-pip nmap theharvester amass gobuster nikto sqlmap hydra aircrack-ng bettercap set

⚙️ Instalação

Siga os passos abaixo para clonar e configurar o ambiente:
Bash

# 1. Clone o repositório
git clone https://github.com/SeuUsuario/AutoPentest-Framework.git

# 2. Acesse o diretório
cd AutoPentest-Framework

# 3. Dê permissão de execução ao script principal
chmod +x install.sh
chmod +x autopentest.py

# 4. Execute a instalação de dependências (se aplicável)
./install.sh

💻 Como Usar

Para iniciar a interface de automação, execute o programa com privilégios de administrador (algumas ferramentas como Nmap em modo SYN e Aircrack requerem root):
Bash

sudo python3 autopentest.py
