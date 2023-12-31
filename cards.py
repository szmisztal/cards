from faker import Faker
fake = Faker()


class BaseContact():
    def __init__(self, name, surname, phone, email):
        self.name = name 
        self.surname = surname
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"{self.name} {self.surname}, {self.phone}, {self.email}"
    
    def contact(self):
        print(f"Wybieram numer prywatny: {self.phone} i dzwonię do {self.name} {self.surname}")
    
    @property
    def name_length(self):
        return len(self.name + self.surname)
    
class BussinesContact(BaseContact):
    def __init__(self, profession, company, bussines_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profession = profession
        self.company = company
        self.bussines_phone = bussines_phone
    
    def __str__(self):
        return super().__str__() + f", {self.profession}, {self.company}, {self.bussines_phone}"
    
    def contact(self):
        print(f"Wybieram numer służbowy: {self.bussines_phone} i dzwonię do {self.name} {self.surname} z firmy {self.company}")

    @property
    def name_length(self):
        return len(self.name + self.surname)
    
card_1 = BussinesContact(name = "Szymon", surname = "Misztal", phone = "123456789", email = "sz.misztal@gmail.com", profession = "Driver", company = "Orlen", bussines_phone = "987654321")
card_2 = BussinesContact(name = "Tomasz", surname = "Łysoń", phone = "123789456", email = "t.łysoń@gmail.com", profession = "IT Specialist", company = "Fujitsu", bussines_phone = "654987321")
card_3 = BussinesContact(name = "Piotr", surname = "Lauk", phone = "456789123", email = "p.lauk@gmail.com", profession = "Programmer", company = "Volkswagen", bussines_phone = "321987654")
card_4 = BussinesContact(name = "Radosław", surname = "Misztal", phone = "456123789", email = "r.misztal@gmail.com", profession = "Cook", company = "SoloPizza", bussines_phone = "987321654")
card_5 = BussinesContact(name = "Jagoda", surname = "Sarzyńska", phone = "789123456", email = "j.sarzynska@gmail.com", profession = "Personnel Manager", company = "BNP", bussines_phone = "654321987")
cards = [card_1, card_2, card_3, card_4, card_5]

for card in cards:
    print(card)
    
def create_contacts(card_type, amount):
    contacts = []
    for i in range(amount):
        if card_type == "base":
            contact = BaseContact(name = fake.first_name(), surname = fake.last_name(), phone = fake.phone_number(), email = fake.email())
        elif card_type == "bussines":
            contact = BussinesContact(name = fake.first_name(), surname = fake.last_name(), phone = fake.phone_number(), email = fake.email(), profession = fake.job(), company = fake.company(), bussines_phone = fake.phone_number())
        else:
            raise ValueError("Wrong card type.")
        contacts.append(contact)
    return contacts
        
base_contacts = create_contacts("base", 3)
bussines_contacts = create_contacts("bussines", 5)

for contact in base_contacts:
    print(contact)

for contact in bussines_contacts:
    print(contact)

card_1.contact()