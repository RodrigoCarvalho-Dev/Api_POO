class Pessoa():
    def __init__(self,  nome : str , sobrenome : str , cpf , email ):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf 
        self.__email = email

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    
    
    def dados_da_pessoa(self):
        return (
            
            f"Nome da Pessoa : {self.__nome} \n"
            f"Sobrenome da Pessoa : {self.__sobrenome} \n"
            f"CPF da pessoa : {self.__cpf} \n"
            f"Email da pessoa : {self.__email} \n" 

            )
        