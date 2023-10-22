class User:
    def __init__(self,name,username,email):
        self.name = name
        self.username = username
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi {self.username}\nIsmi: {self.name}\nemail: {self.email}"

user1 = User('Vepa Kurbanklichev','v_kurbanklichev','v.kurbanklichev@gmail.com')
print(user1.get_info())