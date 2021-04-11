class Userid:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def get_user_id(self):
        return self.id_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
