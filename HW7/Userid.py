class UserId:
    member_info = dict()

    member_ids = list()

    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        UserId.member_info[self.id_number] = {"first_name": self.first_name,
                                              "last_name": self.last_name}
        UserId.member_ids.append(self.id_number)

    def get_user_id(self):
        return self.id_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __repr__(self):
        return UserId.member_ids


mohsen_bayat = UserId("Mohsen", "Bayat", 1001)
sobhan_taghadosi = UserId("Sobhan", "Taghadosi", 1002)
javad_jafari = UserId("Javad", "Jafari", 1003)
masoud_hosseini = UserId("Masoud", "Hosseini", 1004)
hassan_zand = UserId("Hassan", "Zand", 1005)
ali_ebadi = UserId("Ali", "Ebadi", 1006)
