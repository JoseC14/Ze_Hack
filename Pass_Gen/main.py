from Senha import Senha
print("GERADOR DE SENHAS")

tamanho = int(input("Digite o tamanho da senha que você quer(deixe vazio para padrão): "))
senha = Senha(tamanho=tamanho)
print(f"Sua senha: {senha.gerar_senha()}")
del senha




