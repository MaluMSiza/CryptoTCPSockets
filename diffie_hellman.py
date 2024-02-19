# Função para calcular a exponenciação modular
def diffie_hellman(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result
# Função para codificar uma mensagem com a cifra de César
def caesar_cipher(bytes_data, int_chave):
    encrypted_bytes = bytearray()
    for byte in bytes_data:
        encrypted_byte = (byte + int_chave) % 256  # Ajusta para o intervalo de bytes (0-255)
        encrypted_bytes.append(encrypted_byte)
    return bytes(encrypted_bytes)







# Parâmetros compartilhados entre Alice e Bob## TUDO PARA TESTE
shared_prime = 23  # Um número primo compartilhado, "p"
shared_base = 5    # Um número de base compartilhado, "g"

# Alice gera sua chave privada
alice_private_key = 6
# Bob gera sua chave privada
bob_private_key = 15

# Alice calcula sua chave pública
alice_public_key = diffie_hellman(shared_base, alice_private_key, shared_prime)
# Bob calcula sua chave pública
bob_public_key = diffie_hellman(shared_base, bob_private_key, shared_prime)

# Alice e Bob trocam suas chaves públicas
# Alice recebe a chave pública de Bob
bob_to_alice = bob_public_key
alice_to_bob = alice_public_key


# Ambos calculam a chave de sessão
alice_session_key = diffie_hellman(bob_to_alice, alice_private_key, shared_prime)
bob_session_key = diffie_hellman(alice_to_bob, bob_private_key, shared_prime)

# Verificação se a chave de sessão calculada por Alice é igual à chave de sessão calculada por Bob
def compare_session_keys(session_key1, session_key2):
    return session_key1 == session_key2

result = compare_session_keys(alice_session_key, bob_session_key)
print("As chaves de sessão são iguais?", result)
if result:
    print("Valor da chave de sessão:", alice_session_key)

# Bytes originais
original_bytes = bytes("EU COMI MACARRÃO COM O BINGOLA E O ZÉ DA MANGA", 'utf-8')
print("\nMensagem original (em bytes):", original_bytes.decode('utf-8'))

# Codificar os bytes originais com a cifra de César com um deslocamento de 3
encrypted_bytes = caesar_cipher(original_bytes, alice_session_key)
print("Mensagem codificada com cifra de César:", encrypted_bytes)

decrypted_bytes = caesar_cipher(encrypted_bytes, - alice_session_key)
print("Mensagem decodificada com cifra de César:", decrypted_bytes.decode('utf-8'))

with open("mensagem_codificada_dh.txt", "wb") as file:
    file.write(decrypted_bytes)
