from controller import PessoaControler
from dal import PessoaDal

while True:
    decisao = int(input('digite 1 para salva uma pessoa ou digite 2 para ver a pessoa salva e 3 para sair'))

    if decisao == 3:
        break
    if decisao == 1:
        nome = input('digite seu nome: ')
        idade = int(input('digite sua idade: '))
        cpf = input('digite seu cpf: ')
    
        if PessoaControler.cadastrar(nome,idade,cpf):
            print('usuario cadrastado com sucesso')

        else:
            print('digite valores validos')

