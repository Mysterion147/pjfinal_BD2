class CorpDatabase:
    def __init__(self, database):
        self.db = database

    # cria uma pessoa, nesse caso funcionário
    def create_person(self, id, name, sex, age):
        query = "CREATE (:Person {name: $name, id: $id, sex: $sex, age: $age})"
        parameters = {"id": id, "name": name, "sex": sex, "age": age}
        self.db.execute_query(query, parameters)

    # cria uma empresa
    def create_corporation(self, empresa):
        query = "CREATE (:Corporation {name: $name, id: $id, value: $value})"
        parameters = {"id": empresa.id, "name": empresa.name, "value": empresa.value}
        self.db.execute_query(query, parameters)

    # cria uma filial
    def create_branch(self, branch):
        query = "CREATE (:Branch {name: $name, id: $id})"
        parameters = {"id": branch.id, "name": branch.name}
        self.db.execute_query(query, parameters)

    # defoine carg
    def define_position(self, aimed_id, occupation):
        query = f"MATCH (n:Person{{id: $aimed_id}}) SET n:{occupation}"
        parameters = {"aimed_id": aimed_id}
        self.db.execute_query(query, parameters)

    # cria relacao de subordinacao
    def create_subordination(self, boss_id, sub_id):
        query = "MATCH (d:Person {id: $boss_id}), (a:Person {id: $sub_id}) CREATE (d) -[:CHEFE_DE]-> (a)"
        parameters = {"boss_id": boss_id, "sub_id": sub_id}
        self.db.execute_query(query, parameters)

    # cria relacao de representacao
    def create_representation(self, rep_id, branchid_id):
        query = "MATCH (d:Person {id: $rep_id}), (a:Branch {id: $branchid_id}) CREATE (d) -[:REPRESENTANTE_DE]-> (a)"
        parameters = {"rep_id": rep_id, "branchid_id": branchid_id}
        self.db.execute_query(query, parameters)

    # cria relacao de dono
    def create_ownership(self, owner_id, prop_id):
        query = "MATCH (d:Person {id: $owner_id}), (a:Corporation {id: $prop_id}) CREATE (d) -[:DONO_DE]-> (a)"
        parameters = {"owner_id": owner_id, "prop_id": prop_id}
        self.db.execute_query(query, parameters)

    # cria a relacao da filial e empresa
    def create_branch_relation(self, branch_id, corp_id):
        query = "MATCH (d:Branch {id: $branch_id}), (a:Corporation {id: $corp_id}) CREATE (d) <-[:EXTENDE]- (a)"
        parameters = {"branch_id": branch_id, "corp_id": corp_id}
        self.db.execute_query(query, parameters)

    # update o nome de uma corporacao
    def define_corp_name(self, aimed_id, new_name):
        query = f"MATCH (n:Corporation{{id: $aimed_id}}) SET n.name = {new_name}"
        parameters = {"aimed_id": aimed_id, "new_game": new_name}
        self.db.execute_query(query, parameters)

    # update o valor de uma corporacao
    def define_corp_value(self, aimed_id, new_value):
        query = f"MATCH (n:Corporation{{id: $aimed_id}}) SET n.value = {new_value}"
        parameters = {"aimed_id": aimed_id, "new_value": new_value}
        self.db.execute_query(query, parameters)

    # update nome de uma pessoa
    def define_person_name(self, aimed_id, new_name):
        query = "MATCH (n:Person {id: $aimed_id}) SET n.name = $new_name"
        parameters = {"aimed_id": aimed_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # update nome de uma filial
    def define_branch_name(self, aimed_id, new_name):
        query = "MATCH (n:Branch {id: $aimed_id}) SET n.name = $new_name"
        parameters = {"aimed_id": aimed_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # retorna o nome de todas pessoas do db
    def get_people(self):
        query = "MATCH (p:Person) RETURN p.name AS nome"
        results = self.db.execute_query(query)
        return [(result["nome"]) for result in results]

    #retorna a media de idade dos analistas
    def get_avg_analyst_age(self):
        query = "MATCH (p:Analyst) RETURN avg(p.age) AS media_idade"
        results = self.db.execute_query(query)
        return [(result["media_idade"]) for result in results]

    # retorna o nome de todas corporações do db
    def get_corps(self):
        query = "MATCH (p:Corporation) RETURN p.name AS nome"
        results = self.db.execute_query(query)
        return [(result["nome"]) for result in results]

    # retorna o nome de todas filiais do bd
    def get_branches(self):
        query = "MATCH (p:Branch) RETURN p.name AS nome"
        results = self.db.execute_query(query)
        return [(result["nome"]) for result in results]

    # retorna o nome dos donos de uma corp
    def get_owner(self):
        query = "MATCH (p:Owner) RETURN p.name AS nome"
        results = self.db.execute_query(query)
        return [(result["nome"]) for result in results]

    # retorna todos os subordinados de alguém
    def get_subbordinates(self, boss_id):
        query = f"MATCH (p1:Person{{id: $boss_id}})-[:CHEFE_DE]->(p2:Person) RETURN p2.name AS nome"
        parameters = {"boss_id": boss_id}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"]) for result in results]

    # deleta uma entidade pessoa
    def delete_person(self, id):
        query = "MATCH (p: Person {id: $id}) DETACH DELETE p"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    # deleta uma entidade corporacao
    def delete_corp(self, id):
        query = "MATCH (p: Corporation {id: $id}) DETACH DELETE p"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    # deleta uma entidade filial
    def delete_branch(self, id):
        query = "MATCH (p: Branch {id: $id}) DETACH DELETE p"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)
