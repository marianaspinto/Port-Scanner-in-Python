# A biblioteca Socket permite estabeleccer conexões TCP ou UDP,
# que são essenciais para escanear portas em um endereço IP ou Domínio.
import socket
import threading # Torna o escaneamento mais rápido

# Solicitar IP ou Domínio que deseja escanear.
alvo = input("Digite o endereço IP ou domínio para escanear.")

# Solicitar protocolo inserido
protocolo = input ("Escolha o protocolo (TCP/UDP): ").strip().upper()

#Validar o protocolo inserido
if protocolo not in ["TCP", "UDP"]:
     print("Protocolo inválido! Por favor, esclha entre 'TPC' ou 'UDP'.")
     exit()

# Definir um intervalo de portas.
inicio_de_porta = int(input("Digite o número da porta incial."))
fim_de_porta = int(input("Digite o núemro da porta final."))

# Criando a função de escaneamento de portas para TCP
def escanear_porta_tcp(ip, porta):
    try:
        # Criar um socket tipo TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Define um tempo limite de 1 segundo para cada tentativa 

        # Tenta se conectar ao IP e porta especificados
        resultado = sock.connect_ex((ip, porta))

        if resultado == 0:
            print(f"Porta TCP {porta} está aberta.")
        sock.close()
    except socket.error as erro:
        print(f"Erro no TCP: {erro}")


# Criando a função de escaneamento de portas para UDP
def escanear_porta_udp(ip, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b"Teste", (ip, porta))
        resposta, _ = sock.recvfrom(1024)
        print(f"Porta UDP {porta} está aberta. Resposta: {resposta}")
        sock.close()
    except socket.timeout:
        print(f"Porta UDP {porta} não respondeu (pode estar fechada).")
    except socket.error as erro:
        print(f"Erro no UDP:{erro}")

# Função principal para iniciar o escaneamento com threads
def escanear_tcp_com_threads(ip, portas, timeout):
     for porta in portas:
          thread =threading.Thread(target=escanear_porta_tcp, args=(ip, porta, timeout))
          thread.start()        



