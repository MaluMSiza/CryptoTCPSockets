# CryptoTCPSockets
Secure TCP Communication with Caesar Cipher and Diffie-Hellman

Este repositório contém um exemplo de implementação de comunicação segura entre um servidor TCP e um cliente TCP usando a cifra de César para criptografia 
e o protocolo de troca de chaves Diffie-Hellman para estabelecer uma chave compartilhada.

## Estrutura do Repositório

- `tcpServer.py`: O arquivo contendo a implementação do servidor TCP.
- `tcpClient.py`: O arquivo contendo a implementação do cliente TCP.
- `caesar_cipher.py`: O arquivo contendo a implementação da cifra de César para criptografia para teste sem servidor.
- `diffie_hellman.py`: O arquivo contendo a implementação do protocolo de troca de chaves Diffie-Hellman para teste sem servidor.

## Pré-requisitos

Certifique-se de ter Python 3 instalado em seu sistema.

## Como Usar

1. Clone este repositório em sua máquina local.
2. Execute `python3 tcpServer.py` para iniciar o servidor TCP.
3. Execute `python3 tcpClient.py` para iniciar o cliente TCP.
4. Siga as instruções fornecidas pelo cliente para estabelecer a comunicação segura com o servidor.
