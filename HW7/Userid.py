class UserId:
    member_info = dict()

    member_ids = list()

    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        Userid.member_info[self.id_number] = {"first_name": self.first_name,
                                              "last_name": self.last_name}
        Userid.member_ids.append(self.id_number)

    def get_user_id(self):
        return self.id_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __repr__(self):
        return Userid.member_ids


mohsen_bayat = Userid("Mohsen", "Bayat", 1001)
sobhan_taghadosi = Userid("Sobhan", "Taghadosi", 1002)
javad_jafari = Userid("Javad", "Jafari", 1003)
masoud_hosseini = Userid("Masoud", "Hosseini", 1004)
hassan_zand = Userid("Hassan", "Zand", 1005)
ali_ebadi = Userid("Ali", "Ebadi", 1006)
