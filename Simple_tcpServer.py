from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)
received = str(sentence,"utf-8")
print ("Received From Client: ", received)

# def uppercase_com_acento(texto):
#     acentos = {'á': 'Á', 'à': 'À', 'â': 'Â', 'ã': 'Ã', 'é': 'É', 'è': 'È', 'ê': 'Ê', 'í': 'Í', 'ì': 'Ì', 'î': 'Î', 'ó': 'Ó', 'ò': 'Ò', 'ô': 'Ô', 'õ': 'Õ', 'ú': 'Ú', 'ù': 'Ù', 'û': 'Û', 'ç': 'Ç'}

#     texto_uppercase_com_acento = ''
#     for char in texto:
#         if char in acentos:
#             texto_uppercase_com_acento += acentos[char]
#         else:
#             texto_uppercase_com_acento += char.upper()

#     return texto_uppercase_com_acento

def cesar(sentence, shift):
    acentos = {'á': 'Á', 'à': 'À', 'â': 'Â', 'ã': 'Ã', 'é': 'É', 'è': 'È', 'ê': 'Ê', 'í': 'Í', 'ì': 'Ì', 'î': 'Î', 'ó': 'Ó', 'ò': 'Ò', 'ô': 'Ô', 'õ': 'Õ', 'ú': 'Ú', 'ù': 'Ù', 'û': 'Û', 'ç': 'Ç'}
    
    ciphered_message = ""


    for char in sentence:
        if char.isalpha(): 
            if char in acentos:
                ciphered_char += acentos[char]
            elif char.islower():  
                ciphered_char = chr((ord(char) - 97 + shift) % 26 + ord('a'))
            else:  
                ciphered_char = chr((ord(char) - 65 + shift) % 26 + ord('A'))
        else:  
            ciphered_char = char
        ciphered_message += ciphered_char
    return ciphered_message

# mensagem_uppercase_com_acento = uppercase_com_acento(received)
mensagem_cifrada = cesar(received, - 3)  # Aqui usamos um deslocamento de 3, você pode alterar conforme necessário
print("Mensagem cifrada:", mensagem_cifrada)

capitalizedSentence = mensagem_cifrada.upper().encode("utf-8")
connectionSocket.send(capitalizedSentence)
sent = str(capitalizedSentence,"utf-8")
print ("Sent back to Client: ", sent)
connectionSocket.close()