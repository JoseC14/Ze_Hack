import random
import string

def gerar_senha(tamanho = 10):
    alfanumeric = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += random.choice(alfanumeric)
    
    return senha

print("GERADOR DE SENHAS")

tamanho = int(input("Digite o tamanho da senha que você quer(deixe vazio para padrão): "))
print(f"Sua senha: {gerar_senha(tamanho)}")




