def clacular_imprimir(largura, comprimento):
    area = float(largura) * float(comprimento)
    return area


print (clacular_imprimir (2, 3))

# Listas com dados de produtos
nomes_produtos = ["Produto A", "Produto B", "Produto C"]
precos_produtos = [10.0, 20.5, 30.0]
quantidades_produtos = [100, 50, 75]

# Função para imprimir um produto específico
def imprimir_produto(indice):
    if 0 <= indice < len(nomes_produtos):
        print(f"Produto: {nomes_produtos[indice]}")
        print(f"Preço: R${precos_produtos[indice]:.2f}")
        print(f"Quantidade: {quantidades_produtos[indice]}")
    else:
        print("Índice inválido!")

# Função para retirar um produto das listas
def retirar_produto(indice):
    if 0 <= indice < len(nomes_produtos):
        del nomes_produtos[indice]
        del precos_produtos[indice]
        del quantidades_produtos[indice]
        print(f"Produto removido com sucesso!")
    else:
        print("Índice inválido!")

# Testando as funções
# Imprimindo o produto na posição 1 (Produto B)
print("Impressão do Produto na posição 1:")
imprimir_produto(1)
print("\n")

# Retirando o produto na posição 0 (Produto A)
print("Retirando o Produto na posição 0:")
retirar_produto(0)
print("\n")

# Tentando imprimir o produto na posição 0 após a remoção
print("Tentando imprimir o Produto na posição 0 após remoção:")
imprimir_produto(0)
