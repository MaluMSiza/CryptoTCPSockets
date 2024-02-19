# Função para codificar uma mensagem com a cifra de César, ele recebe em bytes e retorna os bytes
# COLAR ESTA
def caesar_cipher(bytes_data, int_chave):
    encrypted_bytes = bytearray()
    for byte in bytes_data:
        encrypted_byte = (byte + int_chave) % 256  # Ajusta para o intervalo de bytes (0-255)
        encrypted_bytes.append(encrypted_byte)
    return bytes(encrypted_bytes)




###  AS FUNÇÕES ABAIXO FORAS PARA TESTE ### NAO COPIE
# Função para decodificar uma mensagem codificada com a cifra de César
def caesar_cipher_decode(encrypted_bytes, int_chave):
    return caesar_cipher(encrypted_bytes, -int_chave)

# Bytes originais
original_bytes = bytes("EU COMI MACARRÃO", 'utf-8')

# Codificar os bytes originais com a cifra de César com um deslocamento de 3
encrypted_bytes = caesar_cipher(original_bytes, 3)
print("Mensagem codificada:", encrypted_bytes)

# Decodificar os bytes codificados com a cifra de César com um deslocamento de 3
decoded_bytes = caesar_cipher_decode(encrypted_bytes, 3)
print("Mensagem decodificada:", decoded_bytes.decode('utf-8'))

with open("mensagem_codificada.txt", "wb") as file:
    file.write(decoded_bytes)
