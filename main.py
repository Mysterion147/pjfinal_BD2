from database import Database
from proj_database import CorpDatabase
from console import Console
from classe_corporation import Corp
from classe_branch import Branch

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.211.218.181:7687", "neo4j", "ramps-concerns-notes")
db.drop_all()

# criando uma instância da classe FamilyDatabase para interagir com o banco de dados
corporation_db = CorpDatabase(db)

# criando as classes das empresas e filiais
empresa1 = Corp("Grupo 935", "456a", 100000)
branch1_1 = Branch("Branch A", "789a")
branch1_2 = Branch("Branch B", "789b")
branch1_1.set_corp(empresa1)
branch1_2.set_corp(empresa1)
empresa1.add_branch(branch1_1)
empresa1.add_branch(branch1_2)

# burner corp
empresa2 = Corp("Shell Company", "000z", 150000)
branch2_1 = Branch("Branch Zeta", "000a")
branch2_1.set_corp(empresa2)
empresa2.add_branch(branch2_1)

# criando as entidades
corporation_db.create_person("123a", "John Murray II", "M", 45)
corporation_db.create_person("123b", "Katarina", "F", 36)
corporation_db.create_person("123c", "Michael", "M", 45)
corporation_db.create_person("123d", "Joseph", "M", 25)
corporation_db.create_person("123e", "Leonardo", "M", 20)
corporation_db.create_person("123f", "Maria", "F", 19)
corporation_db.create_person("123g", "Shen", "M", 22)
corporation_db.create_person("010a", "Charlie", "M", 54) # burner
corporation_db.create_corporation(empresa1)
corporation_db.create_branch(branch1_1)
corporation_db.create_branch(branch1_2)
# burner
corporation_db.create_corporation(empresa2)
corporation_db.create_branch(branch2_1)

# atribuindo segunda label as pessoas
corporation_db.define_position("123a", "Owner")
corporation_db.define_position("010a", "Owner") # burner
corporation_db.define_position("123b", "Manager")
corporation_db.define_position("123c", "Manager")
corporation_db.define_position("123d", "Analyst")
corporation_db.define_position("123e", "Analyst")
corporation_db.define_position("123f", "Analyst")
corporation_db.define_position("123g", "Analyst")

# criando as relacoes de dono, representante, 'filial de' e subordinacao10
corporation_db.create_ownership("123a", "456a")
corporation_db.create_ownership("010a", "000z") # burner
corporation_db.create_branch_relation("789a", "456a")
corporation_db.create_branch_relation("789b", "456a")
corporation_db.create_branch_relation("000a", "000z") # burner
corporation_db.create_representation("123b", "789a")
corporation_db.create_representation("123c", "789b")
corporation_db.create_subordination("123b", "123d")
corporation_db.create_subordination("123b", "123e")
corporation_db.create_subordination("123c", "123f")
corporation_db.create_subordination("123c", "123g")

# criando o console e chamando seu método de exibicao
user_menu = Console(corporation_db)
user_menu.exibir()

# fechando a conexão
db.close()