
# existe alguma entidade que é genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades ?

# estamos falando de um banco de dinheiros, então será voltado para pessoas

#  Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada 

# Quando uma classe herda de outra classe, a classe herdada é conhecida como
# Super Classe
# classe mãe 
# classe pai
# classe base
# Classe Genérica   

""" 
 Quando uma classe herda de outra classe, ela é chamada:

 - Sub Classe 
 - Classe Filha 
 - Classe Específica 

"""

# sobrescrita de métodos ocorre quando reescrevemos / reimplementamos um método presente na super classe em classes filhas

from Dados.pessoa import Pessoa 
from Dados.dados import clientes , funcionarios


class Cliente(Pessoa): #estamos herdando a classe Pessoa 

    def __init__(self , nome , sobrenome , cpf , email , renda : float):
        super().__init__(nome , sobrenome , cpf , email)
        self.__renda = renda

    def dados_do_cliente(self):
        return (
            f"{super().dados_da_pessoa()}Renda do Cliente : {self.__renda} \n"
        )
    
    """
return (

    f"Nome do Cliente : {self._Pessoa__nome}"
    f"Sobrenome do Cliente : {self._Pessoa__sobrenome}"
    f"Cpf do cliente : {self._Pessoa__cpf}"
    f"Email da cliente : {self._Pessoa__email}"
    f"Renda da cliente : {self.__renda}"  
    
    )
    """
    
class Funcionario(Pessoa):
    
    def __init__(self , nome , sobrenome , cpf , email , matricula : int ):
        super().__init__( nome , sobrenome , cpf , email )
        self.__matricula = matricula
    
    def dados_do_funcionario(self):
        return super().dados_da_pessoa() + f"Matricula do funcionario : {self.__matricula}" # duas formas de se fazer essa reimplementação 



for cliente in clientes:
    cliente = Cliente( nome = cliente['nome'] , sobrenome = cliente['sobrenome'] , cpf = cliente['cpf'] , email = cliente['email'] , renda = cliente['renda'] )

    print(cliente.dados_do_cliente()) # consumindo api com python

for funcionario in funcionarios:
    funcionario = Funcionario( nome = funcionario['nome'] , sobrenome = funcionario['sobrenome'] , cpf = funcionario['cpf'] , email = funcionario['email'] , matricula = funcionario['matricula'] )

    print(funcionario.dados_do_funcionario())













# print(Cliente1.__dict__) observar os dados do Cliente
# print(Funcionario1.__dict__) observar os dados do funcionario


