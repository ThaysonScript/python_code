def deletar_item():
    deletar_item = input("Digite o nome do item que deseja excluir: ")
    linhas_atualizadas = []
    with open("dados.csv", "r") as dados:
        for linha in dados:
            fabricante, modelo, serial = linha.strip().split(",")
            
            if fabricante != deletar_item:
                linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
                
    print(f"Registro com o nome '{deletar_item}' foi excluído.")
                
    registrar_delete(linhas_atualizadas)


def registrar_delete(dados_armazenados):

    with open("dados.csv", "w") as arquivo_csv:
        for dado in dados_armazenados:
            arquivo_csv.writelines(dado)
