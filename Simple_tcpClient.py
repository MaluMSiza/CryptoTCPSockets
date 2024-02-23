def diffieHellman(g, y, n):
    result = (g**y)%n
    
    return result


def caesarEncrypter(bytesData, intChave):
    encryptedBytes = bytearray()
    for byte in bytesData:
        encryptedByte = (byte + intChave) % 256 
        encryptedBytes.append(encryptedByte)
    return bytes(encryptedBytes)


def send(sessionKey):
    sentence = input("Input lowercase sentence: ")
    encryptedMessage = caesarEncrypter(sentence.encode(), sessionKey)
    clientSocket.send(encryptedMessage)


def receive(modifiedSentence, sessionKey):




    decripted = caesarEncrypter(modifiedSentence, -sessionKey)


    string = decripted.decode("utf-8")
    conversionTable = {
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
    uppercase_string = ''.join(conversionTable.get(char, char.upper()) for char in string)
    print(uppercase_string)


from socket import *
g = 23
n = 5 
y = 6
r1 = (g**y)%n
serverName = "10.1.70.19"
serverPort = 12000


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(str(r1).encode())
r2 = int(clientSocket.recv(1024).decode())
k = (r2**y)%n


send(k)
modifiedSentence = receive(clientSocket.recv(1024),int(k))
clientSocket.close()