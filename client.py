import socket

def client(host="ip", porta="7444") #bcolocar nosso ip
    try:

#criar socket TCP/IP
         cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar ao servidor
        cliente_socket.connect((host, porta))
        print(f"conectado ao servidor{hosts}:{porta}")

#enviar mensagem ao servidor
        mensagem="Olá"
        cliente_socket.sendall(mensagem.encode('utf-8'))
        print(f"Mensagem enviada:{Mensagem}")

#recebe resposta do servidor
        resposta=cliente_socket.recev(8)
        print(f"Resposta do servidor:{resposta.decode('utf-8')}")

except ConnectionError as e:
    print(f"Erro de Conexão:{e}")

finally:
#fechar conexão
    cliente_socket.close()
    print("Conexão encerrada")

#executar cliente
if __name__ == "__main__":
    cliente()
    
