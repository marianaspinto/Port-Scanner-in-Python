# A biblioteca Socket permite estabeleccer conexões TCP ou UDP,
# que são essenciais para escanear portas em um endereço IP ou Domínio.
import socket

# Solicitar IP ou Domínio que deseja escanear.
alvo = input("Digite o endereço IP ou domínio para escanear.")

# Definir um intervalo de portas.
inicio_de_porta = int(input("Digite o número da porta incial."))
fim_de_porta = int(input("Digite o núemro da porta final."))

# Criando a função de escaneamento de portas
def escanear_porta(ip, porta):
    try:
        # Criar um socket do tipo TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Define um tempo limite de 1 segundo para cada tentativa 

        # Tenta se conectar ao IP e porta especificados
        resultado = sock.connect_ex((ip, porta))

        if resultado == 0:
            print(f"Porta {porta} está aberta.")
        sock.close()
    except socket.error as erro:
        print(f"Não foi possível conectar ao servidor: {erro}")
    except KeyboardInterrupt:
        print("\nEscaneamento interrompido pelo usuário.")
        exit()

# Usar a função "escanear_porta()" em um loop para verificar todas as
# portas dentro da faixa definida
print(f"\nIniciando escaneamento do alvo: {alvo}\n")
for porta in range(inicio_de_porta, fim_de_porta + 1):
        escanear_porta(alvo, porta)