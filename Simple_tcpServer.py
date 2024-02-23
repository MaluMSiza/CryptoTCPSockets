from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

def cesar(msgByte, chave):
    encrypted_bytes = bytearray()
    for byte in msgByte:
        encrypted_byte = (byte + chave) % 256 
        encrypted_bytes.append(encrypted_byte)
    return bytes(encrypted_bytes)

def maiuscula(byte_sequence):
    string = byte_sequence.decode("utf-8")
    conversion_table = {
        'á': 'Á',
        'à': 'À',
        'â': 'Â',
        'ã': 'Ã',
        'ä': 'Ä',
        'é': 'É',
        'è': 'È',
        'ê': 'Ê',
        'ë': 'Ë',
        'í': 'Í',
        'ì': 'Ì',
        'î': 'Î',
        'ï': 'Ï',
        'ó': 'Ó',
        'ò': 'Ò',
        'ô': 'Ô',
        'õ': 'Õ',
        'ö': 'Ö',
        'ú': 'Ú',
        'ù': 'Ù',
        'û': 'Û',
        'ü': 'Ü',
        'ç': 'Ç'
    }
    uppercase_string = ''.join(conversion_table.get(char, char.upper()) for char in string)
    return uppercase_string  

# Parâmetros compartilhados 
num_G = 23  
num_N = 5    
# chave bob
y = 46

r2 = (num_G**y)%num_N
print("Meu R2 calculado (Bob):", r2)

connectionSocket.send(str(r2).encode())  
r1 = int(connectionSocket.recv(1024).decode()) 
print("R1 obtido da Alice:", r1) 

chaveCalculada = (r1**y)%num_N
print("Chave calculada:", chaveCalculada) 

sentence = connectionSocket.recv(65000)
decrypted_bytes = cesar(sentence, - chaveCalculada)

sentence_uppercase = maiuscula(decrypted_bytes)
sentenceUPPER_bytes = sentence_uppercase.encode('utf-8')

encrypted_bytes = cesar(sentenceUPPER_bytes, chaveCalculada)
print("Mensagem criptografada enviada:", str(encrypted_bytes, "utf-8"))
connectionSocket.send(encrypted_bytes)
connectionSocket.close()