from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    @classmethod
    def ler(cls):
        nome = 'caio'
        idade = 20
        cpf = 59874222
        return Pessoa(nome,idade,cpf)

p1 = Pessoa('caio', 20, '1213156465')
PessoaDal.salvar(p1)