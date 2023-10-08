from dal import PessoaDal
from model import Pessoa
class PessoaControler:
    @classmethod
    def cadastrar(cls, nome ,idade, cpf):
        if len(nome) > 8 and (int(idade) > 0 and int(idade) < 200) and len(cpf) == 10:
            try:
                PessoaDal.salvar(Pessoa(nome,idade,cpf))
                return True
            except:
                return False
        else:
            return False
        

PessoaControler.cadastrar('caio',20,'12354651')