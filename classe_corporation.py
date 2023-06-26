class Corp:
    def __init__(self, name, id, value):
        self.name = name
        self.id = id
        self.value = value
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        self.branches.remove(branch)