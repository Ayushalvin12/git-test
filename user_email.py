class User:
    raise_amt=1.05


    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    

    def full_name(self):
        return f"{self.first} {self.last}"
    

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay



# user1=User("Ayush","KC",50000)
# print(user1.email())

