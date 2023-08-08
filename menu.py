import os




def main():
    while True:
        print('\n ==== MENU-CLIENTES ====')
        print('* - 1 listarar clientes cadastrados(mostrar apenas a quantidades de clientes ja cadastrados, sem mostrar dados)')
        print('* - 2 cadastrar novos clientes')
        print('* - 3 listar clientes cadastrados(com algum identificador listar todas as informacoes sensiveis de um cliente cadastrado)')
        print('* - 4 alterar dados sensiveis de cleintes ja cadastrados')
        print('* - 5 remover clientes cadastrados(so remover um cliente por vez, e somente atraves do identificador o cliente podera ser removido com exito)')
        print('* - 6 sair do sistema! ')

        acao=input('Seleciona alguma opcao do menu para comecar a operacao: ')

        if acao == '1':
           ...
        elif acao == '2':
            ...
        elif acao == '3':
            ...
        elif acao == '4':
            ...
        elif acao == '5':
            ...
        elif acao == '6':
            print('Saindo do sistema! ')
            break
        else:
            print('acao invalida digite uma acao valida por favor: 1, 2, 3, 4, 5 ou 6')

if __name__ == '__main__':
        main()