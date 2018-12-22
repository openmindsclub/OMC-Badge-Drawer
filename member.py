
class Member:
    def __init__(self):
        self.first_name = "None"
        self.family_name = "None"
        self.id = "0"

    def __init__(self, fname, faname, id):
        self.first_name = fname
        self.family_name = faname
        self.id = id

    def __init__(self, member_string):
        infos = member_string.split(",")
        self.family_name = infos[0]
        self.first_name = infos[1]
        self.id = infos[2].strip("\n")

    def display_informations(self):
        return "first_name : ",self.first_name,"family_name : ",self.family_name,"id : ",self.id

    def get_infos(self):
        return self.first_name, self.family_name, self.id
