class Console:
    def __init__(self, corp2):
        self.corp2 = corp2
        # dicionario com as opcoes de entrada
        self.opcoes = {
            '1': self.owner_out,
            '2': self.subordinates_of,
            '3': self.anal_avg_age,
            '4': self.all_p,
            '5': self.all_c,
            '6': self.all_b,
            '7': self.delete_pers,
            '8': self.delete_corp,
            '9': self.delete_bran,
            '10': self.update_person_name,
            '11': self.update_corp_name,
            '12': self.update_corp_value,
            '13': self.update_branch_name,
            '0': self.sair
        }

    def exibir(self):
        while True:
            self.mostrar_opcoes()
            opcao = input('Digite o número da opção desejada: ')
            if opcao in self.opcoes:
                self.opcoes[opcao]()
            else:
                print('Opção inválida. Tente novamente.')

    def mostrar_opcoes(self):
        print(' M E N U ')
        print("Entre com o número")
        print('1. Donos de empresas')
        print('2. Subordinados de [entrar com id]')
        print('3. Media de idade dos analistas')
        print('4. Todas pessoas do BD')
        print('5. Todas empresas do BD')
        print('6. Todas as filiais')
        print('7. Deletar pessoa')
        print('8. Deletar empresa')
        print('9. Deletar filial')
        print('10. Atualizar pessoa (nome)')
        print('11. Atualizar empresa (nome)')
        print('12. Atualizar empresa (valor)')
        print('13. Atualizar filial (nome)')
        print('0. Sair')

    # definindo todos os métodos que serão usados pelo dicionario
    def owner_out(self):
        print("As seguintes pessoas sao donos de uma corporacao: ")
        print(self.corp2.get_owner())

    def subordinates_of(self):
        wanted_id = input("Qual o id da pessoa desejada? ")
        print("A pessoa buscada possui subordinados de nome: ")
        print(self.corp2.get_subbordinates(wanted_id))

    def anal_avg_age(self):
        print("A media de idade dos analistas é: ")
        print(self.corp2.get_avg_analyst_age())

    def all_p(self):
        print("Todas as pessoas do banco: ")
        print(self.corp2.get_people())

    def all_c(self):
        print("Todas as empresas do banco: ")
        print(self.corp2.get_corps())

    def all_b(self):
        print("Todas as filiais do banco: ")
        print(self.corp2.get_branches())

    def delete_pers(self):
        wanted_id = input("Qual o id da pessoa a ser deletada? ")
        self.corp2.delete_person(wanted_id)
        print("Pessoa deletada!")

    def delete_corp(self):
        wanted_id = input("Qual o id da pessoa a ser deletada? ")
        self.corp2.delete_corp(wanted_id)
        print("Empresa deletada!")

    def delete_bran(self):
        wanted_id = input("Qual o id da pessoa a ser deletada? ")
        self.corp2.delete_branch(wanted_id)
        print("Filial deletada!")

    def update_person_name(self):
        wanted_id = input("Qual o id da pessoa a ter seu nome alterado? ")
        new_name = input("Insira o novo nome: ")
        self.corp2.define_person_name(wanted_id, new_name)

    def update_corp_name(self):
        wanted_id = input("Qual o id da empresa a ter seu nome alterado? ")
        new_name = input("Insira o novo nome: ")
        self.corp2.define_corp_name(wanted_id, new_name)

    def update_corp_value(self):
        wanted_id = input("Qual o id da empresa a ter seu valor alterado? ")
        new_value = input("Insira o novo valor: ")
        self.corp2.define_corp_value(wanted_id, new_value)

    def update_branch_name(self):
        wanted_id = input("Qual o id da filial a ter seu nome alterado? ")
        new_name = input("Insira o novo nome: ")
        self.corp2.define_branch_name(wanted_id, new_name)

    def sair(self):
        print("Encerrando a consulta!")
        exit()
