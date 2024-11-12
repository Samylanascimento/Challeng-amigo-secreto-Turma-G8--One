import socket
import json
import base64
import hashlib
from cryptography.fernet import Fernet

# Gera a mesma chave usada pelo servidor para criptografia
KEY = base64.urlsafe_b64encode(hashlib.sha256(b'qweasd').digest())
cipher_suite = Fernet(KEY)

def send_request(request_data):
    HOST = '201.58.194.75'  # IP do servidor
    PORT = 7444             # Porta do servidor
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        
        # Serializa e criptografa os dados da requisição
        encrypted_data = cipher_suite.encrypt(json.dumps(request_data).encode())
        
        # Envia o comprimento da mensagem criptografada
        message_length = f"{len(encrypted_data):<10}"
        client_socket.sendall(message_length.encode() + encrypted_data)
        
        # Recebe o comprimento da resposta
        encrypted_length = int(client_socket.recv(10).decode().strip())
        
        # Recebe e descriptografa os dados da resposta
        encrypted_response = client_socket.recv(encrypted_length)
        response_data = cipher_suite.decrypt(encrypted_response).decode()
        
        return json.loads(response_data)

# Funções para operações de autenticação, envio de mensagem e criação de usuário
def autenticar_usuario(nickname, senha):
    request = {
        "flag": 0,
        "User": nickname,
        "Pass": senha
    }
    return send_request(request)

def enviar_mensagem(remetente, destinatario, conteudo_email):
    request = {
        "flag": 1,
        "User": remetente,
        "destinatario": destinatario,
        "conteudo_email": conteudo_email
    }
    return send_request(request)

def criar_usuario(nickname, senha):
    request = {
        "flag": 3,
        "User": nickname,
        "Pass": senha
    }
    return send_request(request)

# Exemplo de uso do cliente
if __name__ == "__main__":
     nickname = "cataanasamy"  # Substitua por um nome de usuário desejado
     senha = "senha123"        # Substitua por uma senha desejada

# Chama a função para criar o usuário
response = criar_usuario(nickname, senha)
print("Resposta criação de usuário:", response)

    # Criar um usuário
response = criar_usuario("testuser", "testpass")
print("Resposta criação de usuário:", response)
    
    # Autenticar o usuário
response = autenticar_usuario("testuser", "testpass")
print("Resposta autenticação:", response)
    
    # Enviar uma mensagem para outro usuário
response = enviar_mensagem("testuser", "otheruser", "Olá, esta é uma mensagem de teste!")
print("Resposta envio de mensagem:", response)
