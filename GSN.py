
produto=[]
ans=True
n=0
p = 0

while ans:
    print("""
    1 - Listar Produtos
    2 - Cadastrar Produtos
    3 - Alterar Produto
    4 - Excluir Produto
    5 - Sair do programa 
    """)

    ans=int(input("O que deseja?"))
    if ans==1:
        for item in produto:
            print(item["cod"],"'", item["nome"],"'",item["description"],"'",item["valor"])

    elif ans==2:
        name = input("Nome do produto\n")
        description = input("Digite a descrição do produto\n")
        valor = input("Qual é o valor?\n")
        n = n+1
        item = {
            "cod": n,
            "nome": name,
            "description": description,
            "valor": valor
            }
        produto.append(item)

    elif ans == 3:

        a = int(input("Qual produto você deseja alterar?"))
        for item in produto:

            if (item["cod"] == a):

                item["nome"] = input("Qual o novo nome?")
                item["description"] = input("Qual a nova descrição?")
                item["valor"] = input("Qual o novo valor?")
                break

    elif ans == 4:

        a = int(input("Qual produto você deseja excluir?"))
        for item in produto:
            if (item["cod"] == a):
                produto.pop(p)
            p=p+1

    elif ans == 5:
        break

    elif ans !=" ":
        print("Não entendi, REPITA!")

