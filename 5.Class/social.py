import datetime

class User:
    """This is a description of th class"""
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
    def age(self):
        today = datetime.date.today()
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_day = (today - dob).days
        age_in_year = age_in_day / 365
        return int(age_in_year)
    def introduce(self):
        text = "Hello, I am {firstName}, I am {age} years old".format(firstName = self.name, age = self.age())
        return text
Enrique = User("Enrique Ramos", "19911129")


print(Enrique.introduce())
