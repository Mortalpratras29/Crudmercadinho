import os
from menus import cipal
import json


def carregar_produtos():
    try:
        with open("indb.json", "r", encoding="utf8") as file:
            produtos = json.load(file)
            return produtos
    except FileNotFoundError:
        print("Arquivo não encontrado. Retornando lista vazia.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON. Retornando lista vazia.")
        return []


def google(busca):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto["ID"] == busca:
            return produto
    return None


def salvar_produtos(produtos):
    with open("indb.json", "w", encoding="utf8") as file:
        json.dump(produtos, file, indent=2)


def atualizar_produto(produto_atualizado):
    produtos = carregar_produtos()
    for i, produto in enumerate(produtos):
        if produto["ID"] == produto_atualizado["ID"]:
            produtos[i] = produto_atualizado
            salvar_produtos(produtos)
            return
    print("Produto não encontrado para atualização.")


while True:
    print(cipal)
    menu = int(input("Escolha uma opção: "))

    if menu == 1:
        os.system("cls")
        nome = str(input("Produto: "))
        preco = float(input("Preço: "))
        quant = int(input("Quantidade: "))
        ID = int(input("ID do produto: "))

        produto = {"Nome": nome, "Preco": preco, "Quantidade": quant, "ID": ID}

        produtos = carregar_produtos()
        produtos.append(produto)
        salvar_produtos(produtos)

    elif menu == 2:
        os.system("cls")
        produtos = carregar_produtos()
        if produtos:
            print(json.dumps(produtos, indent=2))
        else:
            print("Nenhum produto cadastrado.")

    elif menu == 3:
        busca = int(input("Digite id do produto: "))

        produtos = carregar_produtos()
        produto_encontrado = None
        for produto in produtos:
            if produto["ID"] == busca:
                produto_encontrado = produto
                break

        if produto_encontrado:
            produtos.remove(produto_encontrado)
            salvar_produtos(produtos)
            print("Produto removido com sucesso")
        else:
            print("Produto não encontrado")

    elif menu == 4:
        busca = int(input("Digite id do produto: "))

        produto = google(busca)
        if produto:
            print(
                f"""
    || Mercado Guanabara ||

    1- Nome: {produto['Nome']}
    2- Preço: {produto['Preco']}
    3- Quantidade: {produto['Quantidade']}
"""
            )
            mudar = int(input("Escolha o campo a ser alterado: "))
            if mudar == 1:
                produto["Nome"] = str(input("Novo nome: "))
            elif mudar == 2:
                produto["Preco"] = float(input("Novo preço: "))
            elif mudar == 3:
                produto["Quantidade"] = int(input("Nova quantidade: "))
            else:
                print("Escolha inválida")

            atualizar_produto(produto)
        else:
            print("Produto não encontrado.")

    elif menu == 5:
        busca = int(input("Digite id do produto: "))
        produto = google(busca)
        if produto:
            porcem = int(input("Escolha a porcentagem da promoção: "))
            subtracao = (produto["Preco"] * porcem) / 100
            produto["Preco"] = produto["Preco"] - subtracao
            print(f'O produto {produto["Nome"]} entrou em promoção de {porcem}%')
            atualizar_produto(produto)
        else:
            print("Produto não encontrado.")

    elif menu == 6:
        os.system("cls" if os.name == "nt" else "clear")
        break

    else:
        print("Escolha inválida")
