# Importar modulos do codigo
import cadastrar_item
import ver_items
import atualizar_item
import deletar_item
import persistencia_arquivo_csv

# 2.1. Menu inicial para o usuário selecionar a opção de interesse 
def menu_usuario():
    while True:
        print("\n'''''' ESCOLHA UMA OPÇÃO ''''''''''\n")
        print("[1].CADASTRAR ITEM")
        print("[2].BUSCAR ITEM")
        print("[3].EDITAR ITENS CADASTRADOS")
        print("[4].REMOVER ITEM CADASTRADO")
        print("[5].PERSISTIR DADOS EM ARQUIVO.CSV")
        print("[6].SAIR\n")
        print("''''''''''''''''''''''''''''''''''''")
    
        # selecionar a opção de interesse
        escolha = input('Digite uma opção de escolha acima: ')
    
        if escolha == '1':
            cadastrar_item.cadastrar_item()
            
        elif escolha == '2':
            ver_items.visualizar_item()
            
        elif escolha == '3':
            atualizar_item.atualizar_dados()
            
        elif escolha == '4':
            deletar_item.deletar_item()
            
        elif escolha == '5':
            persistencia_arquivo_csv.persistir_dados_arquivo_csv()
        
        elif escolha == '6':
            print("\n******** SAINDO DO PROGRAMA *********\n")
            break
        
        else:
            print('Digite uma opção válida!')
            
            
if __name__ == '__main__':
    menu_usuario()