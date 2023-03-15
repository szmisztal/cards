class BaseContact():
    def __init__(self, name, surname, phone, email):
        self.name = name 
        self.surname = surname
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.name} {self.surname}, {self.phone}, {self.email}"
    def contact(self):
        print("Kontaktuję się z:", self)
    @property
    def name_length(self):
        return len(self.name + self.surname)
    
class BussinesContact(BaseContact):
    def __init__(self, profession, company, bussines_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profession = profession
        self.company = company
        self.bussines_phone = bussines_phone